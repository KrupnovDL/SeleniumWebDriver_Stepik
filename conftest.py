import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os


os.environ['GH_TOKEN'] = "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"


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("browser_name")
    driver = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        s = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=s)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    driver.maximize_window()
    driver.implicitly_wait(7)
    yield driver
    print("\nquit browser..")
    driver.quit()
