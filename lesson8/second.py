import sqlite3
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


def wait_web(browser, wd):
    wait = WebDriverWait(wd, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, browser)))


def test_first_brow(new_browser, url_maker):
    new_browser.get(url_maker)
    wait_web("img[alt=MacBook]", new_browser)
    wait_web(".input-group-btn", new_browser)
    wait_web("#content>.row>div:nth-child(2) button[data-original-title='Add to Wish List']", new_browser)
    wait_web("footer .container .row>:nth-child(2) .list-unstyled>:nth-child(2)", new_browser)
    wait_web("footer .container .row>:nth-child(2) .list-unstyled>:nth-child(2)", new_browser)
    assert new_browser.title == 'Your Store'


def test_second_brow(new_browser, url_maker):
    new_browser.get(url_maker + "/index.php?route=product/category&path=20")
    wait_web("#product-category #content .col-sm-3 a", new_browser)
    wait_web('.breadcrumb > li:nth-child(2) > a:nth-child(1)', new_browser)
    wait_web('#content>.row>div:nth-child(2) button[data-original-title="Add to Wish List"]', new_browser)
    wait_web(".btn-inverse", new_browser)
    wait_web(".row>:nth-child(2).product-layout.product-grid div[class=image]", new_browser)
    time.sleep(5)


def test_third_brow(new_browser, url_maker):
    new_browser.get(url_maker + "/index.php?route=product/product&path=57&product_id=49")
    wait_web("#content div.col-sm-4 > h1", new_browser)
    wait_web('.form-group #button-cart', new_browser)
    wait_web('ul.thumbnails .thumbnail img', new_browser)
    wait_web(".col-sm-4 .btn-group>:nth-child(1)", new_browser)
    wait_web("#content  div.col-sm-4 > ul:nth-child(4) h2", new_browser)


def test_four_brow(new_browser, url_maker):
    new_browser.get(url_maker + "/index.php?route=account/login")
    wait_web("#content > div > div:nth-child(1) > div", new_browser)
    wait_web('input[name="code"]', new_browser)
    wait_web('input[name="password"]', new_browser)
    wait_web("input.btn.btn-primary", new_browser)
    wait_web("a.btn.btn-primary", new_browser)


def test_five_brow(new_browser, url_maker):
    new_browser.get(url_maker + "/admin/")
    wait_web("#input-username", new_browser)
    wait_web('#input-password', new_browser)
    wait_web('.btn.btn-primary', new_browser)
    wait_web(".help-block a", new_browser)
    wait_web("#footer", new_browser)
