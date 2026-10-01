from playwright.sync_api import Page, expect


class BasePage:
    """Базовый класс для всех Page Object'ов."""

    BASE_URL = "https://www.saucedemo.com"

    def __init__(self, page: Page):
        self.page = page

    def open(self, path: str = "/"):
        """Открыть страницу по относительному пути."""
        self.page.goto(f"{self.BASE_URL}{path}")

    def click(self, selector: str):
        self.page.locator(selector).click()

    def fill(self, selector: str, value: str):
        self.page.locator(selector).fill(value)

    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).inner_text()

    def is_visible(self, selector: str) -> bool:
        return self.page.locator(selector).is_visible()

    def wait_for(self, selector: str):
        self.page.locator(selector).first.wait_for()

    def expect_visible(self, selector: str):
        expect(self.page.locator(selector)).to_be_visible()

    def expect_text(self, selector: str, text: str):
        expect(self.page.locator(selector)).to_have_text(text)