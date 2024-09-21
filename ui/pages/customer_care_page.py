from selenium import webdriver
from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage
from ui.locators.customer_care_page_locators import customer_care_page_locators as locators


class CustomerCarePage(BasePage):
    def __init__(self, browser: webdriver.Chrome):
        super().__init__(browser)

    def get_name_field(self):
        field = self.browser.find_element(By.ID, locators['name_field'])
        return field

    def get_email_field(self):
        field = self.browser.find_element(By.ID, locators['email_field'])
        return field

    def get_phone_field(self):
        field = self.browser.find_element(By.ID, locators['phone_field'])
        return field

    def get_message_field(self):
        field = self.browser.find_element(By.ID, locators['message_field'])
        return field

    def get_customer_care_button(self):
        button = self.browser.find_element(
            By.XPATH,
            f'//input[@type="submit" and @value="{locators['send_button']}"]'
        )
        return button
