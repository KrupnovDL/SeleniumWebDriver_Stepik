from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

s = Service(ChromeDriverManager().install())
with webdriver.Chrome(service=s) as driver:
    driver.get(link)
    button = driver.find_element(By.ID, "submit_button")
    button.click()
