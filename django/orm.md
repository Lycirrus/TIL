# ORM
( Object-Relational-Mapping )
- 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 기술

> Django와 DB간에 사용하는 언어가 달라 일반적으로는 소통할 수 없다.
>
> **ORM이 이를 해석**

- '그럼 ORM 문법을 어떻게 사용할 것인가?'

## QuerySet API
ORM에서 데이터를 검색, 필터링, 정렬 및 그룹화 하는 데 사용하는 도구
- python의 모델 클래스와 인스턴스를 활용해 DB에 데이터를 **저장, 조회, 수정, 삭제**하는 것
> API로 SQL이 아닌 Python 코드로 데이터를 처리할 수 있다.

### 과정
1. QuerySet API로 조회, 추가, 삭제, 수정 등의 작업을 한다.
2. SQL로부터 그 결과를 받아온다.
  > 받아오는 방식은 두가지다.
  > - 다중 데이터인 경우 'QuerySet'
  > - 단일 데이터인 경우 'Instance'

### QuerySet API 구문
`Article.objects.all()`
> 순서대로
- Model class
- Manager
- QuerySet API

### Query
데이터베이스에 특정한 데이터를 보여 달라는 요청
- 쿼리문을 작성한다 : 원하는 데이터를 얻기 위해 DB에 요청을 보낼 코드를 작성한다.

### QuerySet
DB에서 전달받은 데이터 모음
- 순회가 가능한 데이터로 1개 이상의 데이터를 불러와 사용 가능
- 단일 객체가 반환 될 시 모델의 Instance로 반환됨

### CRUD
소프트웨어가 가지는 기본적인 데이터 처리 기능
- Create (저장)
- Read (조회)
- Update (수정)
- Delete (삭제)

## QuerySet API 실습
### Django Shell
Django 환경 안에서 실행되는 Python shell
- 입력하는 QuerySet API 구문이 Django 프로젝트에 영향을 미친다.

### Create
#### Save
`save()` : 객체를 DB에 저장하는 인스턴스 메서드

### Read
- 새로운 QuerySet을 반환
  - all() : 데이터 유무에 상관없이 QuerySet 반환
  - filter() : 조회에 조건을 걸 수 있음
- 단일 객체 반환
  - get() : 주어진 매개변수와 일치하는 객체를 반환

#### get() 특징
- 객체를 찾을 수 없으면 DoesNotExist 예외를 발생시킨다.
- 둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외를 발생시킨다.
> PK와 같이 **고유한 데이터의 조회**에서 사용해야 한다.

### Update
- 인스턴스 변수를 변경 후 save 메서드를 호출한다.
> 인스턴스 변수를 변경하는 것이므로, get()을 이용해 변경할 내용을 인스턴스로 해야 한다.

### Delete
- 삭제하려는 데이터 조회 후 delete 메서드를 호출한다.
> Django는 지워진 id 번호를 재사용하지 않는다!

## ORM with view
### 전체 게시글 조회



### 단일 게시글 조회


## HTTP 요청 메서드
- HTTP : 네트워크 상에서 데이터를 주고 받기위한 약속

- HTTP 요청 메서드
  - 데이터에 대해 수행을 원하는 작업을 나타내는 것
  - 클라이언트가 웹 서버에 특정 동작을 요청하기 위해 사용하는 표준 명령어
  > `Get`, `Post` 등이 있다.

### GET Method
서버로부터 데이터를 요청하고 받아오는 데 사용 : **조회**

  #### 특징
  1. 데이터 전송
     - URL의 쿼리 문자열을 통해 데이터를 전송
  2. 데이터 제한
     - URL 길이에 제한이 있어 대량의 데이터 전송에는 적합하지 않음
  3. 브라우저 히스토리
     - 요청 URL이 브라우저 히스토리에 남음
     - 히스토리에 쌓인 스택으로 인해 '뒤로가기' 기능을 사용할 수 있음
  4. 캐싱
     - 브라우저는 GET 요청의 응답을 로컬에 저장할 수 있음
     - 동일한 URL로 재요청할 때, 서버에 접속하지 않고 저장된 결과를 사용
     - 페이지 로딩 시간을 크게 단축

### POST Method
서버에 데이터를 제출하여 리소스를 변경하는 데 사용 : **생성, 수정, 삭제**
> DB에 요청하는 작업

  #### 특징
  1. 데이터 전송
     - HTTP Body를 통해 데이터를 전송
  2. 데이터 제한
     - 대용량 데이터 처리 가능
  3. 브라우저 히스토리
     - POST 요청은 브라우저 히스토리에 남지 않음
  4. 캐싱
     - POST 요청은 기본적으로 캐시할 수 없음
     - POST 요청이 일반적으로 서버의 상태를 변경하는 작업을 수행하기 때문

### CSRF token
- CSRF : 사이트 간 요청 위조
  > 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹 페이지를 보안에 취약하게 하거나 수정 또는 삭제 작업을 하게 만드는 공격 방법

- 진실된 사이트에서 보낸 생성 요청인지 확인하기 위한 징표이다.

## HTTP response status code
서버가 클라이언트의 요청에 대한 처리 결과를 나타낸는 3자리 숫자

### 역할
1. 클라이언트에게 요청 처리 결과를 명확히 전달
2. 문제 발생 시 디버깅에 도움
3. 웹 애플리케이션의 동작을 제어하는 데 사용

### 403 Forbidden
- 서버에 요청은 전달되었지만, **권한** 때문에 거절되었다는 것을 의미

> - 200번대 : 성공이유
> - 400번대 : 클라이언트의 잘못
> - 500번대 : 서버의 잘못

## Redirect
- 서버는 데이터 저장 후 페이지를 응답하는 것이 아닌 사용자를 적절한 기존 페이지로 보내야한다.
> 사용자를 보낸다 -> 사용자가 GET 요청을 한번 더 보내도록 해야한다.

- `redirect()`
  - 클라이언트가 인자에 작성된 주소로 다시 요청을 보내도록 하는 함수

## Delete
```python
def delete(request, pk):
  # 삭제할 게시글을 조회
  article = Article.objects.get(pk=pk)
  # 조회한 게시글 삭제
  article.delete()
  return redirect('articles:index')
```

## Update
### edit
```python
def edit(request, pk):
  article = Article.objects.get(pk=pk)
  context = {
    'article': article,
  }
  return render(request, 'articles/edit.html', context)
```

### update
```python
def update(request, pk):
  # 1. 수정할 게시글 조회
  article = Article.objects.get(pk=pk)
  # 2. 사용자가 입력한 새로운 데이터 추출 및 저장
  article.title = request.POST.get('title')
  article.content = request.POST.get('content')
  # 3. 최종 저장
  article.save()
  return redirect('articles:detail', article.pk)
```