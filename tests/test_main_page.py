import time
import pytest
from pages.main_page import MainPage


@pytest.mark.regression
def test_go_to_login_page(browser):
    link = "http://34.141.58.52:8080/#/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    browser.save_screenshot("result1.png")


@pytest.mark.smoke
def test_go_to_filter_by_dog(browser):
    link = "http://34.141.58.52:8080/#/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_filter_by_type()
    page.go_to_filter_by_dog()
    time.sleep(2)
    browser.save_screenshot("result2.png")



