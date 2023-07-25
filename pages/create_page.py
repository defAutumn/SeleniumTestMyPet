from pages.base_page import BasePage
from locators.create_page_locators import CreatePageLocators as Locators
from selenium.webdriver.common.keys import Keys
from input_data.input_data import Data
import time
import os


class CreatePage(BasePage):

    def login_link(self):

        time.sleep(2)

        self.driver.find_element(*Locators.LOGIN).click()

        time.sleep(2)

    def auth(self):
        username = Data.username
        password = Data.password

        self.driver.find_element(*Locators.USERNAME).send_keys(username)
        self.driver.find_element(*Locators.PASSWORD).send_keys(password)
        self.driver.find_element(*Locators.SUBMIT).click()

        time.sleep(2)

    def fill_fields_and_submit(self,img):

        title = Data.title
        describe = Data.describe
        path = img

        self.driver.find_element(*Locators.ADD_RECIPE).click()

        time.sleep(5)

        self.driver.find_element(*Locators.ADD).send_keys(Keys.PAGE_DOWN)
        time.sleep(5)
        self.driver.find_element(*Locators.TITLE).send_keys(title)
        self.driver.find_element(*Locators.DESCRIBE).send_keys(describe)
        time.sleep(5)
        self.driver.find_element(*Locators.IMAGE).send_keys(path)
        self.driver.find_element(*Locators.ADD).click()

        time.sleep(2)

        return title,describe

    def create_result(self):
        self.driver.find_element(*Locators.ALL_RECIPES).click()
        self.driver.find_element(*Locators.TITLE_LINK).send_keys(Keys.END)

        time.sleep(5)

        # title_link = self.element_is_visible(Locators.TITLE_LINK)
        self.driver.find_element(*Locators.TITLE_LINK).click()

        time.sleep(5)

        self.driver.find_element(*Locators.BODY).send_keys(Keys.END)

        time.sleep(5)

        title_inner = self.element_is_visible(Locators.TITLE_INNER)
        describe_inner = self.element_is_visible(Locators.DESCRIBE_INNER)

        return title_inner.text,describe_inner.text
