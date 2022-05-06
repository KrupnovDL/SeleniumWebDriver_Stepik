from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def form_control_required(link):
    s = Service(ChromeDriverManager().install())
    with webdriver.Chrome(service=s) as driver:
        driver.implicitly_wait(5)
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

        # находим элемент, содержащий текст
        welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        return welcome_text


def test_abs1():
    assert form_control_required("http://suninjuly.github.io/registration1.html") == "Congratulations! You have successfully registered!", "Registration failed"


def test_abs2():
    assert form_control_required("http://suninjuly.github.io/registration2.html") == "Congratulations! You have successfully registered!", "Registration failed"
