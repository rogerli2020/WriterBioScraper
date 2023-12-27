from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, WebDriverException
import time
import random

class PageSourceGetter:
    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        # options.add_argument('--disable-gpu')
        # options.add_argument("--verbose")
        options.add_argument("--window-size=1280x720")
        options.add_argument('--blink-settings=imagesEnabled=false')
        options.add_argument('--ignore-certificate-errors-spki-list')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument("--disable-blink-features=AutomationControlled")
        # options.add_argument("--log-level=3")
        options.add_argument("--disable-notifications")
        # options.page_load_strategy = 'none'  # or 'normal' or 'none'

        # prefs={"profile.managed_default_content_settings.images": 2}
        # options.add_experimental_option('prefs', prefs)
        
        self.driver = webdriver.Chrome(options=options)
        
        self.options = options

    def get_page_source(self, url: str, timeout: int = 10) -> str:

        # try:

        # self.driver.set_script_timeout(timeout)
        self.driver.set_page_load_timeout(timeout)
        self.driver.get(url)
        
        # element_present = EC.presence_of_element_located((By.TAG_NAME, 'html'))
        # WebDriverWait(self.driver, timeout).until(element_present)
        
        time.sleep(random.uniform(0.3, 0.5))
        return self.driver.page_source  
    
        # except Exception as e:
        #     # print(f"An error occurred: {e}")
        #     print("A Selenium error occured...")
        #     self.driver.close()
        #     return ""