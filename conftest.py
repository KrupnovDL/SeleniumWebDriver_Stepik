import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.implicitly_wait(7)
    yield browser
    print("\nquit browser..")
    browser.quit()
