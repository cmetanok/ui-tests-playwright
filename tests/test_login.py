import pytest

from tests.conftest import STANDARD_USER, LOCKED_USER, PASSWORD


class TestLogin:

    def test_successful_login(self, login_page):
        login_page.open()
        login_page.login(STANDARD_USER, PASSWORD)

        # Проверяем, что перешли на страницу товаров
        login_page.page.wait_for_url("**/inventory.html")
        assert "inventory" in login_page.page.url

    def test_locked_out_user(self, login_page):
        login_page.open()
        login_page.login(LOCKED_USER, PASSWORD)

        assert login_page.is_error_visible()
        error = login_page.get_error_message()
        assert "locked out" in error.lower()

    def test_wrong_password(self, login_page):
        login_page.open()
        login_page.login(STANDARD_USER, "wrong_password")

        assert login_page.is_error_visible()
        error = login_page.get_error_message()
        assert "username and password do not match" in error.lower()

    def test_empty_fields(self, login_page):
        login_page.open()
        login_page.click(login_page.LOGIN_BUTTON)

        assert login_page.is_error_visible()
        error = login_page.get_error_message()
        assert "username is required" in error.lower()