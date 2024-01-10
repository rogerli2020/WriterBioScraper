from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import urllib.parse
import time
import random
from urllib.parse import urlparse

driver = webdriver.Chrome()

def is_page_scrollable():
    current_scroll_position = driver.execute_script("return window.scrollY;")
    max_scroll_height = driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")
    return current_scroll_position < max_scroll_height

def get_page_source(url):
    element_locator = (By.CSS_SELECTOR, '.T7sFge.sW9g3e.VknLRd')

    driver.get(url)

    time.sleep(0.5)
    WebDriverWait(driver, 9999).until(EC.invisibility_of_element_located((By.ID, 'captcha-form')))
    print('CAPTCHA finished (if there was one).')

    for _ in range(0, 7):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(random.uniform(1,1.5))

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print("Trying to click...")
        element_to_click = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(element_locator))
        try:
            element_to_click.click()
        except:
            return driver.page_source
        time.sleep(random.uniform(1,1.5))


def get_url(search_query : str):
    url = 'https://www.google.com/search?q=' + urllib.parse.quote(search_query)
    return url


def get_query_and_url(line : str):
    line = line.replace('\n', '')
    query = 'site:' + line
    return query, line


with open('./input_info.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        # query, url = line.split(' ')
        query, url = get_query_and_url(line)
        print(f'Processing query: {query}...')
        domain = urlparse(url).netloc
        google_search_page_src = get_page_source(get_url(query))
        soup = BeautifulSoup(google_search_page_src, 'html.parser')
        elem = soup.find('div', id='botstuff')
        with open(f'./input/local_html/{domain}', 'w', encoding='utf-8') as file:
            file.write(str(elem))
        print('Waiting...')
        time.sleep(random.uniform(5,10))