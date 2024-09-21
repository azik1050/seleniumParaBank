from confest import browser, base_page
from utils import save_photo
import pytest


@pytest.mark.flaky(reruns=3)
def test_navigation_open_new_account(browser, base_page):
    base_page.get_open_new_account_link().click()
    assert base_page.get_right_panel_header().text == 'Open New Account'
    save_photo(base_page.get_right_panel(), browser, 'OpenNewAccount')


@pytest.mark.flaky(reruns=3)
def test_navigation_accounts_overview(browser, base_page):
    base_page.get_accounts_overview_link().click()
    assert base_page.get_right_panel_header().text == 'Accounts Overview'
    save_photo(base_page.get_right_panel(), browser, 'AccountsOverview')


@pytest.mark.flaky(reruns=3)
def test_navigation_transfer_funds(browser, base_page):
    base_page.get_transfer_funds_link().click()
    assert base_page.get_right_panel_header().text == 'Transfer Funds'
    save_photo(base_page.get_right_panel(), browser, 'TransferFunds')


@pytest.mark.flaky(reruns=3)
def test_navigation_bill_pay(browser, base_page):
    base_page.get_bill_pay_link().click()
    assert base_page.get_right_panel_header().text == 'Bill Payment Service'
    save_photo(base_page.get_right_panel(), browser, 'BillPaymentService')


@pytest.mark.flaky(reruns=3)
def test_navigation_find_transactions(browser, base_page):
    base_page.get_find_transactions_link().click()
    assert base_page.get_right_panel_header().text == 'Find Transactions'
    save_photo(base_page.get_right_panel(), browser, 'FindTransactions')


@pytest.mark.flaky(reruns=3)
def test_navigation_update_contact_info(browser, base_page):
    base_page.get_update_contact_info_link().click()
    assert base_page.get_right_panel_header().text == 'Update Profile'
    save_photo(base_page.get_right_panel(), browser, 'UpdateProfile')


@pytest.mark.flaky(reruns=3)
def test_navigation_request_loan(browser, base_page):
    base_page.get_request_loan_link().click()
    assert base_page.get_right_panel_header().text == 'Apply for a Loan'
    save_photo(base_page.get_right_panel(), browser, 'ApplyforaLoan')
