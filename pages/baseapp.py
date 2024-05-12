from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))
