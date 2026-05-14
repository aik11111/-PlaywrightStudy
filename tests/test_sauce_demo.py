import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# 이제 모든 테스트가 login_user라는 '준비물'을 똑같이 나눠 가집니다.
def test_full_shopping_flow(login_user):
    page = login_user # 이미 로그인 됨
    inventory_page = InventoryPage(page)
    inventory_page.add_backpack()
    assert inventory_page.get_cart_count() == "2"

def test_product_price_sorting(login_user):
    page = login_user # 이미 로그인 됨
    inventory_page = InventoryPage(page)
    inventory_page.select_sort_option("lohi")
    # ... 나머지 정렬 코드 ...
    
    raw_prices = inventory_page.get_all_item_prices()
    clean_prices = [float(p.replace("$", "")) for p in raw_prices]

    assert clean_prices == sorted(clean_prices)
    print(f"\n정렬 확인 완료: {clean_prices}")