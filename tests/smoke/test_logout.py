import pytest

from pages.login_page import LoginPage
from pages.sidebar_page import SidebarPage


@pytest.mark.smoke
def test_logout(page):

    login = LoginPage(page)

    login.open()

    login.login(
        "Admin",
        "admin123"
    )

    sidebar = SidebarPage(page)

    sidebar.logout()

    assert sidebar.is_logged_out()