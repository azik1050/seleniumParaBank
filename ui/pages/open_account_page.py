from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from ui.locators.open_account_page_locators import open_account_page_locators as locators


class OpenAccountPage:
    def __init__(self, browser: Chrome):
        self.browser = browser

    def get_open_account_button(self):
        button = self.browser.find_element(
            By.XPATH,
            f'//input[@type="button" and @value="{locators['open_account_button']}"]'
        )
        return button

    def get_account_field(self):
        field = self.browser.find_element(By.ID, locators['account_field'])
        return field
