import pytest
import requests
import argparse
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import Edge
from webdrivermanager import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption('--brows',
                     help='brows',
                     type=str,
                     default='gh',
                     choices=['gh', 'ff', 'ie']
                     )
    parser.addoption('--host',
                     help='main host',
                     type=str,
                     default='localhost',
                     )
    parser.addoption('--port',
                     help='port connect',
                     type=str,
                     default='80',
                     )


@pytest.fixture
def login(new_browser, url_maker):
    new_browser.get(f"{url_maker}/admin")
    new_browser.find_element_by_css_selector('input[name="username"]').send_keys("user")
    new_browser.find_element_by_css_selector('input[name="password"]').send_keys("bitnami1")
    new_browser.find_element_by_css_selector('button[type="submit"]').click()
    return new_browser



@pytest.fixture
def url_maker(request):
    args1 = request.config.getoption("--host")
    port = request.config.getoption("--port")
    return f"http://{args1}:{port}"
@pytest.fixture
def new_browser(request):
    args = request.config.getoption("--brows")
    if args == "gh":
        # gdd = GeckoDriverManager
        # gdd.download_and_install()
        option = webdriver.ChromeOptions()
        # option.add_argument("--headless")
        option.add_argument("--start-fullscreen")
        option.add_argument('ignore-certificate-errors')
        wd = webdriver.Chrome(chrome_options=option)
    elif args == "ff":
        # gdd = GeckoDriverManager
        # gdd.download_and_install()
        option = webdriver.FirefoxOptions()
        # option.add_argument("--headless")
        option.add_argument("--start-maximized")
        option.add_argument("--kiosk")
        option.accept_insecure_certs = True
        wd = webdriver.Firefox(firefox_profile=option)
    elif args == "ie":
        # gdd = GeckoDriverManager
        # gdd.download_and_install()
        option = webdriver.IeOptions()
        option.add_argument("--embedding")
        # option.add_argument("-k")
        wd = webdriver.Ie(options=option)
    # yield wd
    # wd.quit()
    request.addfinalizer(wd.quit)
    return wd
