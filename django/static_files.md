# Django files
## Static files
- 서버 측에서 변경되지 않고 고정적으로 제공되는 파일
  > 이미지, JS, CSS 파일

### 웹 서버와 정적 파일
웹 서버는 요청 받은 URL로 서버에 존재하는 정적 자원을 제공한다.
> 따라서 정적 파일을 제공하기 위한 경로의 URL이 존재해야 한다.

### static file 사용방법
- static 폴더에 이미지가 있다면, 아래와 같이 html을 작성한다.
```html
{% load static %}

<img src="{% static 'articles/sample-1.png' %}" alt=".">
```
- static files 경로는 DTL의 static tag를 사용해야 한다.
- load tag를 사용해 import 후 사용할 수 있다.

### static file 주의사항
1. extends는 항상 html 맨 위에 위치해야 한다.<br>(load가 맨 위에 되어선 안된다.)
2. load static은 지정한 파일(html)에서만 적용된다.<br>(base.html에서 load하더라도 하위 html들에 적용되지 않는다.)

### static url
기본 경로 및 추가 경로에 위치한 정적 파일을 참조하기 위한 URL
> 실제 파일이나 디렉토리 경로가 아니며, URL로만 존재한다.

  #### 예시
  `http://127.0.0.1:8000/static/...`
  - URL + Static_URL + 정적파일 경로로 이루어진다.
  ```python
  # settings.py

  STATIC_URL = 'static/'
  ## 기본 Static_URL이다.
  ```

### Static files 추가 경로
STATICFILES_DIRS에 문자열 값으로 추가 경로 설정

  #### STATICFILES_DIRS
  정적 파일의 기본 경로 외에 추가적인 경로 목록을 정의하는 리스트
  - settings.py에서 아래와 같이 추가한다.
    ```python
    # settings.py

    STATICFILES_DIRS = [
      BASE_DIR / 'static',
    ]
    ```
  - 최상위 폴더에 'static' 폴더를 생성하여 사용할 파일을 넣는다.
  - 이후에는 일반적인 Static files 사용법과 동일하다.

## Media files
- 사용자가 웹에서 업로드하는 정적 파일

### 이미지 업로드
- `ImageField()` : 이미지 업로드에 사용하는 모델 필드
- 근본적으로 문자열 필드이다.
- 실제 이미지가 아닌 이미지가 위치한 경로가 저장된다.
  > 이미지 객체가 직접 DB에 저장되는 것이 아닌 **이미지 파일의 경로** 문자열이 저장된다.

### 준비 사항
1. 'settings.py'에 **MEDIA_ROOT**, **MEDIA_URL** 설정
2. 작성한 MEDIA_ROOT와 MEDIA_URL에 대한 URL 지정

### MEDIA_ROOT
- 미디어 파일들이 위치하는 디렉토리의 절대 경로

### MEDIA_URL
- MEDIA_ROOT에서 제공되는 미디어 파일에 대한 주소를 생성

##### 같은 이름의 이미지 등록 시
Django가 새로 들어온 같은 이름 이미지의 뒤에 임의의 해쉬 값을 추가한다.


## 참고