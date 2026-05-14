import pytest 
from playwright.sync_api import Page, expect
import re


def test_javascript_alerts(page: Page):
    # 1. 해당 연습 페이지로 이동
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    # 2. 알림창 감시자(Listener) 설정
    # 알림창이 뜨는 순간 바로 '확인'을 누르라고 미리 시켜둡니다.
    # lambda d: d.accept() -> "들어온 창(d)을 승인(accept)해라"
    page.on("dialog", lambda dialog: dialog.dismiss())

    # 3. 알림창을 띄우는 버튼 클릭
    # "Click for JS Alert"라는 글자가 써진 버튼을 찾습니다.
    page.get_by_role("button", name="Click for JS Confirm").click()

    # 4. 결과 확인
    # 버튼을 누르면 아래에 "You successfully clicked an alert"라는 결과 글자가 뜹니다.
    result = page.locator("#result")
    expect(result).to_have_text("You clicked: Cancel")

def test_multiple_windows(page: Page):
    # 1. 연습 페이지로 이동
    page.goto("https://the-internet.herokuapp.com/windows")

    # 2. 새 창 대기 및 낚아채기 (핵심 문법)
    # "이제부터 새 창이 뜰 거야. 그 정보를 popup_info라고 부를게!"
    with page.expect_popup() as popup_info:
        # 이 안에서 클릭을 해야 새 창을 잡을 수 있습니다.
        page.get_by_text("Click Here").click()

    # 3. 새로 뜬 창을 변수에 담기
    # popup_info 안에 담긴 진짜 페이지(value)를 꺼냅니다.
    new_page = popup_info.value

    # 4. 새 창에서 검증하기
    # 주소창에 'new'라는 글자가 들어있는지 확인
    expect(new_page).to_have_url(re.compile("new"))
    
    # 새 창에 있는 제목이 "New Window"인지 확인
    expect(new_page.get_by_role("heading")).to_have_text("New Window")
    
    # 5. (선택) 원래 창으로 돌아와서 확인하기
    expect(page.get_by_role("heading")).to_have_text("Opening a new window")

@pytest.mark.skip(reason="외부 사이트 사용량 제한으로 인한 에디터 잠금 문제")
def test_iframe_handling(page: Page):
    page.goto("https://the-internet.herokuapp.com/iframe")

    # 1. 아이프레임 조준
    editor_frame = page.frame_locator("#mce_0_ifr")
    editor_body = editor_frame.locator("#tinymce")

    # 2. [치트키] 강제로 편집 가능 상태로 변경 (JavaScript 주입)
    # el(요소)의 contentEditable 속성을 'true'로 강제 세팅합니다.
    editor_body.evaluate("el => el.contentEditable = 'true'")

    # 3. 이제 잠금이 풀렸으니 지우고 쓰기
    editor_body.clear()
    editor_body.fill("Hello, Playwright Iframe!")

    # 4. 검증
    expect(editor_body).to_have_text("Hello, Playwright Iframe!")