import pytest
from pages.login_page import LoginPage

class TestLogin:
    def test_login_valid(self, page, valid_user):
        login = LoginPage(page)
        login.navigate()
        login.login(valid_user['username'], valid_user['password'])
        assert 'inventory.html' in page.url, \
        f"Failed for user `{valid_user['username']}`"

    def test_login_invalid(self, page, users):
        login = LoginPage(page)
        login.navigate()
        login.login(**users['invalid'])
        assert 'do not match' in login.get_error()

    def test_login_locked(self, page, users):
        login = LoginPage(page)
        login.navigate()
        login.login(**users['locked'])
        assert 'locked out' in login.get_error()