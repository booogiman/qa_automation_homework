from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


def wait_web(locator, driver):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))


def test_first_brow(login):
    browser = login
    wait_web("#menu-catalog a", browser)
    _category = browser.find_element_by_css_selector("a[href='#collapse1']")
    _category.click()
    product = browser.find_element_by_css_selector("ul[id='collapse1'] li")
    product.click()
    wait_web('a[data-original-title="Add New"]', browser)
    add = browser.find_element_by_css_selector('a[data-original-title="Add New"]')
    add.click()

    wait_web('input[name="category_description[1][name]"]', browser)
    browser.find_element_by_css_selector('input[name="category_description[1][name]"]').send_keys("Test_category")
    time.sleep(2)
    browser.find_element_by_css_selector('input[name="category_description[1][meta_title]"]').send_keys("Test_Meta_teg")
    time.sleep(2)
    browser.find_element_by_css_selector('button[type="submit"]').click()
    time.sleep(2)
    print(browser.find_element_by_css_selector("tbody tr td:nth-child(2)").text)
    assert browser.find_element_by_css_selector("tbody tr td:nth-child(2)").text == "1"
    time.sleep(5)


def test_delet_sec_categori(login):
    browser = login
    wait_web("#menu-catalog a", browser)
    _category = browser.find_element_by_css_selector("a[href='#collapse1']")
    _category.click()
    time.sleep(2)
    product = browser.find_element_by_css_selector("ul[id='collapse1'] li")
    product.click()
    time.sleep(2)
    browser.find_element_by_css_selector('tbody tr:nth-child(2) td input').click()
    time.sleep(2)
    delete = browser.find_element_by_css_selector('button[data-original-title="Delete"]')
    delete.click()
    time.sleep(2)
    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(2)
    wait_web(".alert.alert-success.alert-dismissible", browser)
    p = browser.find_element_by_css_selector(".alert")
    assert p.tag_name == "div"


def test_login(login):
    browser = login
    wait_web(".hidden-xs.hidden-sm.hidden-md", browser)
    logout = browser.find_element_by_css_selector(".hidden-xs.hidden-sm.hidden-md")
    assert logout.text == "Logout"

def test_logout(login):
    browser = login
    wait_web(".nav.navbar-nav.navbar-right > li:nth-child(2) a", browser)
    logout = browser.find_element_by_css_selector(".nav.navbar-nav.navbar-right > li:nth-child(2) a")
    logout.click()
    logout_form = browser.find_element_by_css_selector(".panel-title")
    assert logout_form.text == "Please enter your login details."