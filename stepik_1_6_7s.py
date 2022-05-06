from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

s = Service(ChromeDriverManager().install())
with webdriver.Chrome(service=s) as driver:
    driver.get("http://suninjuly.github.io/huge_form.html")
    elements = driver.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("Мой ответ")
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(5)
