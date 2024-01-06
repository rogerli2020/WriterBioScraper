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
            move_file = False
            domain = file_path.name
            with open(file_path, 'r', encoding='utf-8') as f:
                page_source = f.read()
                extracted_urls = crawler_manager.extract_urls(page_source, f"https://{domain}/")
                match_count = 0
                for url in extracted_urls:
                    if re.match(domain_url_regex[domain], url): 
                        match_count += 1
                        if url not in captured:
                            with open('./output/captured_urls.txt', '+a') as f:
                                f.write(url + '\n')
                            captured.add(url)
                if match_count < 10:
                    print(f'[WARNING] Only scraped {match_count} urls from {domain}')
                else:
                    move_file = True
                    print(f'Extracted {match_count} URLs from {domain}')
            if move_file:
                # move the file to archive folder.
                cur_file_path = Path.cwd() / f'input/local_html/{file_path.name}'
                dest_file_path = Path.cwd() / f'input/archived_local_html/{file_path.name}'
                os.replace(cur_file_path, dest_file_path)

capture_urls()