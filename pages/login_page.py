from config.config import BASE_URL
from pages.base_page import BasePage


class LoginPage(BasePage):

    USERNAME_INPUT = "input[name='username']"
    PASSWORD_INPUT = "input[name='password']"
    LOGIN_BUTTON = "button[type='submit']"
    DASHBOARD_TITLE = "h6"

    def open(self):
        super().open(f"{BASE_URL}/web/index.php/auth/login")

    def enter_username(self, username):
        self.fill(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.fill(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def is_login_successful(self):
        self.page.wait_for_url("**/dashboard/index")
        return "/dashboard/index" in self.page.url
    
    ERROR_MESSAGE = ".oxd-alert-content-text"

    def is_login_failed(self):
        self.wait_for_visible(self.ERROR_MESSAGE)
        return "Invalid credentials" in self.get_text(self.ERROR_MESSAGE)