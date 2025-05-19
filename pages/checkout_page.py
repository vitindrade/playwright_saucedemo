from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.first = page.locator('#first-name')
        self.last = page.locator('#last-name')
        self.postal = page.locator('#postal-code')
        self.continue_btn = page.locator('[data-test="continue"]')
        self.finish_btn = page.locator('[data-test="finish"]')
        self.msg_complete = page.locator('.complete-header')
        self.msg_error = page.locator('[data-test="error"]')


    def fill_info(self, first: str, last: str, postal: str):
        self.first.fill(first)
        self.last.fill(last)
        self.postal.fill(postal)
        self.continue_btn.click()

    def finish(self):
        self.finish_btn.click()
        self.page.wait_for_url('**/checkout-complete.html')

    def is_loaded(self, t=1000):
        try:
            self.first.wait_for(timeout=t)
            return True
        except:
            return False

    def get_success_message(self) -> str:
        self.msg_complete.wait_for(state='visible')
        return self.msg_complete.text_content().strip()
    
    def get_error_message(self):
        return self.msg_error.text_content().strip()