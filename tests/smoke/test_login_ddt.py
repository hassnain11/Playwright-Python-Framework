import pytest

from pages.login_page import LoginPage
from utilities.json_reader import load_json


test_data = load_json("test_data/login_data.json")


@pytest.mark.smoke
@pytest.mark.parametrize("data", test_data)
def test_login_ddt(page, data):

    login = LoginPage(page)

    login.open()

    login.login(
        data["username"],
        data["password"]
    )

    if data["expected"]:
        assert login.is_login_successful()
    else:
        assert login.is_login_failed()