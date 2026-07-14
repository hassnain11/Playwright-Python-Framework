import pytest

from pages.login_page import LoginPage
from pages.admin_page import AdminPage


@pytest.mark.regression
def test_open_add_user(page):

    login = LoginPage(page)

    login.open()

    login.login(
        "Admin",
        "admin123"
    )

    admin = AdminPage(page)

    admin.open_admin()

    admin.click_add()