from pages.base_page import BasePage


class AdminPage(BasePage):

    ADMIN_MENU = "a[href*='admin']"
    USERNAME_INPUT = "input.oxd-input"
    SEARCH_BUTTON = "button[type='submit']"
    ADD_BUTTON = "button:has-text('Add')"
    ADD_USER_TITLE = "h6:has-text('Add User')"

    def open(self):
        self.click(self.ADMIN_MENU)

    def open_admin(self):
        self.open()

    def search_username(self, username):
        field = self.page.locator(self.USERNAME_INPUT).nth(1)
        field.fill(username)

    def click_search(self):
        self.click(self.SEARCH_BUTTON)

    def click_add(self):
        self.click(self.ADD_BUTTON)

    def is_add_user_page_displayed(self):
        return self.is_visible(self.ADD_USER_TITLE)
    
    RESULT_TABLE = ".oxd-table-body"

    def results_visible(self):
        return self.is_visible(self.RESULT_TABLE)