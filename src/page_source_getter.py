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
        options.add_argument("--window-size=1280x720")
        # options.add_argument("--verbose")
        options.add_argument('--blink-settings=imagesEnabled=false')
        options.add_argument('--ignore-certificate-errors-spki-list')
        options.add_argument('--ignore-ssl-errors')
        # options.add_argument('--headless')
        # options.add_argument('--disable-gpu')
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--log-level=3")
        options.add_argument("--disable-notifications")
        options.page_load_strategy = 'none'  # or 'normal' or 'none'

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
    
    # def get_page_source(self, url : str) -> str:
    #     try:
    #         self.driver.get(url)
    #         time.sleep(random.uniform(0.6, 1.25))
    #         return self.driver.page_source
        
    #     except Exception as e:
    #         self.driver.close()
    #         return ""

    def get_page_source(self, url: str, timeout: int = 10) -> str:
        try:
            self.driver.get(url)
            
            # Use WebDriverWait to wait for the page to load
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, "//body"))
            )
            
            time.sleep(random.uniform(0.15, 0.3))
            return self.driver.page_source  
        # except TimeoutException:
        #     print(f"Timed out waiting for {url} to load")
        except Exception as e:
            print(f"An error occurred: {e}")
            self.driver.close()
            return ""