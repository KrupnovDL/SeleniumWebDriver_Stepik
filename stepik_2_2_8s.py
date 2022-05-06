from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
import pyperclip

s = Service(ChromeDriverManager().install())
with webdriver.Chrome(service=s) as driver:
    driver.get("http://suninjuly.github.io/file_input.html")
    driver.find_element(By.NAME, "firstname").send_keys("Dmitrii")
    driver.find_element(By.NAME, "lastname").send_keys("Krupnov")
    driver.find_element(By.NAME, "email").send_keys("krupnov.96@list.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    driver.find_element(By.NAME, "file").send_keys(file_path)
    driver.find_element(By.TAG_NAME, "button").click()
    alert = driver.switch_to.alert
    pyperclip.copy(alert.text.split(': ')[-1])
