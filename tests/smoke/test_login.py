import pytest
from pages.login_page import LoginPage


@pytest.mark.smoke
def test_valid_login(page):

    login = LoginPage(page)

    login.open()

    login.login(
        "Admin",
        "admin123"
    )

    assert login.is_login_successful()