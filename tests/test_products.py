import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage

class TestProductsSorting:
    @pytest.fixture(autouse=True)
    def login(self, page, valid_user):
        LoginPage(page).navigate()
        LoginPage(page).login(valid_user['username'], valid_user['password'])
        self.products = ProductsPage(page)
        self.user = valid_user['username']

    @pytest.mark.parametrize('sort_fn,reverse', [
        ('sort_low_to_high', False),
        ('sort_high_to_low', True)])
    def test_sort_by_price(self, sort_fn, reverse):
        getattr(self.products, sort_fn)()
        prices = self.products.get_prices()
        assert prices == sorted(prices, reverse=reverse), \
            f"Sorting failed for '{self.user}'. Retrieved values: {prices}"


    def test_view_product_details(self):
        details = self.products.view_details('Sauce Labs Backpack')
        assert 'backpack' in details['name'].lower(), \
            f"Incorrect name in details for '{self.user}': {details['name']}"
        assert details['price'].startswith('$'), \
            f"Price without $ para '{self.user}': {details['price']}"
        assert len(details['description']) > 0, \
            f"Empty description for '{self.user}'"