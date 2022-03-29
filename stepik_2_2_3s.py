from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/selects1.html")
    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)
    Select(browser.find_element(By.CSS_SELECTOR, ".custom-select")).select_by_value(str(num1 + num2))
    browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
    time.sleep(5)
