from selenium.webdriver.common.by import By


class AuthorizationPageLocators:
    USERNAME = (By.ID, 'id_username')
    PASSWORD = (By.ID, 'id_password')
    SUBMIT = (By.CLASS_NAME, 'btn')
    RESULT = (By.ID,'user')