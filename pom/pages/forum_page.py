from selenium.webdriver.chrome.webdriver import WebDriver
from pom.pages.locators import forum_page_locator as loc


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get('https://dekarlab.de/wp/?post_type=forum')

    def find_element(self, *args):
        by_name, by_val = args[0]
        return self.driver.find_element(by_name, by_val)

    def find_elements(self, *args):
        by_name, by_val = args[0]
        return self.driver.find_element(by_name, by_val)