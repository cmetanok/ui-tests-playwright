from playwright.sync_api import Page

from pages.base_page import BasePage


class CartPage(BasePage):
    """Страница корзины."""

    # Локаторы
    TITLE = "[data-test='title']"
    CART_ITEMS = ".cart_item"
    CART_ITEM_NAMES = ".inventory_item_name"
    CHECKOUT_BUTTON = "[data-test='checkout']"
    REMOVE_BUTTONS = ".cart_button"

    def __init__(self, page: Page):
        super().__init__(page)

    def open(self):
        super().open("/cart.html")

    def get_title(self) -> str:
        return self.get_text(self.TITLE)

    def get_items_count(self) -> int:
        return self.page.locator(self.CART_ITEMS).count()

    def get_item_names(self) -> list[str]:
        return self.page.locator(self.CART_ITEM_NAMES).all_inner_texts()

    def remove_item_by_name(self, item_name: str):
        item = self.page.locator(self.CART_ITEMS).filter(has_text=item_name)
        item.locator(self.REMOVE_BUTTONS).click()

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)