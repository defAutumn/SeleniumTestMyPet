from pages.base_page import BasePage
from locators.register_page_locators import RegisterPageLocators as Locators
from selenium.webdriver.common.keys import Keys
from input_data.input_data import Data
import time


class RegisterPage(BasePage):

    def fill_fields_and_submit(self):
        username = Data.username
        email = Data.email
        password = Data.password

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