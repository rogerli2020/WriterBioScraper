from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, WebDriverException
import time
import random

class PageSourceGetter:
    def __init__(self, max_retries=4):
        options = Options()
        options.add_argument("--window-size=1280x720")
        options.add_argument('--blink-settings=imagesEnabled=false')
        options.add_argument('--ignore-certificate-errors-spki-list')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--log-level=3")
        options.add_argument("--disable-notifications")
        # options.add_argument('--headless')
        # options.add_argument('--disable-gpu')
        # options.add_argument("--verbose")
        # options.page_load_strategy = 'none'  # or 'normal' or 'none'
        # prefs={"profile.managed_default_content_settings.images": 2}
        # options.add_experimental_option('prefs', prefs)
        
        self.driver = webdriver.Chrome(options=options)
        self.options = options
        self.max_retries = max_retries

    def get_page_source(self, url: str, timeout: int=10, retries=0, reinstantiate_after=False) -> str:
        if retries >= self.max_retries: return ""
        if retries > 0: print(f'Retrying for the {retries} time...')
        self.driver.set_page_load_timeout(timeout)
        self.driver.implicitly_wait(timeout)
        try:
            self.driver.get(url)
            time.sleep(random.uniform(0.75, 1.25))
            page_source = self.driver.page_source
            if reinstantiate_after: self.reinstantiate_driver()
            return page_source
        except TimeoutException:
            print("[WARNING] A timeout exception happened...")
            self.reinstantiate_driver()
            self.get_page_source(url, timeout+5, retries+1)
        except Exception:
            print("[WARNING] An exception occured...")
            self.reinstantiate_driver()
            self.get_page_source(url, timeout, retries+1)
    
    def reinstantiate_driver(self):
        self.driver.quit()
        self.driver = webdriver.Chrome(options=self.options)