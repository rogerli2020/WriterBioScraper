import time
from src.page_source_getter import PageSourceGetter
from journalists_crawler.crawler_tree import CrawlerTree
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin, urlunparse
from assets.domain_profile_url_regex import domain_url_regex

class CrawlerManager:
    def __init__(self, verbose, root_urls_path : str, domain_regex_path : str, crawl_output : str, desired_time_gap=8) -> None:
        self.verbose = verbose
        self.crawl_output = crawl_output
        self.page_source_getter = PageSourceGetter()
        self.crawlers : list[CrawlerTree] = []
        self.stop = False
        self.root_urls = []
        self.root_urls_path = root_urls_path
        self.domain_to_regex = domain_url_regex
        self.desired_time_gap = desired_time_gap
        self._load_data(root_urls_path, domain_regex_path)

    def _load_data(self, root_urls_path, domain_regex_path):

        # load root urls to visit.
        print('CrawlerManager: Loading URLs from local file...')
        with open(root_urls_path, 'r') as f:
            for url in f.readlines():
                url = url.replace('\n', '')
                if not urlparse(url).scheme:
                    url = 'https://' + url
                if not urlparse(url).path.endswith('/'):
                    url += '/'
                print(url)
                if url: self.root_urls.append(url)
        
        # load regex
        # print('CrawlerManager: Loading Regex dictionary from local file...')
        # with open(domain_regex_path, 'r') as f:
        #     self.domain_to_regex = json.load(f)
        
        # for each root url, create a crawler and add to list.
        print('CrawlerManager: Creating and adding CrawlerTree objects...')
        for url in self.root_urls:
            self.create_and_add_crawler(url)
        
        print(f'CrawlerManager: Loaded! {len(self.crawlers)} CrawlerTree objects to process.')


    def extract_urls(self, page_source, root_url):
        def remove_query_strings(url):
            parsed_url = urlparse(url)
            cleaned_url = urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, '', '', ''))
            return cleaned_url
        root_domain = urlparse(root_url).netloc
        if not page_source: 
            print(f'Warning: no page source passed in for {root_url}')
            return []
        soup = BeautifulSoup(page_source, 'html.parser')
        all_links = soup.find_all('a', href=True)
        same_domain_links = [link['href'] for link in all_links if urlparse(urljoin(root_url, link['href'])).netloc == root_domain]
        same_domain_links = [urljoin(root_url, link) for link in same_domain_links]
        same_domain_links = [remove_query_strings(url) for url in same_domain_links]
        return same_domain_links


    def start_crawling(self):
        """
        Visit one website from each individual "crawler"
        at each iteration.
        """
        iteration = 0
        while not self.stop:
            n_unfinished_crawlers = 0
            for crawler in self.crawlers:
                if not crawler.finished:
                    n_unfinished_crawlers += 1
            time_gap = self.desired_time_gap / n_unfinished_crawlers
            print(f'Performing new crawl iteration: {iteration}... Time Gap {time_gap}')
            if not self.crawlers:
                print(f'CrawlManager: No CrawlerTree objects to process. Aborting...')
                return
            for crawler in self.crawlers:
                if crawler.finished: continue
                node = crawler.get_next_node()
                if not node:
                    print('No more Nodes to process.')
                    crawler.finished = True
                    continue
                url = node.data

                # workaround for selenium error
                all_good = False
                while not all_good:
                    try:
                        page_source = self.page_source_getter.get_page_source(url)
                        all_good = True
                    except Exception as e:
                        print(e)
                        print('Random ass error happened again. Retrying...')
                        self.page_source_getter.driver.quit()
                        self.page_source_getter = PageSourceGetter()

                child_urls = self.extract_urls(page_source, crawler.root_url)
                crawler.generate_and_add_child_nodes(node, child_urls)
                time.sleep(time_gap)
            all_done = True
            for crawler in self.crawlers:
                if not crawler.finished: all_done = False
            if all_done: self.stop = True
            iteration += 1
        print('Crawling finished.')
    

    def create_and_add_crawler(self, root_url):
        profile_url_regex = self.domain_to_regex.get(urlparse(root_url).netloc)
        if not profile_url_regex:
            print(f'Could not find corresponding regex for {root_url}. Skipping...')
            return
        new_crawler_tree = CrawlerTree('TESTING', root_url, profile_url_regex)
        self.crawlers.append(new_crawler_tree)


    def stop_crawling(self):
        print('Crawling will stop shortly...')
        self.stop = True