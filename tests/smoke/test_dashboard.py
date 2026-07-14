import pytest

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@pytest.mark.smoke
def test_dashboard(page):

    login = LoginPage(page)

    login.open()

    login.login(
        "Admin",
        "admin123"
    )

    dashboard = DashboardPage(page)

    assert dashboard.is_dashboard_loaded()
    assert dashboard.is_sidebar_visible()
    assert dashboard.is_user_dropdown_visible()
    assert dashboard.is_search_box_visible()