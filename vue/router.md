# Routing
네트워크에서 경로를 선택하는 프로세스
> 웹 애플리케이션에서 다른 페이지 간의 전환과 경로를 관리하는 기술

#### SSR에서의 Routing
- SSR에서 routing은 서버 측에서 수행
- 서버가 사용자가 방문한 URL 경로를 기반으로 응답을 전송
- 링크를 클릭하면 브라우저는 서버로부터 HTML 응답을 수신하고 새 HTML로 전체 페이지를 다시 로드

#### CSR에서의 Routing
- CSR에서 routing은 클라이언트 측에서 수행
- 클라이언트 측 JavaScript가 새 데이터를 동적으로 가져와 전체 페이지를 다시 로드하지 않음

### Routing이 없는 SPA
- 유저가 URL을 통한 페이지 변화 감지 불가
- 페이지가 무엇을 렌더링 중인지 상태 파악 불가
  > URL이 1개이기에 새로고침 시 처음 페이지로 되돌아간다.
  >
  > 링크를 공유할 시 첫 페이지만 공유 가능
- 브라우저의 뒤로 가기 기능 사용 불가

> 페이지는 1개이지만, 주소에 따라 여러 컴포넌트를 새로 렌더링하여 마치 여러 페이지를 사용하는 것처럼 보이도록 해야 한다!!

## Vue Router
Vue 공식 라우터

#### RouterLink
```vue
<RouterLink to="/">Home</RouterLink>
<RouterLink to="/about">About</RouterLink>
<!-- HTML의 <a> 태그를 렌더링한다. -->

<RouterView />
<!-- RouterLink URL에 해당하는 컴포넌트를 표시한다. -->
<!-- 원하는 곳에 배치하여 컴포넌트를 레이아웃에 표시할 수 있다 -->
```
- `src/router/index.js` : 라우팅에 관련된 정보 및 설정이 작성되는 곳
- `src/views` : RouterView 위치에 렌더링 할 컴포넌트를 배치
  > 기존 components와 차이는 없고, 단순히 분류를 위해 따로 위치한다.
  
  > 따라서, 컴포넌트 명의 끝에 'view'로 끝나도록 하는 것이 좋다.

### Basic Routing
```javascript
// index.js

const router = createRouter({
  routes: [
    {
      path: '/',          // URL
      name: 'home',       // 이름
      component: HomeView // 적용 컴포넌트
    },
    ...
  ]
})
```
- RouterLink의 'to' 속성에 index.js에서 정의한 'path'를 사용
- RouterLink 클릭 시 경로와 일치하는 컴포넌트가 RouterView에서 렌더링

### Named Routes
- 경로에 이름을 지정하는 라우팅

#### 예시
- 위의 index.js에서 name 속성을 활용
```vue
<!-- App.vue -->

<!-- name 속성 값에 경로에 대한 이름을 지정한다. -->
<RouterLink :to="{ name: 'home' }">Home</RouterLink>
<RouterLink :to="{ name: 'about' }">About</RouterLink>
<!-- RouterLink에 v-bind를 사용해 'to' props 객체로 전달한다. -->
```

#### 장점
- 하드 코딩 된 URL을 사용하지 않아도 됨
- URL 입력 시의 오타 방지

### Dynamic Route Matching
- URL의 일부를 변수로 사용하여 경로를 동적으로 매칭
```javascript
// index.js
...
path: '/user/:id'
// 매개변수 부분을 콜론으로 표기한다.
```
```vue
<RouterLink :to="{ name: 'user', params: { 'id' : userId } }">User</RouterLink>

<!-- 매개변수는 객체의 'params' 속성의 객체 타입으로 전달 -->

<!-- 단, 객체의 key이름과 index.js에서 지정한 매개변수 이름이 같아야 한다 -->
```
- 경로가 일치하면 라우트의 매개변수는 컴포넌트에서 아래와 같이 참조 가능
```vue
{{ $route.params.id }}
```
- `useRoute()` 함수를 사용해 스크립트 내에서 반응형 변수에 할당 후 템플릿에 출력하는 것을 권장
  > $route의 사용과 동일
```javascript
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const userId = ref(route.params.id)
// userId를 템플릿에서 기존 $route.params.id 대신 사용
```

### Nested Routes
- 중첩 라우팅

#### 활용
- 중첩 시킬 두 컴포넌트 작성
- 라우터 등록
  ```javascript
  // index.js

  import aComp from ...
  import bComp from ...
  ```
- `children`옵션을 사용해 중첩된 라우터에 컴포넌트를 등록
  ```javascript
  // index.js
  ...
  {
    path: ...
    ...
    // children : 배열 형태로 필요한 만큼 중첩 관계를 표현할 수 있다.
    children: [
      { path: '', name: 'user', component: UserHome },
      // 중첩 Named Routes를 다룰 때는 일반적으로 하위 경로에만 이름을 지정한다.
      { path: 'a', name: 'acomp', component: aComp },
      { path: 'b', name: 'bcomp', component: bComp }
    ]
  }
  ```
- 두 컴포넌트에 대한 RouterLink 및 RouterView 작성

### Programmatic Navigation
- RouterLink 대신 JavaScript를 사용해 페이지를 이동하는 것

#### router 메서드
1. 다른 위치로 이동
   - `router.push()`
2. 현재 위치 변경
   - `router.replace()`

#### router.push()
> 새 항목을 history stack에 push해서 사용자가 브라우저 뒤로 가기 버튼을 클릭하면 이전 URL로 이동할 수 있도록 한다.

- RouterLink 클릭 시 내부적으로 호출되는 메서드
  - 선언적 표현 : <RouterLink :to="...">
  - 프로그래밍적 표현 : router.push(...)

- 활용
  ```javascript
  import { useRouter } from 'vue-router'

  const router = useRouter()
  const goHome = function () {
    router.push({ name: 'home' })
  }
  ```
  ```vue
  <button @click="goHome">홈</button>
  ```

#### router.replace()
- push와 달리 history stack에 push 하지 않으므로 뒤로가기 불가
  - 선언적 표현 : <RouterLink :to="..." replace>
  - 프로그래밍적 표현 : router>replace(...)

- 활용
  ```javascript
  const goHome = function () {
    router.replace({ name: 'home' })
  }
  ```

## Navigation Guard
Vue router를 통해 특정 URL에 접근할 때, 다른 URL로 redirect를 하거나 취소하여 네비게이션을 보호
> 라우트 전환 전/후 자동으로 실행되는 Hook

### Globally Guard
- 애플리케이션 전역에서 동작하는 가드
  > 작성위치 : index.js

#### 종류
- `beforeEach()`
- `beforeResolve()`
- `afterEach()`

#### beforeEach
- 다른 URL로 이동하기 직전에 실행하는 함수
- 구조 :
  ```javascript
  router.beforeEach((to, from) => {
    // to : 이동할 URL 정보가 담긴 Route 객체
    // from : 현재 URL 정보가 담긴 Route 객체
    ...
    return false
    또는 
    return { name: 'About' }
    // false :
    //      현재 네이게이션 취소
    //      브라우저 URL이 변경된 경우 'from' 경로의 URL로 재설정

    // Route Location
    //      router.push()를 호출하는 것처럼 경로 위치를 전달하여 다른 위치로 redirect
    //      return이 없다면 자동으로 'to' URL Route 객체로 이동
  })
  ```

### Per-route Guard
- 특정 라우터에서만 동작하는 가드
  > 작성위치 : index.js의 각 routes

#### 종류
- `beforeEnter()`

#### beforeEnter()
- 특정 route에 진입했을 때만 실행되는 함수
  > 단순히 URL의 매개변수나 쿼리 값이 변경될 때는 실행되지 않는다.

  > 다른 URL에서 탐색해 올 때만 실행된다.

- 구조 :
  ```javascript
  ...
  {
    path: ...,
    ...,
    beforeEnter: (to, from) => {
      ...,
      return false
    }
  }
  ```

### In-component Guard
- 특정 컴포넌트 내에서만 동작하는 가드
  > 작성위치 : 각 컴포넌트의 script 내부

#### 종류
- `onBeforeRouteLeave()`
- `onBeforeRouteUpdate()`

#### onBeforeRouteLeave()
- 사용자가 현재 라우트에서 다른 라우트로 이동하기 전 실행
- 구조 :
  ```javascript
  <!-- 특정 컴포넌트 vue 파일 -->

  import { onBeforeRouteLeave } from 'vue-router'

  onBeforeRouteLeave((to, from) => {
    const answer = window.confirm('Leave Truly?')
    if (answer === false) {
      return false
    }
  })
  ```

#### onBeforeRouteUpdate()
- 이미 렌더링 된 컴포넌트가 같은 라우트 내에서 업데이트 되기 전 실행
- 구조 :
  ```javascript
  <!-- 특정 컴포넌트 vue 파일 -->

  import { onBeforeRouteUpdate } from 'vue-router'

  const routeUpdate = function () {
    router.push({ name: 'user', params: { id: 100 } })
  }

  onBeforeRouteUpdate((to, from) => {
    userId.value = to.params.id
  })
  ```

## 참고
### Lazy Loading Routes
```javascript
{
  ...,
  component: () => import('../views/AboutView.vue')
}
```
- Vue 애플리케이션 첫 빌드 시 해당 컴포넌트를 로드하지 않고, "해당 경로를 처음으로 방문할 때 컴포넌트를 로드" 하는 것