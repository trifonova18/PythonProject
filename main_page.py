import time

from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators


from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

        login_send = self.browser.find_element(*LoginPageLocators.LOGIN_SEND)
        login_send.send_keys('ionas0988@gmail.com')
        pass_send = self.browser.find_element(*LoginPageLocators.PASS_SEND)
        pass_send.send_keys('Abc12345!@#')
        time.sleep(2)
        button = self.browser.find_element(*LoginPageLocators.LOGIN_BUT)
        button.click()
        time.sleep(5)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

