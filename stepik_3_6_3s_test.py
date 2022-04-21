import pytest
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


MAX_WAITING_TIME = 7


def calc():
    return math.log(int(time.time()))


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(MAX_WAITING_TIME)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link_number', ["895", "896", "897", "898", "899", "903", "904", "905"])
def test_parameterization(browser, link_number):
    browser.get(f"https://stepik.org/lesson/236{link_number}/step/1")
    input_field = browser.find_element(By.TAG_NAME, "textarea")
    input_field.send_keys(calc())
    button = WebDriverWait(browser, MAX_WAITING_TIME).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
    )
    button.click()
    assert browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text == "Correct!", "The answer isn't correct"
