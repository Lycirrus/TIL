# DRF
## API
두 소프트웨어가 서로 통신할 수 있도록 하는 메커니즘
- 클라이언트 <-> 서버처럼 서로 다른 프로그램에서 요청과 응답을 받을 수 있도록 만든 체계

### 역할
- 복잡한 코드를 추상화하여 대신 사용할 수 있는 몇 가지 더 쉬운 구문을 제공

### Web API
- 웹 서버 또는 웹 브라우저를 위한 API
- 웹 개발에서 여러 Open API들을 사용

## REST API
### REST
- `Representational State Transfer`
- API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론

  #### RESTful API
  - RESTful하다 : REST 원리를 따르는 시스템
  - **자원을 정의**하고 **자원에 대한 주소를 지정**하는 전반적인 방법 서술

### REST API
- REST 설계 디자인 약속을 지켜 구현한 API

  #### 자원 정의 및 주소 지정
  1. 자원 **식별**
    - URI
  2. 자원 **행위**
    - HTTP Methods
  3. 자원 **표현**
    - JSON 데이터 (표현 결과물)

### 자원 식별
- `URI` (통합 자원 식별자) : 인터넷에서 자원을 식별하는 문자열
  > 가장 일반적인 URI => `URL`

- `URL` : 웹에서 주어진 자원의 주소
  > 네트워크 상에 자원이 어디 있는지를 알려주기 위한 약속

  #### URL의 구조
  `https://www.test.com:80/...?...#...`
  - Scheme (또는 Protocol)
    - `https`에 해당
    - 브라우저가 리소스를 요청하는데 사용해야 하는 규약
    - URL의 첫 부분은 브라우저가 사용하는 규약을 표현
    - 기본적인 웹은 http(s) 요구
      - `mailto` : 메일
      - `ftp` : 파일 전송
  - Domain Name
    - `www...`에 해당
    - 요청 중인 웹 서버
    - 어떤 웹 서버가 요구되는지 직접 가리킴
    - IP 주소도 사용가능하나 암기의 어려움으로 Domain Name을 사용
  - Port
    - `80`에 해당
    - 웹 서버 자원에 접근하기 위해 사용되는 기술적인 문(Gate)
    - HTTP 프로토콜의 표준 포트
      - `HTTP` - 80
      - `HTTPS` - 443
    - 표준 포트만 작성 시 생략 가능
  - path
    - `/...`에 해당
    - 웹 서버 자원의 경로
    - 초기에는 물리적 위치를 나타냈으나, 현재는 실제 위치가 아닌 추상화된 형태의 구조를 표현
  - Parameters
    - `?...`에 해당
    - '&' 기호로 구분되는 key-value 쌍 목록
    - 서버는 자원을 응답하기 전에 파라미터를 사용하여 추가 작업을 수행할 수 있음
  - Anchor
    - `#...`에 해당
    - 일종의 북마크
    - 브라우저 해당 지점에 있는 콘텐츠를 표시
    - '#' 이후 부분은 서버에 전송하지 않음
    - 브라우저를 해당 지점으로 이동할 수 있도록 함

### 자원 행위
- `HTTP Request Methods` : 자원에 대한 수행하고자 하는 동작을 정의
  > HTTP verbs 라고도 한다.

  #### 대표 HTTP Request Methods
  1. `GET`
    - 서버에 자원 표현을 요청
    - GET을 사용하는 요청은 데이터만 검색해야 함
  2. `POST`
    - 데이터를 지정된 리소스에 제출
    - 서버의 상태를 변경
  3. `PUT`
    - 요청한 주소의 자원을 수정
  4. `DELETE`
    - 지정된 자원을 삭제

#### HTTP response status codes
- 특정 HTTP 요청이 성공적으로 완료되었는지 여부를 나타내는 것

|응답 그룹|번호|
|:------:|:--:|
|Informational responses|`100 ~ 199`|
|Successful responses|`200 ~ 299`|
|Redirection messages|`300 ~ 399`|
|Client error responses|`400 ~ 499`|
|Server error responses|`500 ~ 599`|

### 자원 표현
- 서버는 사용자에게 html 뿐만 아니라 JSON 등 다양한 타입으로 응답이 가능함
- REST API는 JSON 타입으로 응답하는 것을 권장

#### 응답 데이터 타입 변화
1. html만을 응답하는 서버
2. JSON 데이터를 응답하는 REST API 서버로 변환
3. Django가 더 이상 Template 부분에 대한 역할을 담당하지 않음
   > 프론트엔드와 백엔드가 분리되어 구성
4. Django를 이용해 RESTful API 서버 구축

## DRF with Single Model
### DRF
`Django REST framework`
- Django에서 RESTful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리

### Serializer
- `직렬화` : 여러 시스템에서 활용하기 위해 데이터 구조나 객체 상태를 재구성할 수 있는 포맷으로 변환하는 과정
- `Serializer` : 직렬화를 진행한 Serialized Data를 반환해주는 클래스
- `ModelSerializer` : Django 모델과 연결된 Serializer 클래스
  > 일반 Serializer과 달리 사용자 입력 데이터를 받아 **자동으로 모델 필드에 맞추어** Serializion을 진행

## CRUD with ModelSerializer

||`GET`|`POST`|`PUT`|`DELETE`|
|:-:|:-:|:---:|:---:|:------:|
|`전체`|전체 글 조회|글 작성|||
|`게시글`|N번 글 조회||N번 글 수정|N번 글 삭제|

### GET method - 조회
- 게시글 데이터 목록 조회
  ```python
  # serializers.py

  from rest_framework import serializers
  from .models import Article

  class ArticleListSerializer(seriallizers.ModelSerializer):
    class Meta:
      model = Article
      fields = ('id', 'title', 'content',)
  ```
- url 및 view 함수 작성
  ```python
  # urls.py

  ...
  urlpatterns = [
    path('articles/', views.article_list),
  ]
  ```
  ```python
  # views.py
  from rest_framework.response import Response
  from rest_framework.decorators import api_view

  from .models import Article
  from .serializers import ArticleListSerializer

  @api_view(['GET'])
  def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    # many : Serialize 대상이 QuerySet인 경우 입력
    return Response(serializer.data)
    # data : Serialized data 객체에서 실제 데이터 추출
  ```

  #### render와 Response
  - render : 데이터를 HTML에 출력되도록 페이지와 함께 응답
  - Response : JSON 데이터로 serialization하여 페이지 없이 응답

  #### api_view
  - DRF view 함수에서 **필수로 작성**되는 데코레이터
  - view 함수 실행 전 HTTP 메서드 확인
  - 기본적으로 GET 메서드마나 허용
  - DRF view 함수가 응답해야 하는 HTTP 메서드 목록을 작성
    > 명시되지 않은 HTTP 메서드에 대해서는 '405 Method Not Allowed'로 응답

### POST method - 생성
- 데이터 생성이 성공했을 경우 `201 Created` 응답
- 데이터 생성이 실패했을 경우 `400 Bad request` 응답
  
<br>

- 게시글 작성 (조회에 추가)
  ```python
  # views.py

  from rest_framework import status

  @api_view(['GET', 'POST'])
  def article_list(request):
    # 조회 부분은 GET일 경우에만 작동
    if request.method == 'GET':
      articles = Article.objects.all()
      serializer = ArticleListSerializer(articles, many=True)
      return Response(serializer.data)

    # 생성 부분은 POST일 경우 작동
    elif request.method == 'POST':
      serializer = ArticleSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        # 생성 성공 시 201 응답
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      # 실패했다면 400 응답
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

### DELETE method - 삭제
- 게시글 데이터 삭제
  ```python
  # views.py

  @api_view(['GET', 'DELETE'])
  def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    # 단순 게시글 조회
    if request.method == 'GET':
      serializer = ArticleSerializer(article)
      # queryset이 아니기에 many는 사용하지 않는다.
      return Response(serializer.data)

    # 게시글 삭제
    elif request.method == 'DELETE':
      article.delete()
      # 요청한 데이터 삭제 작업이 성공했을 경우 204 No Content 응답
      return Response(status=status.HTTP_204_NO_CONTENT)

### PUT method - 수정
- 게시글 데이터 수정
  ```python
  # views.py

  @api_view(['GET', 'DELETE', 'PUT'])
  def article_detail(request, article_pk):
    # 조회와 삭제 부분 변동 없음
    ...

    # 수정 부분
    elif request.method == 'PUT':
      serializer = AritcleSerializer(article, data=request.data, partial=True)
      # partial : 부분 업데이트를 허용하기 위한 인자
      # partial이 False이면, title만 수정해도 전체가 요청 시에 함께 전송해야 한다.
      # True여야 수정하지 않은 데이터는 전송되지 않고, 미전송 시에 유효성 검사에서도 오류가 발생하지 않는다.

      if serializer.is_valid():
        serializer.save()
        # 수정 성공
        return Response(serializer.data)
      # 수정에 실패하면 400 Bad Request 응답
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

## raise_exception
- `is_valid()`의 선택 인자
- 유효성 검사를 통과하지 못할 경우 ValidationError 예외를 발생시킴
- 기본 제공 예외 처리기에 의해 자동으로 처리되어 기본적으로 400 응답을 반환
- 따라서, 생성과 수정 마지막에 들어갔던 `return Response(serializer.errors, status=status.HTTP_400_BAD_REQEUST)`를 생략 가능해짐

## DRF with N:1 Relation

|URL|`GET`|`POST`|`PUT`|`DELETE`|
|:-:|:---:|:----:|:---:|:------:|
|`comments`|댓글 목록 조회||||
|`comments/1/`|단일 댓글 조회||단일 댓글 수정|단일 댓글 삭제|
|`articles/1/comments`||댓글 생성|||

> 댓글은 게시글에 종속되기에 생성시에 개별적인 pk가 필요하다.

### GET
1. 댓글 목록 조회를 위한 CommentSerializer 정의
   ```python
   # serializers.py

   from .models import Article, Comment

   class CommentSerializer(serializers.ModelSerializer):
    class Meta:
      model = Comment
      fields = '__all__'
   ```
2. url 작성
   ```python
   # urls.py

   urlpatterns = [
    ...,
    path('comments/', views.comment_list),
   ]
   ```
3. view 함수 작성
   ```python
   # views.py

   from .models import Article, Comment
   from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer

   @api_view(['GET'])
   def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)
   ```

### POST
1. url 및 view 함수 작성
   ```python
   # urls.py

   urlpatterns = [
    ...,
    path('articles/<int:article_pk>/comments/', views.comment_create),
   ]
   ```
   ```python
   # views.py

   @api_view(['POST'])
   def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      # serializer 인스턴스의 save() 메서드는 특정 serializer 인스턴스를 저장하는 과정에서 추가 데이터를 받을 수 있다.
      # 외래키를 받도록 설정한다.
      # `article=article`
      serializer.save(article=article)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
   ```
2. 읽기 전용 필드로 설정
   - 외래키인 article field도 사용자로부터 입력 받도록 설정되어 있기 때문에, 서버측에서는 입력이 누락되었다고 판단
   - 외래키 필드를 읽기 전용 필드로 설정하여 유효성 검사 목록에서 제외
   ```python
   # serializer.py

   class CommentSerializer(...):
    class Meta:
      ...
      read_only_fields = ('article',)
   ```

### DELETE와 PUT
1. 단일 댓글 삭제 및 수정을 위한 view 함수 작성
   ```python
   # views.py
   
   @api_view(['GET', 'DELETE', 'PUT'])
   def comment_detail(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'GET':
      ...

    elif reqeust.method == 'DELETE':
      comment.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
      serializer = CommentSerializer(comment, data=request.data)
      if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
   ```

### 응답 데이터 재구성
> 댓글 목록을 받을 때, pk뿐만 아니라 참조 게시글의 제목까지 출력하기 위함이다.

- Comment Serializer 클래스 내부에서 추가 선언 가능
  ```python
  # serializers.py

  class CommentSerializer(...):

    class ArticleTitleSerializer(...):
      class Meta:
        model = Article
        fields = ('title',)

    article = ArticleTitleSerializer(read_only=True)

    class Meta:
      model = Comment
      fields = '__all__'
   ```

## 역참조 데이터 구성
- 두 가지 사항에 대한 데이터 재구성하기
  - 단일 게시글 조회 시 **해당 게시글에 작성된 댓글 목록**도 함께 붙여서 응답
  - 단일 게시글 조회 시 **해당 게시글에 작성된 댓글 개수**도 함께 붙여서 응답

### 단일 게시글의 댓글 목록
- Nested relationships
  - 역참조 매니저 활용
  ```python
  # serializers.py

  class ArticleSerializer(...):
    class CommentDetailSerializer(...):
      class Meta:
        model = Comment
        fields = ('id', 'content',)

    comment_set = CommentDetailSerializer(many=True, read_only=True)

    class Meta:
      model = Article
      fields = '__all__'
   ```

### 단일 게시글의 댓글 개수
- 댓글 개수에 해당하는 새로운 필드 생성
  ```python
  # serializers.py

  class ArticleSerializer(...):
    ...
    comment_count = serializers.    IntegerField(source='comment_set.count', read_only=True)
    # source : 필드를 채우는 데 사용할 속성의 이름
    # 점 표기법으로 속성을 탐색할 수 있다.

    class Meta:
      ...
    # 특정 필드를 오버라이드하거나 추가한 경우 read_only_fields는 동작하지 않는다.
    # 따라서 새로운 필드에 read_only 키워드 인자를 작성해야 한다.
  ```

### 읽기 전용 필드
- 아래와 같은 경우에 사용
  - 사용자에게 입력으로는 받지 않지만 제공은 해야하는 경우
  - 새로운 필드 값을 만들어 제공해야 하는 경우

#### 특징
- 유효성 검사에서 제외
- 생성 로직에서만 사용이 국한되는 것은 아님

#### read_only_fields 속성과 read_only 인자
- read_only_fields
  - 기존 외래키 필드 값을 **그대로 응답 데이터에 제공**하기 위해 지정하는 경우
- read_only
  - 외래키 필드 값의 결과를 **다른 값으로 덮어쓰는** 경우
  - **새로운 응답 데이터 값을 제공**하는 경우

## API 문서화
- `OpenAPI Specification` : RESTful API를 설명하고 시각화하는 표준화된 방법
  > API에 대한 세부사항을 기술할 수 있는 공식 표준

### 문서화 활용
- `drf-spectacular` 라이브러리 : DRF를 위한 OpenAPI 3.0 구조 생성을 도와주는 라이브러리
  - 설치 후 settings.py의 'INSTALLED_APPS'에 추가
  - 관련 설정 코드 입력
    ```python
    # settings.py

    REST_FRAMEWORK = {
      'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    }
    ```
  - 페이지 제공을 위한 url 작성
    ```python
    # urls.py

    from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

    urlpatterns = [
      ...,
      path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
      path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
      path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    ]
    ```

### 설계 우선 접근법
- OpenAPI Specification의 핵심 이점
- API를 먼저 설계하고 명세서를 작성한 후, 이를 기반으로 코드를 구현하는 방식
- API의 일관성을 유지하고, API 사용자는 더 쉽게 API를 이해하고 사용할 수 있음
- API가 어떻게 작동하는지 시각적으로 보여주는 문서를 생성 가능하고, 이를 활용하여 API를 이해하고 테스트하는데 유용
  > Swagger-UI나 ReDoc이 유용한 도구

## 참고
### 올바른 404 응답
> 장고에는 404를 응답하는 함수가 존재한다.
- `get_object_or_404()`
  - 모델 objects에서 get()을 호출하고, 해당 객체가 없으면 예외 대신 Http404를 raise
  > `article = Article.objects.get(pk=article_pk)`<br>=><br>
  > `article = get_object_or_404(Article, pk=article_pk)`
- `get_list_or_404()`
  - 모델 objects에서 filter()의 결과를 반환하고, 해당 객체 목록이 없으면 Http404를 raise

#### 사용 이유
- 클라이언트에게 실행 오류에 대한 현황과 원인을 전달하는 것이 중요하기 때문이다.
> 서버 오류의 경우 해결이 불가능하거나 모호해진다.

### 복잡한 ORM 활용
- 복잡한 query나 로직은 `View 함수`에서 진행
- `Serializer`는 기본적인 데이터 변환을 담당
  > Serializer만으로는 복잡한 query를 처리하기 어렵다.