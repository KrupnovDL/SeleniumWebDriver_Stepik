from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import math
import pyperclip


def calc(number):
    return str(math.log(abs(12 * math.sin(int(number)))))


s = Service(ChromeDriverManager().install())
with webdriver.Chrome(service=s) as driver:
    driver.implicitly_wait(5)
    driver.get(" http://suninjuly.github.io/redirect_accept.html")
    driver.find_element(By.TAG_NAME, "button").click()
    driver.switch_to.window(driver.window_handles[1])
    input_for_answer = driver.find_element(By.ID, "answer")
    answer = calc(driver.find_element(By.ID, "input_value").text)
    input_for_answer.send_keys(answer)
    driver.find_element(By.TAG_NAME, "button").click()
    alert = driver.switch_to.alert
    pyperclip.copy(driver.switch_to.alert.text.split(': ')[-1])
