from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.items = page.locator('.cart_item')
        self.checkout_btn = page.locator('[data-test="checkout"]')
        self.empty_msg = page.locator('text=empty')
        self.msg_error = page.locator('[data-test="error"]')

    def count(self) -> int:
        return self.items.count()

    def remove(self, item_id: str):
        self.page.wait_for_selector(f'button#remove-{item_id}')
        self.page.locator(f'button#remove-{item_id}').click()

    def checkout(self):
        self.checkout_btn.click()

    def get_empty_message(self) -> str:
        return self.empty_msg.text_content().strip()
    
    def get_error_message(self):
        return self.msg_error.text_content().strip()
    
    def remove_all_items(self):
        while self.page.locator('button:has-text("Remove")').count() > 0:
            self.page.locator('button:has-text("Remove")').first.click()