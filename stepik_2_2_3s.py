from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

s = Service(ChromeDriverManager().install())
with webdriver.Chrome(service=s) as driver:
    driver.get("http://suninjuly.github.io/selects1.html")
    num1 = int(driver.find_element(By.ID, "num1").text)
    num2 = int(driver.find_element(By.ID, "num2").text)
    Select(driver.find_element(By.CSS_SELECTOR, ".custom-select")).select_by_value(str(num1 + num2))
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
    time.sleep(5)
