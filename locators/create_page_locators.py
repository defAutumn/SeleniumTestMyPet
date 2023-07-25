from selenium.webdriver.common.by import By
from input_data.input_data import Data



class CreatePageLocators:
    LOGIN = (By.ID, 'create_login')
    USERNAME = (By.ID, 'id_username')
    PASSWORD = (By.ID, 'id_password')
    SUBMIT = (By.CLASS_NAME, 'btn')
    ADD_RECIPE = (By.ID, 'create')
    TITLE = (By.ID, 'id_title')
    DESCRIBE = (By.ID, 'id_describe')
    IMAGE = (By.ID, 'id_image')
    ADD = (By.ID,'knopka')
    ALL_RECIPES = (By.ID, 'all_rec')
    TITLE_LINK = (By.LINK_TEXT, Data.title)
    BODY = (By.TAG_NAME, 'body')
    TITLE_INNER = (By.ID,'title_inner')
    DESCRIBE_INNER = (By.ID,'describe_inner')
