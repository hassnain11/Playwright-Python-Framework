from playwright.sync_api import expect


class BasePage:

    def __init__(self, page):
        self.page = page

    def open(self, url):
        self.page.goto(
            url,
            wait_until="domcontentloaded",
            timeout=60000
        )

    def click(self, locator):
        element = self.page.locator(locator)
        element.wait_for(state="visible")
        element.click()

    def fill(self, locator, text):
        field = self.page.locator(locator)

        field.wait_for(state="visible", timeout=10000)

        field.click()

        field.fill("")

        field.fill(text)

        expect(field).to_have_value(text)

    def type(self, locator, text):
        self.fill(locator, text)

    def get_text(self, locator):
        return self.page.locator(locator).inner_text().strip()

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()

    def wait_for_visible(self, locator):
        self.page.locator(locator).wait_for(
            state="visible",
            timeout=10000
        )

    def wait_for_url(self, url):
        self.page.wait_for_url(
            url,
            timeout=10000
        )