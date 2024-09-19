# 템플릿과 URL
## 템플릿 시스템
- Django Template system
  - 데이터 **표현**을 제어하면서, **표현**과 관련된 부분을 담당

- Django Template Language
  - Template에서 조건, 반복, 변수 등의 프로그래밍적 기능을 제공하는 시스템

- DTL Syntax
  1. Variable
  2. Filters
  3. Tags
  4. Comments
  
  #### Variable
  - render 함수의 세번째 인자로 딕셔너리 사용
  - 딕셔너리 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨
  - dot('.')을 사용하여 변수 속성에 접근할 수 있음

  #### Filters
  - 표시한 변수를 수정할 때 사용 (`변수 + | + 필터`)
  - 연결이 가능하며 일부 필터는 인자를 받음
  - 약 60개의 built-in template filters를 제공

  #### Tags
  - 반복 또는 논리를 수행하여 제어 흐름을 만듦
  - 일부 태그는 시작과 종료 태그가 필요
  - 약 24개의 built-in template tags를 제공

  #### Comments
  - DTL에서의 주석 역할

## 템플릿 상속
**페이지의 공통요소를 포함**하고,<br> **하위 템플릿이 재정의 할 수 있는 공간**을 정의하는<br> 기본 'skeleton' 템플릿을 작성하여 상속 구조를 구축
- 공통요소는 'base.html'에 입력
- 재정의 할 수 있는 공간은 'block'으로 설정
- 하위 템플릿에서는 'extends'를 이용하여 상속 받음

### 태그 종류
- `extends` tag
  - 하위 템플릿이 상위 템플릿을 확장한다는 것을 알림
  > 반드시 하위 템플릿 최상단에 작성되어야 함
  >
  > 그러므로 2개 이상 사용 불가(하나의 템플릿만 상속받을 수 있음)
- `block` tag
  - 하위 템플릿에서 재정의 할 수 있는 블록을 정의
  > 상위 템플릿에 작성하여 하위 템플릿이 작성되는 공간을 지정함

## HTML 폼
HTML 'form'은 HTTP 요청을 서버에 보내는 가장 편리한 방법

- `form` element
  - 사용자로부터 할당된 데이터를 서버로 전송
  > 웹에서 사용자 정보를 입력하는 여러 방식 *(text, password, checkbox 등)* 을 제공한다.

- `input` element
  - 사용자의 데이터를 입력받을 수 있는 요소
  - `name` 속성을 통해 입력 데이터의 key를 지정해 주어야 한다.

### Query String Parameters
- 사용자의 입력 데이터를 URL 주소에 파라미터로 서버에 보내는 방법
- '&'로 연결된 key=value 쌍으로 구성되며, 기본 URL과는 '?'로 구분된다.

### form 활용


## Django URLs
URL dispatcher
- URL 패턴을 정의하고, 해당 패턴이 일치하는 요청을 처리할 view 함수를 연결

Variable Routing
- URL 일부에 변수를 포함시키는 것
  - `<path_converter:variable_name>`
  #### 예시
  ```django
  path('articles/<int:num>/', views.detail)
  ```


App URL mapping
- 각 앱에 URL을 정의하는 것


## URL 이름 지정




## URL 이름 공간




## 참고