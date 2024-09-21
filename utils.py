from selenium.webdriver import Chrome
from ui.pages.registration_page import Authentication
from configs import USERNAME, PASSWORD


def auth(browser):
    _auth = Authentication(
        browser=browser,
        username=USERNAME,
        password=PASSWORD
    )
    return _auth


def highlight(element, chrome_driver):
    chrome_driver = element._parent
    original_style = element.get_attribute('style')
    chrome_driver.execute_script("arguments[0].setAttribute(arguments[1], arguments[2])",
                                 element, "style", "border: 2px solid red; " + original_style)
    return original_style


def save_photo(element, chrome_driver: Chrome, test_name):
    highlight(element, chrome_driver)
    chrome_driver.save_screenshot(f'screenshots/{test_name}.png')