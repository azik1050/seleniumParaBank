from selenium import webdriver
import pytest


@pytest.fixture()
def browser():
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
    chrome_driver.quit()

