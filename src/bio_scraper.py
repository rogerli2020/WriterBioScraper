import json
import time
import random
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from datetime import datetime
from src.page_source_getter import PageSourceGetter

DEFAULT_WARNING_LOG_PATH = './scraper_warnings.txt'


class BioScraper:
    def __init__(self, urls_path, selectors_path, save_path, shuffle, verbose_mode=False) -> None:
        self.urls_path = urls_path
        self.selectors_path = selectors_path
        self.save_path = save_path
        self.shuffle = shuffle
        self.verbose_mode = verbose_mode
        self.page_source_getter = PageSourceGetter()
        self.domain_to_selectors = {}
        self.default_post_selectors = {
            'email': 'href',
            'twitter': 'href',
            'linkedin': 'href',
            'facebook': 'href',
            'instagram': 'href',
            'pfp': 'src',
            'single_article_url': 'href',
        }
        self._load_data()
    

    def _load_data(self):
        print("Loading outlet scraper information...")
        with open(self.selectors_path, 'r') as jsonl_file:
            json_lines = ""
            for line in jsonl_file:
                json_lines += line.strip()
                try:
                    data = json.loads(json_lines)
                    domain = self.get_url_domain(data['url'])
                    self.domain_to_selectors[domain] = data
                    json_lines = ""
                except json.JSONDecodeError:
                    continue
        print(f"Scraper information loaded for {len(self.domain_to_selectors)} outlets.")


    def get_urls_list(self):
        urls = []
        with open(self.urls_path, 'r') as f:
            for url in f.readlines():
                url = url.replace('\n', '')
                if url: urls.append(url)
        if self.shuffle:
            random.shuffle(urls)
        return urls
    

    def get_url_domain(self, url) -> str:
        return urlparse(url).netloc
    

    def complete_url(self, base_url, relative_url):
        return urljoin(base_url, relative_url)


    def scrape_single_page(self, url):

        def apply_post_selectors(raw_elems : list, select_text : bool=False, post_selector : str=None) -> list[str]:
            if select_text: return [elem.text.replace('\n',' ').replace('\t', ' ').strip() for elem in raw_elems]
            else: return [elem.get(post_selector) for elem in raw_elems]

        def post_process(json_obj : dict):
            """
            Organize the articles into JSON/dict objects.
            Remove redundant information after organizing.
            Complete partial URLs.
            Delete unnecessary items.
            """
            # =============== complete URLs =============== 
            json_obj['single_article_url'] = [self.complete_url(json_obj['url'], url) for url in json_obj['single_article_url']]
            if 'pfp' in json_obj: json_obj['pfp'] = [self.complete_url(json_obj['url'], url) for url in json_obj['pfp']]
            # =============== organizie articles =============== 
            articles = []
            while (
                json_obj.get('single_article_title')
            ):
                new_article = {
                    'article_title': json_obj['single_article_title'].pop() if json_obj['single_article_title'] else None, 
                    'article_description':json_obj['single_article_description'].pop() if json_obj['single_article_description'] else None, 
                    'article_date':json_obj['single_article_date'].pop() if json_obj['single_article_date'] else None,
                    'article_url':json_obj['single_article_url'].pop() if json_obj['single_article_url'] else None,
                }
                articles.append(new_article)
            json_obj['articles'] = articles
            # =============== delete unncessary fields =============== 
            keys_to_delete = set(['single_article', 'single_article_title', 'single_article_description', 'single_article_date', 'single_article_url'])
            for key, val in json_obj.items():
                if not val: keys_to_delete.add(key)
            for key in list(keys_to_delete):
                del json_obj[key]
            for key, val in json_obj.items():
                if key != "articles" and val and type(val) == list: json_obj[key] = str(val[0])
            # =============== clean up name =============== 
            if 'name' in json_obj:
                json_obj['name'] = json_obj['name'].replace('About', '').replace(',','').strip()
                if ' - ' in json_obj['name']:
                    json_obj['name'] = json_obj['name'].split(' - ')[0].strip()
            # =============== add more fields and return =============== 
            json_obj['scrape_datetime'] = datetime.now().timestamp()
            return json_obj

        # obtain selectors and apply selectors for all fields.
        print(f'Processing {url}...')
        res, raw_elements = {'url':url}, {}

        url_domain = self.get_url_domain(url)

        # if domain does not have a scraper, log and return
        if url_domain not in self.domain_to_selectors:
            print(f'[WARNING] Could not find scraper for domain {url_domain}')
            with open('./could_not_process.txt', '+a') as file:
                file.write(url + '\n')
                return
        
        page_source = self.page_source_getter.get_page_source(url)

        # if page_source is blank,, log and return
        if not page_source:
            print(f'[WARNING] Could not get page source for {url}')
            with open('./could_not_process.txt', '+a') as file:
                file.write(url + '\n')
                return

        if page_source == None: page_source = ''
        soup = BeautifulSoup(page_source, 'html.parser')
        selectors = self.domain_to_selectors[url_domain]['selectors']
        post_selectors = self.domain_to_selectors[url_domain]['post_selectors']
        for field, selector in selectors.items():
            if selectors[field]: 
                raw_elements[field] = soup.select(selector)
            else: raw_elements[field] = []
        
        # apply "post_selectors"...
        for field, elems in raw_elements.items():
            post_selected = []
            if field in post_selectors: 
                post_selected = apply_post_selectors(elems, False, post_selectors[field])
            elif field in self.default_post_selectors:
                post_selected = apply_post_selectors(elems, False, self.default_post_selectors[field])
            else:
                post_selected = apply_post_selectors(elems, True)
            res[field] = post_selected
        
        res['outlet'] = self.domain_to_selectors[url_domain]['outlet_name']
        res = post_process(res)
        self.handle_warning(res)
        self.save_result(res)
            

    def handle_warning(self, res):
        try:
            def log_warning(outlet, url, warning, path=DEFAULT_WARNING_LOG_PATH):
                with open(path, '+a') as file:
                    outlet = outlet if ',' not in outlet else f'"{outlet}"'
                    newline = f"{outlet}, {url}, {warning}\n"
                    file.write(newline)
            outlet, url = res.get('outlet'), res.get('url')
            if not res.get('name'):
                log_warning(outlet, url, "did not get journalist name")
            if not res.get('articles'):
                log_warning(outlet, url, "did not get any articles")
            elif len(res.get('articles')) <= 1:
                log_warning(outlet, url, "got 1 or less article")
        except Exception as e:
            print(f'Encountered error while logging warning: {e}')


    def start_scraping(self):
        urls = self.get_urls_list()
        url_count = len(urls)
        counter = 1
        for url in urls:
            print(f"({counter}/{url_count}) ", end="")
            self.scrape_single_page(url)
            counter += 1
    

    def save_result(self, res):
        with open(self.save_path, '+a') as f:
            f.write(json.dumps(res, indent=4) + '\n')