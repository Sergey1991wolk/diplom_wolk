from selenium import webdriver
import os
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='function')
def driver():
    print(os.environ['PATH'])

    return init_driver()

def init_driver():
    Service(executable_path='chromedriver.exe')
    options = Options()
    options.add_argument('start-maximized')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver
