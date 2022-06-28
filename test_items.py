from selenium.webdriver.common.by import By
import time


def test_check_button_add_to_basket(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(5)
    assert browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
