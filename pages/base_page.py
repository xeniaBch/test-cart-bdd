from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate_to(self, url):
        self.driver.get(url)

    def wait_for_element(self, by, locator):
        return self.wait.until(EC.visibility_of_element_located((by, locator)))