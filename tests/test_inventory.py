class TestInventory:

    def test_inventory_items_displayed(self, logged_in_inventory):
        # После логина мы на inventory
        assert logged_in_inventory.get_items_count() == 6
        assert "inventory" in logged_in_inventory.page.url

    def test_sort_by_price_low_to_high(self, logged_in_inventory):
        logged_in_inventory.sort_by("lohi")
        prices = logged_in_inventory.get_item_prices()
        assert prices == sorted(prices)

    def test_add_item_to_cart(self, logged_in_inventory):
        logged_in_inventory.add_to_cart_by_name("Sauce Labs Backpack")
        assert logged_in_inventory.get_cart_count() == 1

    def test_cart_counter_increases(self, logged_in_inventory):
        assert logged_in_inventory.get_cart_count() == 0
        logged_in_inventory.add_to_cart_by_name("Sauce Labs Backpack")
        assert logged_in_inventory.get_cart_count() == 1
        logged_in_inventory.add_to_cart_by_name("Sauce Labs Bike Light")
        assert logged_in_inventory.get_cart_count() == 2