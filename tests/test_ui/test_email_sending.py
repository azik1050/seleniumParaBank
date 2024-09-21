from time import sleep
from confest import customer_care_page, browser
from utils import save_photo
from configs import USERNAME
import pytest


@pytest.mark.flaky(reruns=3)
def test_email_sending(customer_care_page, browser):
    customer_care_page.get_email_link().click()

    customer_care_page.get_name_field().send_keys(f'{USERNAME}')
    customer_care_page.get_email_field().send_keys('A')
    customer_care_page.get_phone_field().send_keys('A')
    customer_care_page.get_message_field().send_keys('A')

    customer_care_page.get_customer_care_button().click()
    sleep(2)
    save_photo(customer_care_page.get_right_panel(), browser, 'EmailSending')

    assert customer_care_page.get_right_panel_p()[2].text == f'Thank you {USERNAME}'
    assert customer_care_page.get_right_panel_p()[3].text == 'A Customer Care Representative will be contacting you.'

