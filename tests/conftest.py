import pytest
import allure
from playwright.sync_api import Page

@pytest.fixture
def login_user(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    yield page

    print("\n테스트가 완료되어 정리 중입니다.")

# 테스트가 끝날 때마다 실행되는 Pytest의 내부 갈고리(Hook) 함수입니다.
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # 1. 테스트 실행 결과를 먼저 받아옵니다.
    outcome = yield
    report = outcome.get_result()
    
    # 2. '실행(call)' 단계에서 '실패(failed)'했을 때만 동작하게 합니다.
    if report.when == 'call' and report.failed:
        # 3. 테스트 함수에서 사용한 'page' 또는 'login_user' 도구를 찾아냅니다.
        page = item.funcargs.get('page') or item.funcargs.get('login_user')
        
        if page:
            # 4. [핵심] 현재 화면을 캡처해서 알루어 보고서 데이터에 직접 박아넣습니다.
            allure.attach(
                page.screenshot(), 
                name="실패_현장_스크린샷", 
                attachment_type=allure.attachment_type.PNG
            )