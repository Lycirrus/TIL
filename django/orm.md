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



## 참고
### Field lookups



### ORM, QuerySet API를 사용하는 이유