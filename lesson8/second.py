import pytest


def test_first_brow(new_browser, url_maker):
    new_browser.get(url_maker)
    new_browser.find_element_by_css_selector("img[alt=MacBook]")
    new_browser.find_element_by_css_selector('.input-group-btn')
    new_browser.find_element_by_css_selector('#content>.row>div:nth-child(2) button[data-original-title="Add to Wish List"]')
    new_browser.find_element_by_css_selector("footer .container .row>:nth-child(2) .list-unstyled>:nth-child(2)")
    new_browser.find_element_by_css_selector("footer .container .row>:nth-child(2) .list-unstyled>:nth-child(2)")
    # assert new_browser.title == 'Your Store'


def test_second_brow(new_browser, url_maker):
    new_browser.get(url_maker + "/index.php?route=product/category&path=20")
    new_browser.find_element_by_css_selector("#product-category #content .col-sm-3 a")
    new_browser.find_element_by_css_selector('.breadcrumb > li:nth-child(2) > a:nth-child(1)')
    new_browser.find_element_by_css_selector('#content>.row>div:nth-child(2) button[data-original-title="Add to Wish List"]')
    new_browser.find_element_by_css_selector(".btn-inverse")
    new_browser.find_element_by_css_selector(".row>:nth-child(2).product-layout.product-grid div[class=image]")


def test_third_brow(new_browser, url_maker):
    new_browser.get(url_maker +"/index.php?route=product/product&path=57&product_id=49")
    new_browser.find_element_by_css_selector("#content div.col-sm-4 > h1")
    new_browser.find_element_by_css_selector('.form-group #button-cart')
    new_browser.find_element_by_css_selector('ul.thumbnails .thumbnail img')
    new_browser.find_element_by_css_selector(".col-sm-4 .btn-group>:nth-child(1)")
    new_browser.find_element_by_css_selector("#content  div.col-sm-4 > ul:nth-child(4) h2")


def test_four_brow(new_browser, url_maker):
    new_browser.get(url_maker + "/index.php?route=account/login")
    new_browser.find_element_by_css_selector("#content > div > div:nth-child(1) > div")
    new_browser.find_element_by_css_selector('input[name="code"]')
    new_browser.find_element_by_css_selector('input[name="password"]')
    new_browser.find_element_by_css_selector("input.btn.btn-primary")
    new_browser.find_element_by_css_selector("a.btn.btn-primary")


def test_five_brow(new_browser, url_maker):
    new_browser.get(url_maker + "/admin/")
    new_browser.find_element_by_css_selector("#input-username")
    new_browser.find_element_by_css_selector('#input-password')
    new_browser.find_element_by_css_selector('.btn.btn-primary')
    new_browser.find_element_by_css_selector(".help-block a")
    new_browser.find_element_by_css_selector("#footer")