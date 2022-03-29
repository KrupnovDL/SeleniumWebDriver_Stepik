from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


def form_control_required(link):
    with webdriver.Chrome() as browser:
        browser.implicitly_wait(5)
        browser.get(link)

        # Мой код, который заполняет обязательные поля
        first_name_input = browser.find_element(By.CSS_SELECTOR, ".form-control.first:required")
        first_name_input.send_keys("Мой ответ")
        last_name_input = browser.find_element(By.CSS_SELECTOR, ".form-control.second:required")
        last_name_input.send_keys("Мой ответ")
        email_input = browser.find_element(By.CSS_SELECTOR, ".form-control.third:required")
        email_input.send_keys("Мой ответ")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        return welcome_text


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        self.assertEqual(form_control_required("http://suninjuly.github.io/registration1.html"), "Congratulations! You have successfully registered!", "Registration failed")

    def test_abs2(self):
        self.assertEqual(form_control_required("http://suninjuly.github.io/registration2.html"), "Congratulations! You have successfully registered!", "Registration failed")


if __name__ == "__main__":
    unittest.main()
