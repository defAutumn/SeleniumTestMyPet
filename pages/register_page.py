from pages.base_page import BasePage
from locators.register_page_locators import RegisterPageLocators as Locators
from selenium.webdriver.common.keys import Keys
import input_data
import time


class RegisterPage(BasePage):

    def fill_fields_and_submit(self):
        username = input_data.username
        email = input_data.email
        password = input_data.password
        time.sleep(2)
        self.driver.find_element(*Locators.SUBMIT).send_keys(Keys.END)
        self.driver.find_element(*Locators.USERNAME).send_keys(username)
        self.driver.find_element(*Locators.EMAIL).send_keys(email)
        self.driver.find_element(*Locators.PASSWORD).send_keys(password)
        self.driver.find_element(*Locators.PASSWORD_CONFIRM).send_keys(password)
        self.driver.find_element(*Locators.SUBMIT).click()

        time.sleep(5)

        return username

    def register_result(self):
        result = self.element_is_visible(Locators.RESULT)
        time.sleep(5)
        return result.text
