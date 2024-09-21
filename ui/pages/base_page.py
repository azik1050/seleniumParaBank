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

    def get_open_new_account_link(self):
        link = self.browser.find_element(By.LINK_TEXT, 'Open New Account')
        return link

    def get_accounts_overview_link(self):
        link = self.browser.find_element(By.LINK_TEXT, 'Accounts Overview')
        return link

    def get_transfer_funds_link(self):
        link = self.browser.find_element(By.LINK_TEXT, 'Transfer Funds')
        return link

    def get_bill_pay_link(self):
        link = self.browser.find_element(By.LINK_TEXT, 'Bill Pay')
        return link

    def get_find_transactions_link(self):
        link = self.browser.find_element(By.LINK_TEXT, 'Find Transactions')
        return link

    def get_update_contact_info_link(self):
        link = self.browser.find_element(By.LINK_TEXT, 'Update Contact Info')
        return link

    def get_request_loan_link(self):
        link = self.browser.find_element(By.LINK_TEXT, 'Request Loan')
        return link
