from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import ChromeOptions
from webdrivermanager import GeckoDriverManager


def test_example():
    gdd = GeckoDriverManager()
    gdd.download_and_install()
    option = FirefoxOptions()
    option.add_argument("--kiosk")
    # option.headless = True
    wd = webdriver.Firefox(options=option)
    wd.get("https://otus.ru/")
    assert wd.title == 'Онлайн‑курсы для профессионалов, дистанционное обучение современным профессиям'
    wd.quit()
