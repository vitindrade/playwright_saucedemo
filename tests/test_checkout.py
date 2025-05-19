import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

class TestCheckout:
    @pytest.fixture(autouse=True)
    def setup(self, page, valid_user):
        self.page = page
        LoginPage(page).navigate()
        LoginPage(page).login(valid_user['username'], valid_user['password'])
        self.prod = ProductsPage(page)
        self.cart = CartPage(page)
        self.user = valid_user['username']

    def test_checkout_empty_cart(self):
        self.prod.open_cart()
        self.cart.checkout()
        checkout_page = CheckoutPage(self.page)
        assert not checkout_page.is_loaded(), \
            f"Should not reach checkout page with empty cart for '{self.user}'"

    def test_complete_purchase_success(self):
        self.prod.add_to_cart('sauce-labs-backpack')
        self.prod.open_cart()
        self.cart.checkout()
        co = CheckoutPage(self.page)
        co.fill_info('Usuario', 'Teste', '12345')
        msg = co.finish()
        assert co.get_success_message() == "Thank you for your order!", \
        f"Purchase not completed successfully for '{self.user}'"