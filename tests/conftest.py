import pytest

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


STANDARD_USER = "standard_user"
LOCKED_USER = "locked_out_user"
PASSWORD = "secret_sauce"


@pytest.fixture
def login_page(page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def inventory_page(page) -> InventoryPage:
    return InventoryPage(page)


@pytest.fixture
def cart_page(page) -> CartPage:
    return CartPage(page)


@pytest.fixture
def logged_in_inventory(login_page, inventory_page):
    """Логинится под standard_user и возвращает InventoryPage."""
    login_page.open()
    login_page.login(STANDARD_USER, PASSWORD)
    inventory_page.wait_for(InventoryPage.INVENTORY_ITEMS)
    return inventory_page