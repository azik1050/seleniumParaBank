from ui.pages.registration_page import Authentication
from configs import USERNAME, PASSWORD


def auth(browser):
    _auth = Authentication(
        browser=browser,
        username=USERNAME,
        password=PASSWORD
    )
    return _auth
