import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

class TestCart:
    @pytest.fixture(autouse=True)
    def setup(self, page, valid_user):
        self.page = page
        LoginPage(page).navigate()
        LoginPage(page).login(valid_user['username'], valid_user['password'])
        self.prod = ProductsPage(page)
        self.cart = CartPage(page)
        self.user = valid_user['username']
        self.prod.open_cart()
        if self.cart.count() > 0:
            self.cart.remove_all_items() 
        self.page.go_back()

    def test_add_single_item(self):
        self.prod.add_to_cart('sauce-labs-backpack')
        self.prod.open_cart()
        assert self.cart.count() == 1, \
            f"Failed to add {self.cart.count()} items for '{self.user}'"


    def test_add_multiple_items(self):
        for item in ['sauce-labs-backpack', 'sauce-labs-bike-light']:
            self.prod.add_to_cart(item)
        self.prod.open_cart()
        assert self.cart.count() == 2, \
            f"Failed to add {self.cart.count()} items for '{self.user}'"

    def test_remove_item(self):
        self.prod.add_to_cart('sauce-labs-backpack')
        self.prod.open_cart()
        self.cart.remove('sauce-labs-backpack')
        assert self.cart.count() == 0, \
            f"Failed to remove {self.cart.count()} items for '{self.user}'"

    def test_persist_cart_after_logout(self, valid_user):
        self.prod.add_to_cart('sauce-labs-backpack')
        self.prod.open_cart()
        self.page.reload()
        self.page.goto('https://www.saucedemo.com/')
        LoginPage(self.page).login(valid_user['username'], valid_user['password'])
        self.prod.open_cart()
        assert self.cart.count() == 1, \
            f"Persistence failed for '{self.user}'."