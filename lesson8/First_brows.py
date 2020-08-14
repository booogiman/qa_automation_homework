import os

from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import ChromeOptions
from selenium.webdriver import IeOptions
from webdrivermanager import GeckoDriverManager


def test_first_brow(new_browser, url_maker):
    # gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
    # gdd = GeckoDriverManager()
    # gdd.download_and_install()
    # option.headless = True
    # option.add_argument("headless")
    # option.add_argument("start-fullscreen")
    # new_browser.get(url_maker)
    # print(new_browser)
    # print(url_maker)
    new_browser.get("http://cp.vagrant2.devel.sweb.ru:10001/main/")
    # content = new_browser.find_element_by_css_selector('a[href^="http://localhost/index.php?route=product/product&amp;product_id=30"]')
    # print(content)
    # assert new_browser.title == 'Your Store'
