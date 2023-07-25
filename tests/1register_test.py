from pages.register_page import RegisterPage


class TestRegisterPage:

    def test_register(self, driver):
        register_page = RegisterPage(driver, 'https://defautumn.pythonanywhere.com/users/register/')
        register_page.open()
        user = register_page.fill_fields_and_submit()
        result = register_page.register_result()
        assert user == result
