from selenium.webdriver.common.by import By

class RegisterPageLocators:
    USERNAME = (By.ID, 'id_username')
    EMAIL = (By.NAME, 'email')
    PASSWORD = (By.NAME, 'password1')
    PASSWORD_CONFIRM = (By.NAME, 'password2')
    SUBMIT = (By.CLASS_NAME, 'btn')
    RESULT = (By.ID,'user')