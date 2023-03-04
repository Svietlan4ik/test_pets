from .locators import MainPageLocators
from .base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def go_to_filter_by_type(self):
        filter_by_type = self.browser.find_element(*MainPageLocators.FILTER_BY_TYPE)
        filter_by_type.click()

    def go_to_filter_by_dog(self):
        filter_by_dog = self.browser.find_element(*MainPageLocators.FILTER_BY_DOG)
        filter_by_dog.click()

