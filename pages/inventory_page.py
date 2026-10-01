from playwright.sync_api import Page

from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Страница со списком товаров (inventory)."""

    # Локаторы
    TITLE = "[data-test='title']"
    INVENTORY_ITEMS = ".inventory_item"
    ITEM_NAMES = ".inventory_item_name"
    ITEM_PRICES = ".inventory_item_price"
    SORT_SELECT = "[data-test='product-sort-container']"
    CART_BADGE = "[data-test='shopping-cart-badge']"
    CART_LINK = "[data-test='shopping-cart-link']"

    def __init__(self, page: Page):
        super().__init__(page)

    def open(self):
        super().open("/inventory.html")

    def get_title(self) -> str:
        return self.get_text(self.TITLE)

    def get_items_count(self) -> int:
        return self.page.locator(self.INVENTORY_ITEMS).count()

    def get_item_names(self) -> list[str]:
        return self.page.locator(self.ITEM_NAMES).all_inner_texts()

    def get_item_prices(self) -> list[float]:
        texts = self.page.locator(self.ITEM_PRICES).all_inner_texts()
        return [float(t.replace("$", "")) for t in texts]

    def sort_by(self, value: str):
        """value: 'az', 'za', 'lohi', 'hilo'."""
        self.page.locator(self.SORT_SELECT).select_option(value)

    def add_to_cart_by_name(self, item_name: str):
        """Нажать 'Add to cart' у товара с указанным именем."""
        item = self.page.locator(self.INVENTORY_ITEMS).filter(
            has_text=item_name
        )
        item.locator("button").click()

    def remove_from_cart_by_name(self, item_name: str):
        item = self.page.locator(self.INVENTORY_ITEMS).filter(
            has_text=item_name
        )
        item.locator("button").click()

    def get_cart_count(self) -> int:
        """Возвращает число на бейдже корзины (0, если бейджа нет)."""
        if self.page.locator(self.CART_BADGE).count() == 0:
            return 0
        return int(self.get_text(self.CART_BADGE))

    def go_to_cart(self):
        self.click(self.CART_LINK)