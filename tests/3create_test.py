import os
from pages.create_page import CreatePage


class TestCreatePage:

    def test_create(self, driver):

        create_page = CreatePage(driver, 'https://defautumn.pythonanywhere.com/create')
        create_page.open()
        create_page.login_link()
        create_page.auth()

        img = os.getcwd() + '/input_data/img/test_img.png'
        path = img.replace('\\', '/')

        result_1 = create_page.fill_fields_and_submit(path)
        result_2 = create_page.create_result()
        assert result_1==result_2