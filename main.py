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
    parser.add_argument('-scrape', '--scrape', dest='scrape', action='store_true', help='Start the scraping process given an input file of a list of URLs.')
    parser.add_argument('-crawl', '--crawl', dest='crawl', action='store_true', help='Start crawling for journalist URLs given an input file of URLs to start scraping from.')
    parser.add_argument('-adds', '--add-scraper', dest='add_scraper', action='store_true', help="Add CSS Selectors for different components of an outlet's journalist profile pages.")
    parser.add_argument('-extract', '--extract', dest='extract', action='store_true', help='Extract profile URLs of a local HTML given an outlet domain.')
    args = parser.parse_args()

    # start manual identification process if user wishes to do so.
    if args.add_scraper:
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

    
    # start scraping given URLs.
    bio_scraper = BioScraper(
            # url_input_path, 
            DEFAULT_INPUT_URLS_PATH,
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