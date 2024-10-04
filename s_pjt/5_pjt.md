# 웹 크롤링
## 웹 크롤링 프로세스
1. 웹 페이지 다운로드
   - 해당 웹 페이지의 HTML, CSS, JavaScript 등의 코드를 가져오는 단계
2. 페이지 파싱
   - 다운로드 받은 코드를 분석하고 필요한 데이터를 추출하는 단계
3. 링크 추출 및 다른 페이지 탐색
   - 다른 링크를 추출하고, 다음 단계로 이동하여 원하는 데이터를 추출하는 단계
4. 데이터 추출 및 저장
   - 분석 및 시각화에 사용하기 위해 데이터를 처리하고 저장하는 단계

## 필수 라이브러리
- `requests` : HTTP 요청을 보내고 응답을 받을 수 있는 모듈
- `BeautifulSoup` : HTML 문서에서 원하는 데이터를 추출하는 데 사용되는 파이썬 라이브러리
- `Selenium` : 웹 애플리케이션을 테스트하고 자동화하기 위한 파이썬 라이브러리
  - 웹 페이지의 동적인 컨텐츠를 가져오기 위해 사용한다.

# Selenium 사용 이유
- `requests`는 동적인 부분을 다운로드 할 수 없다.
  - 정적 데이터 : 서버가 이미 가지고 있는 데이터
- `selenium`은 동적 컨텐츠를 받을 수 있다.


# Project 5주차
이번주는 지난 주에 진행했던 CRUD가 들어간 영화 페이지에 계정 관련 기능(로그인, 회원가입 등)을 추가하는 프로젝트로 진행하였다.

## 사진 올리기
사진을 올리는 기능을 구현하기 위해 MEDIA file을 이용하였다. 그러기 위해 아래와 같은 내용을 추가하였다.
- 'settings.py'에 `MEDIA_ROOT`와 `MEDIA_URL`을 추가
- 'views.py'의 생성(저장)과 수정 함수의 폼에 `request.FILES` 요소 입력
- html form에서 `인코딩 타입`(*multipart/form-data*) 추가

그러나 이미지가 등록되지 않는 문제가 발생했다. 그리고 한 가지를 빠뜨렸음을 발견했다.
<br>
'urls.py'에 media 이미지 파일에 대한 경로를 지정을 해주지 않았다.
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
위와 같은 내용을 누락시켜서, 깨진 이미지만 출력이 되었던 것이었다.