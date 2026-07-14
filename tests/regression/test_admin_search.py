import pytest

from pages.login_page import LoginPage
from pages.admin_page import AdminPage


@pytest.mark.regression
def test_search_admin_user(page):

    login = LoginPage(page)

    login.open()

    login.login(
        "Admin",
        "admin123"
    )

    admin = AdminPage(page)

    admin.open()

    admin.search_username("Admin")

    admin.click_search()

    assert admin.results_visible()