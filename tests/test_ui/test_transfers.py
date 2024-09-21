import pytest
from confest import transfers_page, base_page, browser
from selenium.webdriver.support.ui import Select
from time import sleep
from utils import save_photo


def open_new_account(browser, transfers_page):
    transfers_page.get_open_new_account_link().click()
    sleep(5)
    assert transfers_page.get_open_account_button().get_property('value') == 'Open New Account'
    account = Select(transfers_page.get_account_field())
    account.select_by_visible_text(account.first_selected_option.text)

    transfers_page.get_open_account_button().is_displayed()
    transfers_page.get_open_account_button().click()
    sleep(2)
    save_photo(transfers_page.get_right_panel(), browser, 'OpenAccount')


@pytest.mark.flaky(reruns=3)
@pytest.mark.positive
def test_correct_transfer(browser, transfers_page, base_page):
    open_new_account(browser, transfers_page)

    transfers_page.get_transfer_funds_link().click()
    transfers_page.get_amount_field().send_keys('100')

    sleep(5)
    from_account = Select(transfers_page.get_from_account_field())
    from_account.select_by_visible_text(from_account.first_selected_option.text)
    print(f'From {from_account.options[0].text}')
    sleep(2)
    to_account = Select(transfers_page.get_to_account_field())
    to_account.select_by_index(1)
    print(f'To {to_account.options[1].text}')
    sleep(5)

    transfers_page.get_transfer_button().click()
    sleep(2)
    save_photo(transfers_page.get_right_panel(), browser, 'CorrectTransfer')


@pytest.mark.flaky(reruns=3)
@pytest.mark.negative
def test_incorrect_transfer(browser, transfers_page, base_page):
    open_new_account(browser, transfers_page)

    transfers_page.get_transfer_funds_link().click()
    transfers_page.get_amount_field().send_keys('100')

    sleep(5)
    from_account = Select(transfers_page.get_from_account_field())
    from_account.select_by_visible_text(from_account.first_selected_option.text)
    print(f'From {from_account.options[0].text}')
    sleep(2)
    to_account = Select(transfers_page.get_to_account_field())
    to_account.select_by_index(0)
    print(f'To {to_account.options[0].text}')
    sleep(5)

    transfers_page.get_transfer_button().click()
    sleep(2)
    save_photo(transfers_page.get_right_panel(), browser, 'IncorrectTransfer')
