import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from gh_token import GH_TOKEN
import os


os.environ['GH_TOKEN'] = GH_TOKEN


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption("--language", action="store", default="en",
                     help="Enter language")


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    driver = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        s = Service(ChromeDriverManager().install())
        op = Options()
        op.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        driver = webdriver.Chrome(service=s, options=op)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        s = Service(GeckoDriverManager().install())
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        driver = webdriver.Firefox(service=s, firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    driver.maximize_window()
    driver.implicitly_wait(7)
    yield driver
    print("\nquit browser..")
    driver.quit()
