import pytest
from playwright.sync_api import Playwright, APIRequestContext, expect

# 이번엔 헤더 없이도 잘 되는지 확인하기 위해 기본으로 작성합니다.
@pytest.fixture(scope="session")
def api_request_context(playwright: Playwright):
    # base_url을 JSONPlaceholder로 바꿉니다.
    request_context = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )
    yield request_context
    request_context.dispose()

def test_get_single_post(api_request_context: APIRequestContext):
    # 1. 1번 게시글 정보를 가져옵니다.
    response = api_request_context.get("/posts/1")

    # 2. 상태 코드 200(성공)인지 확인
    assert response.status == 200
    
    # 3. 데이터 확인
    post_data = response.json()
    print(f"\n게시글 제목: {post_data['title']}")
    
    # 1번 게시글의 userId가 1인지 확인 (데이터 검증)
    assert post_data['userId'] == 1
    # 게시글 ID가 1인지 확인
    assert post_data['id'] == 1

def test_create_post(api_request_context: APIRequestContext):
    new_post_data = {
        "title": "선생님과 함께하는 플레이라이트",
        "body": "직접 타이핑하니 머리에 쏙쏙 들어오네요!",
        "userid": 1
    }

    response = api_request_context.post("/posts", data=new_post_data)

    assert response.status == 201

    result = response.json()
    print(f"\n생성된 데이터: {result}")

    assert result["title"] == new_post_data["title"]
    assert "id" in result

def test_update_post(api_request_context: APIRequestContext):
    updated_data = {
        "id": 1,
        "title": "제목을 수정했습니다",
        "body": "내용도 바뀌었을까요?",
        "userid": 1
    }

    response = api_request_context.put("/posts/1", data=updated_data)

    assert response.status == 200

    result = response.json()
    assert result["title"] == "제목을 수정했습니다"
    print(f"\n수정 확인: {result['title']}")

def test_delete_post(api_request_context: APIRequestContext):
    response = api_request_context.delete("/posts/1")

    assert response.status == 200

    print("\n삭제 요청 성공")