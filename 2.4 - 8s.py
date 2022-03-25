from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import pyperclip
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def calc(number):
    return str(math.log(abs(12 * math.sin(int(number)))))


with webdriver.Chrome() as browser:
    browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(browser, 12).until(ec.text_to_be_present_in_element((By.ID, "price"), "100"))
    browser.find_element(By.ID, "book").click()
    input_for_answer = browser.find_element(By.ID, "answer")
    answer = calc(browser.find_element(By.ID, "input_value").text)
    input_for_answer.send_keys(answer)
    browser.find_element(By.ID, "solve").click()
    alert = browser.switch_to.alert
    pyperclip.copy(browser.switch_to.alert.text.split(': ')[-1])
