from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

s = Service(ChromeDriverManager().install())
with webdriver.Chrome(service=s) as driver:
    link = "http://suninjuly.github.io/registration2.html"
    driver.get(link)

    # Мой код, который заполняет обязательные поля
    first_name_input = driver.find_element(By.CSS_SELECTOR, ".form-control.first:required")
    first_name_input.send_keys("Мой ответ")
    last_name_input = driver.find_element(By.CSS_SELECTOR, ".form-control.second:required")
    last_name_input.send_keys("Мой ответ")
    email_input = driver.find_element(By.CSS_SELECTOR, ".form-control.third:required")
    email_input.send_keys("Мой ответ")

    # Отправляем заполненную форму
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
