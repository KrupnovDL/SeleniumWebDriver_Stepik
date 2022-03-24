from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import pyperclip

with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/file_input.html")
    browser.find_element(By.NAME, "firstname").send_keys("Dmitrii")
    browser.find_element(By.NAME, "lastname").send_keys("Krupnov")
    browser.find_element(By.NAME, "email").send_keys("krupnov.96@list.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    browser.find_element(By.NAME, "file").send_keys(file_path)
    browser.find_element(By.TAG_NAME, "button").click()
    alert = browser.switch_to.alert
    pyperclip.copy(alert.text.split(': ')[-1])
