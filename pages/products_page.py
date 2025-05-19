from playwright.sync_api import Page

class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        self.sort_dropdown = page.locator('.product_sort_container')
        self.cart_icon = page.locator('.shopping_cart_link')
        self.items = page.locator('.inventory_item')

    def add_to_cart(self, item_id: str):
        self.page.wait_for_selector(f'button#add-to-cart-{item_id}', state='visible')
        self.page.locator(f'button#add-to-cart-{item_id}').click()

    def remove_from_cart(self, item_id: str):
        self.page.wait_for_selector(f'button#remove-{item_id}', state='visible')
        self.page.locator(f'button#remove-{item_id}').click()

    def sort_low_to_high(self):
        self.sort_dropdown.select_option('lohi')

    def sort_high_to_low(self):
        self.sort_dropdown.select_option('hilo')

    def open_cart(self):
        self.cart_icon.click()

    def get_prices(self) -> list:
        return [float(p.text_content().strip().replace('$', ''))
                for p in self.page.locator('.inventory_item_price').all()]

    def view_details(self, item_id: str) -> dict:
        self.page.wait_for_selector(f'text={item_id}')
        self.page.locator(f'text={item_id}').click()
        name = self.page.locator('.inventory_details_name').text_content().strip()
        price = self.page.locator('.inventory_details_price').text_content().strip()
        desc = self.page.locator('.inventory_details_desc').text_content().strip()
        self.page.go_back()
        return {"name": name, "price": price, "description": desc}