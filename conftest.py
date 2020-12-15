import pytest
from selenium import webdriver


# parameter language
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: en, ru, fr, es etc.")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    print("\nstart chrome browser for test..")
    options = webdriver.ChromeOptions()
    options.add_argument('--lang=' + language)
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit chrome browser..")
    browser.quit()

