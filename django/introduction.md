# Intro
## Web Application
웹은 기본적으로 '클라이언트-서버' 구조이다.
> 클라이언트가 서버에 요청을 하면 서버가 응답하는 구조이다.

Client : 서비스를 요청하는 주제
Server : 클라이언트의 요청에 응답하는 주체

#### 웹 페이지를 보는 기본 과정
1. 클라이언트가 페이지 주소를 입력
2. 인터넷에 연결된 어딘 가의 서버에게 '[page].html' 파일을 요청
3. 요청 받은 서버는 html 파일을 찾아 응답
4. 웹 브라우저가 전달받은 html 파일을 사람이 볼 수 있도록 해석하고 출력

### 프론트엔드와 백엔드
- 프론트엔드 : **사용자가 어플리케이션과 상호작용** 할 수 있도록 한다.
  > HTML, CSS, JavaScript, 프론트엔드 프레임워크 등

- 백엔드 : 서버측에서 동작하여 클라이언트의 **요청에 대한 처리**와 **데이터베이스와의 상호작용** 담당
  > 서버언어(Python, Java 등) 및 벡엔드 프레임워크, 데이터베이스, API, 보안 등

## Framework
### Web Framework
웹 어플리케이션을 빠르게 개발할 수 있도록 도와주는 도구
> 개발에 필요한 기본 구조, 규칙, 라이브러리 등을 제공한다.
>
> 좋은 프레임 워크는 대규모 트래픽 서비스에서도 안정적인 서비스를 제공할 수 있어야 한다.

### Django Framework
Python 기반의 대표적인 웹 프레임워크

  #### Django 사용 이유
  1. 다양성
     > 광범위한 서비스 개발에 적합
  2. 확장성
     > 대량의 데이터에 대해 빠르고 유연하게 확장할 수 있는 기능을 제공
  3. 보안
     > 보안 기능이 내장되어 있음
  4. 커뮤니티 지원
     > 개발자를 위한 지원, 문서 및 업데이트를 제공하는 커뮤니티가 활성화 되어있음

### 가상 환경
Python 애플리케이션과 그에 따른 패키지들을 격리하여 관리할 수 있는 **독립적인** 실행 환경
> 가상 환경끼리는 서로를 인지할 수 없다!

  #### 사용 시나리오
  1. 각각의 프로젝트가 하나의 패키지의 다른 버전을 사용할 때
  2. 프로젝트를 위해 충돌이 발생하는 두 개 이상의 패키지를 사용해야만 할 때

  #### 가상환경 생성 방법
  1. 가상 환경 venv 생성<br>
     `$ python -m venv [name]`<br></br>
     > 이름은 변경 가능하나 기본적으로 'venv'를 사용한다.
  2. 가상 환경 활성화<br>
     `$ source venv/Scripts/activate`<br></br>
     > mac이나 Linux의 경우<br>
     > `$ source venv/bin/activate`

     - 활성화를 하면 터미널에 `([name])` 이 출력된다.
  3. 환경에 설치된 패키지 목록 확인<br>
     `$ pip list`
  4. 설치된 패키지 목록 생성<br>
     - 현재 Python 환경에 설치된 모든 패키지와 그 버전을 텍스트 파일로 저장한다.
     `$ pip freeze > requirements.txt`<br></br>
     > 'requirements는 텍스트 파일의 이름으로 변경가능하나, 관례적으로 사용한다.

### Django 프로젝트



## Django Design Pattern
- 디자인 패턴 : 소프트웨어 설계에서 발생하는 문제를 해결하기 위한 일반적인 해결책
  > "애플리케이션 구조는 이렇게 구성하자!"

- MVC 디자인 패턴 :<br>
  `Model, View, Controller`<br>
  애플리케이션을 구조화하는 대표적인 패턴
  > "데이터" & "사용자 인터페이스" & "비즈니스 로직" 을 분리
  > - 시각적 요소와 뒤에서 실행되는 로직을 서로 영향 없이 **독립적**이고 **쉽게** 유지 보수할 수 있는 앱을 만들기 위해서이다.

- MTV 디자인 패턴 :<br>
  `Model, Template, View`<br>
  Django에서 앱을 구조화하는 패턴
  > 기존 MVC 패턴과 동일하나 단순히 명칭만을 다르게 정의한 것이다.

### 프로젝트와 앱
- 프로젝트 : 앱들의 집합
  > DB 설정, URL 연결, 전체 앱 설정 등을 관리

- 어플리케이션 : 독립적으로 작동하는 **기능 단위** 모듈
  > 각자 특정한 기능을 담당하며 다른 앱들과 하나의 프로젝트를 구성한다.
  >
  > 하나의 앱은 하나의 기능을 담당한다.

### 앱 생성
  #### 순서
  1. 앱 생성 <br>
     `$ python manage.py startapp articles`
     - 앱의 이름은 **복수형**으로 지정하는 것을 권장한다.

     > 주의사항!
     >
     > 생성된 앱은 프로젝트 폴더 안에 들어가지 않는다.<br> 따라서 프로젝트는 앱의 존재를 모른다.
     >
     >
  2. 앱 등록
     - `프로젝트 폴더` - `settings.py`의 `INSTALLED_APPS` 란에 내가 만든 앱을 추가해야 한다.

  > **앱 생성 순서는 반드시 지켜져야 한다!**

  #### 프로젝트 구조
  - `settings.py` : 프로젝트의 모든 설정을 관리
  - `urls.py` : 요청 들어오는 URL에 따라 해당하는 적절한 views를 연결
  - `__init__.py` : 해당 폴더를 패키지로 인식하도록 설정하는 파일
  - `asgi.py` : 비동기식 웹 서버와의 연결 관련 설정
  - `wsgi.py` : 웹 서버와의 연결 관련 설정
  - `manage.py` : Django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티

  #### 앱 구조
  - `admin.py` : 관리자용 페이지 설정
  - `models.py` : DB와 관련된 Model을 정의 > **MTV 패턴의 M**
  - `views.py` : HTTP 요청을 처리하고 해당 요청에 대한 **응답을 반환** > **MTV 패턴의 V**
  - `apps.py` : 앱의 정보가 작성된 곳
  - `tests.py` : 프로젝트 테스트 코드를 작성하는 곳

  > Template에 해당하는 파일은 기본적으로 만들어지지 않는다.
  >
  > Template는 사용자에게 보여지는 부분으로 프론트엔드의 영역이라 기본 생성되지는 않는다.

### Django에서 요청과 응답
`urls.py`에서 요청을 받는다.