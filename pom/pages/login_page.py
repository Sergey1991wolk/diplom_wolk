from selenium.webdriver.chrome.webdriver import WebDriver
from pom.pages.locators import login_page_locator as loc


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get('https://dekarlab.de/wp/wp-admin')

    def find_element(self, *args):
        by_name, by_val = args[0]
        return self.driver.find_element(by_name, by_val)

    def find_elements(self, *args):
        by_name, by_val = args[0]
        return self.driver.find_element(by_name, by_val)

    def user_name_field(self):
        return self.find_element(loc.user_name_field)

    def user_password_field(self):
        return self.find_element(loc.user_password_field)

    def remember_me_field(self):
        return self.find_element(loc.remember_me)

    def login_button(self):
        return self.find_element(loc.login_button)

    def wrong_login_message(self):
        return self.find_element(loc.wrong_login_message)
