# 1. 베이스 이미지 선택 (파이썬과 플레이라이트가 이미 깔려있는 상자)
FROM mcr.microsoft.com/playwright/python:v1.59.0-jammy

# 2. 작업 폴더 설정 (상자 내부의 위치)
WORKDIR /app

# 3. 필요한 파일들 복사 (우리 장바구니 목록 복사)
COPY requirements.txt .

# 4. 라이브러리 설치 (상자 안에서 pip 실행)
RUN pip install --no-cache-dir -r requirements.txt

# 5. 소스 코드 전체 복사
COPY . .

# 6. 실행 명령 (도커가 켜지자마자 실행할 명령어)
# --headed를 빼는 이유는 도커 안에는 모니터(화면)가 없기 때문입니다!
CMD ["pytest", "-s"]