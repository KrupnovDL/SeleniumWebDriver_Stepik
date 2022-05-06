import pytest
import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


MAX_WAITING_TIME = 7


def calc():
    return math.log(int(time.time()))


@pytest.mark.parametrize('link_number', ["895", "896", "897", "898", "899", "903", "904", "905"])
def test_parameterization(driver, link_number):
    driver.get(f"https://stepik.org/lesson/236{link_number}/step/1")
    input_field = driver.find_element(By.TAG_NAME, "textarea")
    input_field.send_keys(calc())
    button = WebDriverWait(driver, MAX_WAITING_TIME).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
    )
    button.click()
    assert driver.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text == "Correct!", "The answer isn't correct"
