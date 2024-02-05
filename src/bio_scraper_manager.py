"""
    Unfinished Code
"""

from src.bio_scraper import BioScraper
from urllib.parse import urlparse
from src.page_source_getter import PageSourceGetter
import threading

DEFAULT_INPUT_FILE_PATH = './input/scrape_urls.txt'
DEFAULT_SELECTORS_PATH = './assets/selectors.jsonl'

class URLsGroupByDomain:
    def __init__(self, domain):
        self.domain = domain
        self.skip = False
        self.urls = []
    
    def add_url(self, url):
        self.urls.append(url)
    
    def pop_url(self):
        if not self.is_empty():
            return self.urls.pop()
        return None
    
    def is_empty(self):
        return len(self.urls) <= 0
    
    def __hash__(self) -> int:
        return hash(self.domain)


class Worker:
    def __init__(self, id, write_lock) -> None:
        self.id = id
        self.write_lock = write_lock
        self.page_source_getter = PageSourceGetter()


class BioScraperManager:
    def __init__(self, 
                 execution_id, 
                 urls_path : str=DEFAULT_INPUT_FILE_PATH, 
                 thread_count : int=1
                 ) -> None:
        self.urls_path = urls_path
        self.num_threads = thread_count
        self.execution_id = execution_id
        self.group_by_domain = {}
        self.url_count = 0
        self.bio_scraper = BioScraper(self.urls_path, DEFAULT_SELECTORS_PATH, )
    
    def load_urls(self):
        urls = []
        print('Loading URLs...')
        with open(self.urls_path, 'r') as f:
            for url in f.readlines():
                url = url.replace('\n', '')
                if url: 
                    urls.append(url)
                    self.url_count += 1
        print('Grouping URLs based on domain...')
        for url in urls:
            domain = urlparse(url).netloc
            if domain not in self.group_by_domain():
                new_holder = URLsGroupByDomain(domain)
                new_holder.add_url(url)
                self.group_by_domain[domain] = new_holder
            else:
                self.group_by_domain[domain].add_url(url)
        print(f'{len(self.group_by_domain)} domains identified.')

    def start_multithreaded_scrape(self):
        pass