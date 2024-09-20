from confest import browser, base_page
from ui.pages.base_page import BasePage


def test_navigation_open_new_account(browser, base_page):
    base_page.get_open_new_account_link().click()
    assert base_page.get_accounts_overview_link().text == ''

