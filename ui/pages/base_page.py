from selenium import webdriver
from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import base_page_locators


class BasePage:
    def __init__(self, browser: webdriver.Chrome):
        self.browser = browser

    def get_right_panel(self):
        panel = self.browser.find_element(By.ID, base_page_locators['right_panel']['block'])
        return panel

    def get_right_panel_header(self):
        header = self.browser.find_element(By.CLASS_NAME, base_page_locators['right_panel']['header'])
        return header
