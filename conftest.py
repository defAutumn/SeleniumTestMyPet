import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def driver():
    driver_service = Service(executable_path='chromedriver_win32/chromedriver.exe')
    driver = webdriver.Chrome(service=driver_service)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()
