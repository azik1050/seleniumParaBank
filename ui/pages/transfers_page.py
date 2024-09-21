from selenium import webdriver
from selenium.webdriver.common.by import By
from ui.locators.transfers_page_locators import transfers_page_locators as locators
from ui.pages.open_account_page import OpenAccountPage
from .base_page import BasePage


class TransferFundsPage(BasePage, OpenAccountPage):
    def __init__(self, browser: webdriver.Chrome):
        super().__init__(browser)

    def get_amount_field(self):
        field = self.browser.find_element(By.ID, locators['amount_field'])
        return field

    def get_from_account_field(self):
        field = self.browser.find_element(By.ID, locators['from_account_field'])
        return field

    def get_to_account_field(self):
        field = self.browser.find_element(By.ID, locators['to_account_field'])
        return field

    def get_transfer_button(self):
        button = self.browser.find_element(
            By.XPATH,
            f'//input[@class="button" and @value="{locators['transfer_button']}"]'
        )
        return button
