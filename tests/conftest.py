import pytest
from playwright.sync_api import Page

@pytest.fixture
def login_user(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    yield page

    print("\n테스트가 완료되어 정리 중입니다.")