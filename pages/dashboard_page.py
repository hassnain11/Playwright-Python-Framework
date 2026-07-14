from pages.base_page import BasePage


class DashboardPage(BasePage):

    DASHBOARD_TITLE = "h6"
    USER_DROPDOWN = ".oxd-userdropdown-name"
    SIDEBAR = ".oxd-sidepanel"
    SEARCH_BOX = "input[placeholder='Search']"

    def is_dashboard_loaded(self):
        self.wait_for_visible(self.DASHBOARD_TITLE)
        return self.get_text(self.DASHBOARD_TITLE) == "Dashboard"

    def is_sidebar_visible(self):
        return self.is_visible(self.SIDEBAR)

    def is_user_dropdown_visible(self):
        return self.is_visible(self.USER_DROPDOWN)

    def is_search_box_visible(self):
        return self.is_visible(self.SEARCH_BOX)