import re
from playwright.sync_api import Page, expect

def test_sauce_demo_full_flow(page: Page):
    # 1. 접속 및 로그인
    page.goto("https://www.saucedemo.com/")
    
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()

    # 2. 장바구니 담기 (Backpack)
    # filter와 get_by_role의 파이썬 문법을 확인하세요.
    backpack_item = page.locator(".inventory_item").filter(has_text="Sauce Labs Backpack")
    backpack_item.get_by_role("button", name="Add to cart").click()

    # 3. 장바구니 배지 숫자 확인
    cart_badge = page.locator(".shopping_cart_badge")
    expect(cart_badge).to_have_text("1")

    # 4. 장바구니 이동 및 상품 확인
    page.locator(".shopping_cart_link").click()
    expect(page.locator(".inventory_item_name")).to_have_text("Sauce Labs Backpack")