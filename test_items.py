from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
# import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_is_add_to_cart_button_visible(browser):
    browser.get(link)
    # time.sleep(30)
    try:
        button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    except NoSuchElementException:
        button = False
    assert button, "'Add to cart' button isn't visible"
