import os
import re
from pathlib import Path
from journalists_crawler.crawler_manager import CrawlerManager
from assets.domain_profile_url_regex import domain_url_regex


def capture_urls():
    crawler_manager = CrawlerManager(
        False, 
        './assets/root_urls_for_crawling.txt',
        './assets/domain_profile_url_regex.py',
        './output/captured_urls.txt'
        )
    
    captured = set()

    directory_path = Path.cwd()
    directory_path = directory_path / 'input/local_html'
    for file_path in directory_path.rglob("*"):
        if file_path.is_file():
            domain = file_path.name
            with open(file_path, 'r', encoding='utf-8') as f:
                page_source = f.read()
                extracted_urls = crawler_manager.extract_urls(page_source, f"https://{domain}/")
                print(extracted_urls)
                for url in extracted_urls:
                    print(url)
                    if re.match(domain_url_regex[domain], url): 
                        if url not in captured:
                            with open('./output/captured_urls.txt', '+a') as f:
                                print('Saving a valid url...')
                                f.write(url + '\n')
                            captured.add(url)

capture_urls()