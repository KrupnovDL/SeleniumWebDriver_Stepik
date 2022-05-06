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
    driver.get("http://SunInJuly.github.io/execute_script.html")
    x_element = driver.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    driver.find_element(By.ID, "answer").send_keys(y)
    driver.find_element(By.ID, "robotCheckbox").click()
    button = driver.find_element(By.TAG_NAME, "button")
    driver.execute_script("return arguments[0].scrollIntoView(true);", button)
    driver.find_element(By.ID, "robotsRule").click()
    button.click()
    time.sleep(5)
