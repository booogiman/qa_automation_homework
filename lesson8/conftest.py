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

@pytest.fixture
def url_maker(request):
    args1 = request.config.getoption("--host")
    return f"https://{args1}"
@pytest.fixture
def new_browser(request):
    args = request.config.getoption("--brows")
    if args == "gh":
        # gdd = GeckoDriverManager
        # gdd.download_and_install()
        option = webdriver.ChromeOptions()
        # option.add_argument("--headless")
        option.add_argument("--start-fullscreen")
        wd = webdriver.Chrome(options=option)
    elif args == "ff":
        # gdd = GeckoDriverManager
        # gdd.download_and_install()
        option = webdriver.FirefoxOptions()
        option.add_argument("--headless")
        # option.add_argument("--start-maximized")
        option.add_argument("--kiosk")
        wd = webdriver.Firefox(options=option)
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
