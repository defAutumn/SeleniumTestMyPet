from pages.authorization_page import AuthorizationPage


class TestAuthorizationPage:

    def test_authorization(self, driver):
        authorization_page = AuthorizationPage(driver, 'https://defautumn.pythonanywhere.com/users/login/')
        authorization_page.open()
        user = authorization_page.fill_fields_and_submit()
        result = authorization_page.authorization_result()
        assert user == result

