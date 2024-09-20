from selenium import webdriver
from configs import UI_BASE_URL
from utils import auth
import pytest


@pytest.fixture()
def browser():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(UI_BASE_URL)
    auth(chrome_driver).authenticate()
    yield chrome_driver
    chrome_driver.quit()


