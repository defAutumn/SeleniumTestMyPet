from pages.base_page import BasePage
from locators.authorization_page_locators import AuthorizationPageLocators as Locators
from input_data.input_data import Data
import time


class AuthorizationPage(BasePage):

    def fill_fields_and_submit(self):

        username = Data.username
        password = Data.password

        time.sleep(2)

        self.driver.find_element(*Locators.USERNAME).send_keys(username)
        self.driver.find_element(*Locators.PASSWORD).send_keys(password)
        self.driver.find_element(*Locators.SUBMIT).click()

        time.sleep(5)

        return username

    def authorization_result(self):
        result = self.element_is_visible(Locators.RESULT)

        return result.text