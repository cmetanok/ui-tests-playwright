class TestCart:

    def test_added_item_shows_in_cart(self, logged_in_inventory, cart_page):
        item_name = "Sauce Labs Backpack"
        logged_in_inventory.add_to_cart_by_name(item_name)
        logged_in_inventory.go_to_cart()

        cart_page.wait_for(cart_page.CART_ITEMS)
        assert cart_page.get_items_count() == 1
        assert item_name in cart_page.get_item_names()

    def test_remove_item_from_cart(self, logged_in_inventory, cart_page):
        item_name = "Sauce Labs Backpack"
        logged_in_inventory.add_to_cart_by_name(item_name)
        logged_in_inventory.go_to_cart()

        cart_page.wait_for(cart_page.CART_ITEMS)
        cart_page.remove_item_by_name(item_name)
        assert cart_page.get_items_count() == 0

    def test_checkout_button(self, logged_in_inventory, cart_page):
        logged_in_inventory.add_to_cart_by_name("Sauce Labs Backpack")
        logged_in_inventory.go_to_cart()

        cart_page.wait_for(cart_page.CHECKOUT_BUTTON)
        cart_page.click_checkout()

        # После checkout попадаем на страницу с формой
        cart_page.page.wait_for_url("**/checkout-step-one.html")
        assert "checkout-step-one" in cart_page.page.url