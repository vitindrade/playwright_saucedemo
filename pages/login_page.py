from playwright.sync_api import Page

class LoginPage:
    URL = 'https://www.saucedemo.com/'

    def __init__(self, page: Page):
        self.page = page
        self.user_input = page.locator('#user-name')
        self.pass_input = page.locator('#password')
        self.btn_login = page.locator('#login-button')
        self.err_msg = page.locator('[data-test="error"]')

    def navigate(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.user_input.fill(username)
        self.pass_input.fill(password)
        self.btn_login.click()

    def get_error(self) -> str:
        return self.err_msg.text_content().strip()