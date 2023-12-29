import os
import argparse
import sys
import time
from src.manual_identifier import ManualIdentifier
from src.bio_scraper import BioScraper
from journalists_crawler.crawler_manager import CrawlerManager

MANUAL_IDENTIFICATION_OUTPUT_PATH = './assets/selectors.jsonl'
DEFAULT_INPUT_URLS_PATH = './assets/input_urls.txt'
DEFAULT_SELECTORS_PATH = './assets/selectors.jsonl'
DEFAULT_SCRAPE_SAVE_PATH = './output/output.jsonl'
DEFAULT_CRAWL_ROOT_URLS_PATH = './assets/root_urls_for_crawling.txt'
DEFAULT_CRAWL_DOMAIN_REGEX_PATH = './assets/domain_profile_url_regex.json'
DEFAULT_CRAWL_OUTPUT = './output/crawl_results.txt'

if __name__ == '__main__':

    print(f'Current PID: {os.getpid()}')

    # start measuring the time taken to finish entire process.
    start_time = time.time()

    # handle command line arguments.
    parser = argparse.ArgumentParser(prog='WritersBioScraper', description='WritersBioScraper.', )
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', help='Verbose mode')
    parser.add_argument('-m', '--manual-identification', dest='manual_identification', action='store_true', help='Start manual identification')
    parser.add_argument('-c', '--crawl-for-profile-urls', dest='crawl_for_profile_urls', action='store_true', help='Start crawling for URLs for writer profiles.')
    parser.add_argument('-i', '--url-input-path', dest='url_input_path', type=str, help='Specify the input path of journalists URLs')
    parser.add_argument('-s', '--shuffle', dest='shuffle', action='store_true', help='Shuffle the list while scraping')
    parser.add_argument('-np', '--number-of-processes', dest='np', default=1, type=int, help='Specify the number of child processes you want to utilize')
    parser.add_argument('-auto', '--auto', dest='auto_mode', action='store_true', help='Automatic mode')
    args = parser.parse_args()

    # apply cmd line arguments.
    url_input_path = DEFAULT_INPUT_URLS_PATH if not args.url_input_path else args.url_input_path

    # start manual identification process if user wishes to do so.
    if args.manual_identification:
        manual_identifier = ManualIdentifier(MANUAL_IDENTIFICATION_OUTPUT_PATH)
        manual_identifier.start()
        sys.exit(0)

    # start the crawling process if user wishes to do so.
    if args.crawl_for_profile_urls:
        crawler_manager = CrawlerManager(
            False, 
            DEFAULT_CRAWL_ROOT_URLS_PATH, 
            DEFAULT_CRAWL_DOMAIN_REGEX_PATH, 
            DEFAULT_CRAWL_OUTPUT
            )
        crawler_manager.start_crawling()
        sys.exit(0)

    # start auto mode if the user wishes to do so.
    if args.auto_mode:
        print('Starting automatic URL Crawling and Bio Scraping process...')
        sys.exit(0)
    
    # start scraping given URLs.
    bio_scraper = BioScraper(
            url_input_path, 
            DEFAULT_SELECTORS_PATH, 
            DEFAULT_SCRAPE_SAVE_PATH,
            shuffle=args.shuffle,
        )
    bio_scraper.start_scraping()

    # finishing up.
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'''Done! Total runtime: {elapsed_time}''')
    sys.exit(0)