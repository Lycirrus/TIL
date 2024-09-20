# 모델
Django Model
- DB의 테이블을 정의하고 데이터를 조작할 수 있는 기능들을 제공
  > 테이블 구조를 설계하는 청사진이다.

### 모델 클래스 작성방법
```python
class Article(models.Model):
  title = models.CharField(max_length=10)
  content = models.TextField()
```
**생성 결과**
|id|title|content|
|:-:|:--:|:-----:|
|...|...|...|

> id 열은 Django에서 기본으로 생성한다.

> 우리는 테이블 구조를 어떻게 설계할지 고민하고 코드로 작성해야한다!

## 모델 필드
DB 테이블의 **필드**를 정의하며, 해당 필드에 저장되는 **데이터 타입**과 **제약조건**을 정의하는 필드이다.

### 구성
1. Field Types (필드 유형)
   - DB에 저장될 **데이터의 종류**를 정의
2. Field Options (필드 옵션)
   - 필드의 **동작**과 **제약 조건**을 정의

### Field Types
DB에 저장될 **데이터의 종류**를 정의한다.
> models 모듈의 클래스로 정의되어 있다.

  #### 주요 유형
  - 문자열 필드
    - CharField, TextField
  - 숫자 필드
    - IntegerField, FloatField
  - 날짜/시간 필드
    - DataField, TimeField, DateTimeField
  - 파일 필드
    - FileField, ImageField

|주요 유형|의미|비고|
|:-:|:-:|:-:|
|`CharField()`|**제한된 길이**의 문자열 저장|필드 최대 길이를 결정하는 `max_length`는 필수 옵션|
|`TextField()`|**사실상 제한이 없는 길이**의 대용량 텍스트 저장|시스템에 따라 달라짐|

### Field Options
필드의 **동작**과 **제약 조건**을 정의한다.

  #### 주요 필드 옵션
  - null
    - DB에서 NULL값을 허용할지 여부를 결정 (*기본값 : False*)
  - blank
    - form에서 빈 값을 허용할지 여부를 결정 (*기본값 : False*)
  - default
    - 필드의 기본값을 설정

### 제약 조건
특정 규칙을 강제하기 위해 테이블의 열이나 행에 적용되는 규칙이나 제한사항
> Example_
> - 숫자만 저장되도록 설정
> - 문자열 길이를 100자로 제한

## Migrations
model 클래스의 *필드 생성이나 수정, 삭제 등*의 **변경사항**을 DB에 최종 반영하는 방법

### Migrations 과정
1. model class 생성
2. migration 파일 생성
   > `app - migrations - __pycache__ - xxxx_initaial.py`로 생성
3. migrate 진행
   > `db.sqlite3`에 반영

### Migrations 핵심 명령어
- `$ python manage.py makemigrations`
  - model 클래스를 기반으로 최종 설게도 작성
- `$ python manage.py migrate`
  - 최종 설계도를 DB에 전달하여 반영

> migrate 시에 여러 파일이 Applying 되는 이유 :
>
> Django 내장 앱들에 대한 설계도 역시 존재한다.<br>
> 그래서 첫 migrate 때 내장 앱들에 대한 설계도도 migrate 된다.

### Migration 수정
1. 동일하게 models.py에 수정 내용을 추가 또는 제거한다.
2. 최종 설계도를 작성한다.
   - 1번 : 현재 대화를 유지하면서 직접 기본값을 입력하는 방법
   - 2번 : 현재 대화에서 나간 후 models.py에 기본값 관련 설정을 하는 방법<br> (*default 요소 추가*)
  
   > 수정한 내용에 대한 새로운 migration 파일이 생성된다.
   >
   > **기존 model 클래스의 수정**으로 만들어진 새로운 migration 파일은 **기존 migration 파일에 의존**하므로, 혼자서 작동할 수 없다.<br>
   > **새로운 model 클래스**로 만들었다면 이전 migration 파일에 **의존하지 않는다**.
   >
   > git commit과 유사하게 분기에 따른 확인 또는 복원 기능을 제공한다.
3. DB에 설계도를 전달하여 반영시킨다.

## Admin site
Automatic admin interface
- Django가 추가 설치 및 설정 없이 자동으로 제공하는 관리자 인터페이스
  > 데이터 확인 및 테스트 등을 진행하는데 유용하다.

### 방법
1. admin 계정 생성
   - `$ python manage.py createsuperuser`
   - e-mail 입력은 선택사항이다.
   - 비밀번호 입력 시 보안상 터미널에 출력되지 않는다.
2. DB에 생성된 admin 계정 확인
3. admin에 모델 클래스 등록
   - admin.py에 작성한 모델 클래스를 등록해야만 admin site에서 확인 가능
   ```python
   # articles/admin.py

   from django.contrib import admin
   from .models import Article

   admin.site.register(Article)
   ```
4. admin site에 로그인 후 등록된 모델 클래스 확인
5. 데이터 생성, 수정, 삭제 테스트
6. 테이블 확인

## 참고
### 데이터베이스 초기화
1. migration 파일 삭제
2. db.sqlite3 파일 삭제
> `__init__.py`, `migration 폴더`를 삭제하지 않도록 주의해야 한다.