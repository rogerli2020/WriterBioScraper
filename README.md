# WritersBioScraper

## Overview
This program has several functionalities related to obtaining journalists information, including:
  - Scraping for information of a journalist given their profile URL.
  - Crawling for journalist URLs given a starting URL.
  - Adding Regex for news outlet profile page URLs.
  - Manually adding scraper information for outlets.
  - Extract journalist URLs from local files.
  - Create local files for journalist URLs extraction.

## Setup
Set up Python virtual environment and install dependencies listed under `requirements.txt`.

## Usage and Options
Listed below are the primary functionalities of this application.
  1. ### `scrape`
     - Start the scraping process given an input file of a list of URLs.
  2. ### `crawl`
     - Start crawling for journalist URLs given an input file of URLs to start scraping from.
  3. ### `addr` (Add Regex)
     - Add regex expression for an outlet's profile URLs.
  4. ### `adds` (Add Scraper)
     - Add CSS Selectors for different components of an outlet's journalist profile pages.
  5. ### `extract`
      - Extract profile URLs of an HTML given an outlet domain.

    

## TODO
