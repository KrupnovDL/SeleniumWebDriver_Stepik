from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import math
import pyperclip
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def calc(number):
    return str(math.log(abs(12 * math.sin(int(number)))))


s = Service(ChromeDriverManager().install())
with webdriver.Chrome(service=s) as driver:
    driver.implicitly_wait(5)
    driver.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(driver, 12).until(ec.text_to_be_present_in_element((By.ID, "price"), "100"))
    driver.find_element(By.ID, "book").click()
    input_for_answer = driver.find_element(By.ID, "answer")
    answer = calc(driver.find_element(By.ID, "input_value").text)
    input_for_answer.send_keys(answer)
    driver.find_element(By.ID, "solve").click()
    alert = driver.switch_to.alert
    pyperclip.copy(driver.switch_to.alert.text.split(': ')[-1])
