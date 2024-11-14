# Vue with DRF
## 메인 페이지 구현
### DRF와의 요청과 응답
- DRF 서버에 요청하여 데이터를 응답 받아 store에 저장 후 출력

#### 과정
- DRF 서버로의 AJAX 요청을 위한 axios 설치 및 관련 코드 작성
```javascript
// counter.js

import axios from 'axios'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'
})
```
- DRF 서버로 요청을 보내고 응답 데이터를 처리하는 메서드 작성
```javascript
// counter.js

const getArticles = function () {
  axios({
    method: 'get',
    url: `${API_URL}/api/v1/articles/`
  }).then((response) => {
    ...
  }).catch((error) => {
    ...
  })
}
```
- ArticleView 컴포넌트가 마운트 될 때 getArticles 함수가 실행되도록 함
```javascript
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()

onMounted(() => {
  store.getArticles()
})
```

### SOP
- 동일 출처 정책
  - 어떤 출처에서 불러온 문서나 스크립트가 다른 출처에서 가져온 리소스와 상호 작용하는 것을 제한하는 보안 방식
  > 프로토콜, 호스트, 포트가 모두 동일한 경우에만 동일 출처로 인정한다.

#### SOP 문제점
- 현대 웹 애플리케이션은 다양한 출처로부터 리소스를 요청하는 경우가 많음
> 웹 서버가 리소스에 대한 서로 다른 출처 간 접근을 허용하도록 선택할 수 있는 기능인 **CORS**가 등장한다.

### CORS Policy
- `CORS` : 교차 출처 리소스 공유
  - 특정 출처에서 실행 중인 웹 애플리케이션이 **다른 출처의 자원에 접근할 수 있는 권한을 부여**하도록 브라우저에게 알려주는 체제

- `CORS Policy` : 교차 출처 리소스 공유 정책
  - 서버에서 설정되어 브라우저가 해당 정책을 확인하여 요청이 허용되는지 여부를 결정
  > 다른 출처의 리소스를 불러오려면 그 다른 출처에서 올바른 **CORS header를 포함한 응답을 반환**해야 한다.

### CORS Headers 설정
> Django에서는 `django-cors-headers` 라이브러리 활용

#### 사용
- 설치<br>
`pip install django-cors-headers`

- settings.py 설정
```python
INSTALLED_APPS = [
  ...,
  'corsheaders',
  ...
]

MIDDLEWARE = [
  ...,
  'corsheaders.middleware.CorsMiddleware',
  ...
]
```

- CORS를 허용할 Vue 프로젝트의 Domain 등록
```python
# settings.py

CORS_ALLOWED_ORIGINS = [
  'http://127.0.0.1:5173',
  'http://localhost:5173',
]
```

## Article CR 구현
### 전체 게시글 조회
- 생성한 articles 객체의 value에 응답 데이터 response의 data를 넣는다.

### 단일 게시글 조회
- 게시글 경로 작성
```javascript
// index.js

import DetailView from '@/views/DetailView.vue'

const router = createRouter({
  ...,
  routes: [
    ...,
    {
      path: '/articles/:id',
      name: 'detailView',
      component: DetailView
    }
  ]
})
```
- DetailView 컴포넌트로 가기 위한 RouterLink 작성
- DetailView가 마운트 될 때 특정 게시글을 조회하는 AJAX 요청 진행
```javascript
...

const store = useCounterStore()
const route = useRoute()
const article = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
  }).then((res) => {
    article.value = res.data
  }).catch((err) => {
    ...
  })
})
```

### 게시글 작성
- createView로 가는 경로를 index.js에 작성
- RouterLink 작성
- 게시글 생성을 요청하는 함수 작성
```javascript
// CreateView.vue

const createArticle = function () {
  axios({
    method: 'post',
    url: `${store.API_URL}/api/v1/articles/`,
    data: {
      title: title.value,
      content: content.value
    },
  }).then(() => {
    router.push({ name: 'ArticleView' })
    // 생성 성공 시 전체 게시판으로 이동
  }).catch((err) => {
    ...
  })
}
```
- v-model을 사용해 사용자 입력 데이터 양방향 바인딩
  > `trim` : 공백 제거
- submit에 함수 호출
```vue
<div>
  <form @submit.prevent="createArticle">
    <input ... v-model.trim="content">
  </form>
</div>
```

## 인증 with DRF
### 인증
> 토큰을 이용하여 사용자를 인증한다!

#### 요청 관련 거부 응답
- HTTP 401 Unauthorized
  - 유효한 인증 자격이 없음
  - 서버가 클라이언트를 모름
- HTTP 403 Forbidden
  - 권한 때문에 거절
  - 서버가 클라이언트를 인지

### 인증 정책 설정
#### 설정 위치
- 전역 설정
  - `DEFAULT_AUTHENTICATION_CLASSES` 사용
    ```python
    REST_FRAMEWORK = {
      'DEFAULT_AUTHENTICATION_CLASSES' : [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
      ]
    }
    ```
- View 함수 별 설정
  - `authentication_classes` 데코레이터 사용
    ```python
    from rest_framework.decorators import authentication_classes
    from rest_framework.authentication import BasicAuthentication, TokenAuthentication

    @api_view(['GET', 'POST'])
    @authentication_classes([TokenAuthentication, BasicAuthentication])
    def article_list(request):
      pass
    ```

### Token 인증 설정
#### TokenAuthentication
- token 기반 HTTP 인증 체계
- 기본 클라이언트-서버 설정에 적합

> 서버가 인증된 사용자에게 토큰을 발급하고 사용자는 매 요청마다 발급받은 토큰을 요청과 함께 보내 인증 과정을 거친다.

#### 적용 과정
- 인증 클래스 설정
  > 전역 설정
- INSTALLED_APPS에 추가
  > `rest_framework.authtoken` 추가
- Migrate 진행
- 토큰 생성 코드 작성
  ```python
  from djnago.db.models.signals import post_save
  from django.dispatch import receiver
  from rest_framework.authtoken.models import Token
  from django.conf import settings

  @receiver(post_save, sender=settings.AUTH_USER_MODEL)
  def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
      Token.objects.create(user=instance)
  ```

#### 토큰 인증 방식 과정
1. 클라이언트의 로그인
2. 서버가 DB에서 사용자 확인
3. Token 발급
4. Token을 포함하여 응답
5. Token을 포함하여 데이터 요청
6. Token 검증
7. 요청 데이터를 포함하여 응답

### Dj-Rest-Auth 라이브러리
- 회원가입, 인증, 비밀번호 재설정, 사용자 세부 정보 검색, 회원 정보 수정 등 다양한 인증 관련 기능 제공 라이브러리

#### 설치 과정
- 설치<br>
  `pip install dj-rest-auth`
- INSTALLED_APPS에 추가<br>
  `dj_rest_auth`
- URL 추가<br>
  `path('accounts/', include('dj_rest_auth.urls'))`

#### Registration 기능 추가 설정
- 패키지 설치<br>
  `pip install 'dj-rest-auth[with-social]'`
- INSTALLED_APPS 추가 <br>
  ```python
  INSTALLED_APPS = [
    ...,
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'dj_rest_auth.registration',
  ]

  SITE_ID = 1
  ```
- allauth에 대한 middleware 작성
  ```python
  MIDDLEWARE = [
    ...,
    'allauth.account.middleware.AccountMiddleware',
  ]
  ```
- 회원 등록 URL 추가
  ```python
  urlpatterns = [
    ...,
    path('accounts/signup/', include('dj_rest_auth.registration.urls')),
  ]
  ```
- Migrate 진행

## 권한 with DRF
### 권한 정책 설정
- 전역 설정
  - `DEFAULT_PERMISSION_CLASSES` 사용
    ```python
    REST_FRAMEWORK = {
      'DEFAULT_PERMISSION_CLASSES' : [
        'rest_framework.permissions.IsAuthenticated',
      ],
    }
    ```
- view 함수 별 설정
  - `permission_classes` 데코레이터 사용
    ```python
    from rest_framework.decorators import permission_classes
    from rest_framework.permissions import IsAuthenticated

    @api_view(['GET', 'POST'])
    @permission_classes([IsAuthenticated])
    def article_list(request):
      pass
    ```

### isAuthenticated 설정
- 인증되지 않은 사용자에 대한 권한을 거부하고 그렇지 않은 경우 권한을 허용
  > 등록된 사용자만 API에 액세스 하도록 하는 경우에 적합하다.

#### 권한 설정 방법
- settings.py에 `DEFAULT_PERMISSION_CLASSES` 정보 입력
- 인증된 사용자만 진행 할 수 있도록 view별로 설정한다.

## 인증 with Vue



### 회원가입



### 로그인



### 요청과 토큰



### 인증 여부 확인



## 참고