from pages.base_page import BasePage


class SidebarPage(BasePage):

    USER_DROPDOWN = ".oxd-userdropdown-tab"
    LOGOUT = "a:has-text('Logout')"

    def open_user_menu(self):
        self.click(self.USER_DROPDOWN)

    def click_logout(self):
        self.click(self.LOGOUT)

    def logout(self):
        self.open_user_menu()
        self.click_logout()

    def is_logged_out(self):
        self.wait_for_url("**/auth/login")
        return self.page.url.endswith("/auth/login")