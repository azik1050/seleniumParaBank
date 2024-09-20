from selenium import webdriver
from selenium.webdriver.common.by import By
from ui.locators.base_page_locators import base_page_locators


class BasePage:

    def __init__(self, browser: webdriver.Chrome):
        self.browser = browser
        self.links = browser.find_elements(By.TAG_NAME, 'a')

    def get_right_panel(self):
        panel = self.browser.find_element(By.ID, base_page_locators['right_panel']['block'])
        return panel

    def get_right_panel_header(self):
        header = self.browser.find_element(By.CLASS_NAME, base_page_locators['right_panel']['header'])
        return header

    def get_open_new_account_link(self):
        return self.links[0]

    def get_accounts_overview_link(self):
        return self.links[1]

    def get_transfer_funds_link(self):
        return self.links[2]

    def get_bill_pay_link(self):
        return self.links[3]

    def get_find_transactions_link(self):
        return self.links[4]

    def get_update_contact_info_link(self):
        return self.links[5]

    def get_request_loan_link(self):
        return self.links[6]
