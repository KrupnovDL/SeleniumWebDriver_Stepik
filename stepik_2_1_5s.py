from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


s = Service(ChromeDriverManager().install())
with webdriver.Chrome(service=s) as driver:
    driver.get("http://suninjuly.github.io/math.html")
    x_element = driver.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    driver.find_element(By.ID, "answer").send_keys(y)
    driver.find_element(By.ID, "robotCheckbox").click()
    driver.find_element(By.ID, "robotsRule").click()
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
    time.sleep(5)
