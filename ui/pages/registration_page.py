from .base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from ui.locators.registration_page_locators import registration_page_locators
from selenium.common.exceptions import NoSuchElementException


class RegistrationPage:
    def __init__(self, browser: webdriver.Chrome):
        self.browser = browser

    def _get_first_name_field(self):
        field = self.browser.find_element(By.ID, registration_page_locators['registration_form']['first_name'])
        return field

    def _get_last_name_field(self):
        field = self.browser.find_element(By.ID, registration_page_locators['registration_form']['last_name'])
        return field

    def _get_address_field(self):
        field = self.browser.find_element(By.ID, registration_page_locators['registration_form']['address'])
        return field

    def _get_city_field(self):
        field = self.browser.find_element(By.ID, registration_page_locators['registration_form']['city'])
        return field

    def _get_state_field(self):
        field = self.browser.find_element(By.ID, registration_page_locators['registration_form']['state'])
        return field

    def _get_zip_code_field(self):
        field = self.browser.find_element(By.ID, registration_page_locators['registration_form']['zip_code'])
        return field

    def _get_phone_field(self):
        field = self.browser.find_element(By.ID, registration_page_locators['registration_form']['phone'])
        return field

    def _get_ssn_field(self):
        field = self.browser.find_element(By.ID, registration_page_locators['registration_form']['ssn'])
        return field

    def _get_username_field(self):
        field = self.browser.find_element(By.ID, registration_page_locators['registration_form']['username'])
        return field

    def _get_password_field(self):
        field = self.browser.find_element(By.ID, registration_page_locators['registration_form']['password'])
        return field

    def _get_confirm_password_field(self):
        field = self.browser.find_element(By.ID, registration_page_locators['registration_form']['confirm_password'])
        return field

    def _get_registration_button(self):
        button = self.browser.find_element(
            By.XPATH,
            f'//input[@type="submit" and @value="{registration_page_locators['registration_button']}"]',
        )
        return button

    def _get_login_username_field(self):
        field = self.browser.find_element(By.NAME, registration_page_locators['login_form']['username'])
        return field

    def _get_login_password_field(self):
        field = self.browser.find_element(By.NAME, registration_page_locators['login_form']['password'])
        return field

    def _get_login_button(self):
        button = self.browser.find_element(
            By.XPATH,
            f'//input[@type="submit" and @value="{registration_page_locators['login_button']}"]'
        )
        return button


class Authentication(RegistrationPage, BasePage):
    registered = False

    def __init__(self, browser, username, password):
        super().__init__(browser)
        self.username = username
        self.password = password

    def _fill_registration_form(self):
        self._get_first_name_field().send_keys('A')
        assert self._get_first_name_field().get_attribute(
            'value') == 'A', "First name field did not match expected value."

        self._get_last_name_field().send_keys('Smith')
        assert self._get_last_name_field().get_attribute(
            'value') == 'Smith', "Last name field did not match expected value."

        self._get_address_field().send_keys('123 Main St')
        assert self._get_address_field().get_attribute(
            'value') == '123 Main St', "Address field did not match expected value."

        self._get_city_field().send_keys('Anytown')
        assert self._get_city_field().get_attribute('value') == 'Anytown', "City field did not match expected value."

        self._get_state_field().send_keys('CA')
        assert self._get_state_field().get_attribute('value') == 'CA', "State field did not match expected value."

        self._get_zip_code_field().send_keys('90210')
        assert self._get_zip_code_field().get_attribute(
            'value') == '90210', "Zip code field did not match expected value."

        self._get_phone_field().send_keys('123-456-7890')
        assert self._get_phone_field().get_attribute(
            'value') == '123-456-7890', "Phone field did not match expected value."

        self._get_ssn_field().send_keys('123-45-6789')
        assert self._get_ssn_field().get_attribute('value') == '123-45-6789', "SSN field did not match expected value."

        self._get_username_field().send_keys(self.username)
        assert self._get_username_field().get_attribute(
            'value') == self.username, "Username field did not match expected value."

        self._get_password_field().send_keys(self.password)
        assert self._get_password_field().get_attribute(
            'value') == self.password, "Password field did not match expected value."

        self._get_confirm_password_field().send_keys(self.password)
        assert self._get_confirm_password_field().get_attribute(
            'value') == self.password, "Confirm password field did not match expected value."

    def _fill_login_form(self):
        self._get_login_username_field().send_keys(self.username)
        assert self._get_login_username_field().get_attribute(
            'value') == self.username, "Username field did not match expected value."

        self._get_login_password_field().send_keys(self.password)
        assert self._get_login_password_field().get_attribute(
            'value') == self.password, "Password field did not match expected value."

    def register(self):
        self._fill_registration_form()
        self._get_registration_button().click()
        try:
            if self.get_right_panel_header().text == f'Welcome {self.get_right_panel_header()}':
                self.registered = True
        except NoSuchElementException:
            return

    def login(self):
        self._fill_login_form()
        self._get_login_button().click()

    def authenticate(self):
        self.register()
        if not self.registered:
            self.login()

