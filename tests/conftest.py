import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='session')
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36)")
    # chrome_options.add_argument("--headless")  # режим без визуальной загрузки браузера
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_experimental_option('prefs', {
        'download.default_directory' : os.getcwd() + '\\tests',
        "download.prompt_for_download": False,
        "safebrowsing.enabled": True
    })

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
