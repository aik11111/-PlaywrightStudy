import pytest
from playwright.sync_api import Page, expect
# 1. 우리가 만든 리모컨(클래스)을 가져옵니다.
from pages.login_page import LoginPage

@pytest.mark.parametrize("username, password, expected_url", [
    ("standard_user", "secret_sauce", "inventory.html"),
    ("problem_user", "secret_sauce", "inventory.html")
])
def test_multiple_logins_with_pom(page: Page, username, password, expected_url):
    # 2. 리모컨 조립 (인스턴스화)
    # 픽스처로 받은 page를 리모컨(LoginPage)에 끼워 넣습니다.
    login_page = LoginPage(page)

    # 3. 리모컨 버튼 누르기 (동작)
    # 로케이터가 뭔지 몰라도 이름만 보고 기능을 실행합니다.
    login_page.navigate()
    login_page.login(username, password)
    
    # 4. 검증 (Assertion)
    import re
    expect(page).to_have_url(re.compile(expected_url))