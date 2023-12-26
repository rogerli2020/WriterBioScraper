import argparse
import sys
import time
from src.manual_identifier import ManualIdentifier
from src.bio_scraper import BioScraper

MANUAL_IDENTIFICATION_OUTPUT_PATH = './output/manual_identification.jsonl'
DEFAULT_INPUT_URLS_PATH = './assets/input_urls.txt'
DEFAULT_SELECTORS_PATH = './output/manual_identification.jsonl'
DEFAULT_SCRAPE_SAVE_PATH = './output/output.jsonl'

if __name__ == '__main__':

    # start measuring the time taken to finish entire process.
    start_time = time.time()

    # handle command line arguments.
    parser = argparse.ArgumentParser(prog='WritersBioScraper', description='WritersBioScraper.', )
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', help='Verbose mode')
    parser.add_argument('-m', '--manual-identification', dest='manual_identification', action='store_true', help='Start manual identification')
    parser.add_argument('-i', '--url-input-path', dest='url_input_path', type=str, help='Specify the input path of journalists URLs')
    parser.add_argument('-np', '--number-of-processes', dest='np', default=1, type=int, help='Specify the number of child processes you want to utilize')
    args = parser.parse_args()

    # apply cmd line arguments.
    url_input_path = DEFAULT_INPUT_URLS_PATH if not args.url_input_path else args.url_input_path

    # start manual identification process if user wishes to do so.
    if args.manual_identification:
        manual_identifier = ManualIdentifier(MANUAL_IDENTIFICATION_OUTPUT_PATH)
        manual_identifier.start()
        sys.exit(0)
    
    # start scraping given URLs.
    bio_scraper = BioScraper(
        DEFAULT_INPUT_URLS_PATH, 
        DEFAULT_SELECTORS_PATH, 
        DEFAULT_SCRAPE_SAVE_PATH
        )
    bio_scraper.start_scraping()

    # finishing up.
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'''Done! Total runtime: {elapsed_time}''')
    sys.exit(0)