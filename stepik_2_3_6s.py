from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import pyperclip


def calc(number):
    return str(math.log(abs(12 * math.sin(int(number)))))


with webdriver.Chrome() as browser:
    browser.implicitly_wait(5)
    browser.get(" http://suninjuly.github.io/redirect_accept.html")
    browser.find_element(By.TAG_NAME, "button").click()
    browser.switch_to.window(browser.window_handles[1])
    input_for_answer = browser.find_element(By.ID, "answer")
    answer = calc(browser.find_element(By.ID, "input_value").text)
    input_for_answer.send_keys(answer)
    browser.find_element(By.TAG_NAME, "button").click()
    alert = browser.switch_to.alert
    pyperclip.copy(browser.switch_to.alert.text.split(': ')[-1])
