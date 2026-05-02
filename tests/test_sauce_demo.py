import pytest
from playwright.sync_api import Page, expect
# 1. 우리가 만든 리모컨(클래스)을 가져옵니다.
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_full_shopping_flow(page: Page):
    # 1. 리모컨들 준비
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    # 2. 로그인 진행 (첫 번째 리모컨 사용)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # 3. 상품 추가 (두 번째 리모컨 사용)
    inventory_page.add_backpack()

    # 4. 검증 (게터 함수로 받은 값이 '1'인지 확인)
    assert inventory_page.get_cart_count() == "1"
    print("\n장바구니에 물건이 1개 담긴 것을 확인했습니다!")