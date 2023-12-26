from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random

class PageSourceGetter:
    def __init__(self):
        options = Options()
        options.add_argument("--window-size=1280x720")
        # options.add_argument("--verbose")
        options.add_argument('--blink-settings=imagesEnabled=false')
        options.add_argument('--ignore-certificate-errors-spki-list')
        options.add_argument('--ignore-ssl-errors')
        # options.add_argument('--headless')
        # options.add_argument('--disable-gpu')
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--log-level=3")
        options.page_load_strategy = 'eager'  # or 'normal' or 'none'

        prefs={"profile.managed_default_content_settings.images": 2}
        options.add_experimental_option('prefs', prefs)
        
        self.driver = webdriver.Chrome(options=options)
        # network throttling.
        # self.driver.set_network_conditions(
        #     offline=False,
        #     latency=5,  # additional latency (ms)
        #     download_throughput=200 * 1024,  # maximal throughput
        #     upload_throughput=200 * 1024   # maximal throughput
        # )
        
        self.options = options
    
    def get_page_source(self, url : str) -> str:
        try:
            # self.driver.set_page_load_timeout(20)
            self.driver.get(url)
            time.sleep(random.uniform(0.6, 1.25))
            # input()
            return self.driver.page_source
        
        except Exception as e:
            self.driver.close()
            return e