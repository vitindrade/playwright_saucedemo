import json
import pytest
from playwright.sync_api import sync_playwright

with open('fixtures/users.json', 'r') as f:
    USERS = json.load(f)

ENV_VALID_KEYS = ['standard_user', 'problem_user', 'performance_glitch_user', 'error_user', 'visual_user']

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as pw:
        yield pw

@pytest.fixture(scope="session")
def browser(playwright, browser_name):
    browser = getattr(playwright, browser_name).launch(
        headless=False,  # vizualizacao dos testes
        slow_mo=100      # tempo de execucao da janela
    )
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    page.set_default_timeout(20000)
    yield page

@pytest.fixture(scope='function')
def users():
    return USERS

@pytest.fixture(params=ENV_VALID_KEYS, ids=ENV_VALID_KEYS)
def valid_user(request):
    return USERS[request.param]