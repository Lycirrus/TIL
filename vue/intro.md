# 개요
## 프론트엔드 개발
웹 사이트와 웹 애플리케이션의 UI와 UX를 만들고 디자인하는 것
> HTML, CSS, JavaScript 등을 활용하여 사용자가 **직접 상호작용**하는 부분을 개발한다.

### Client-side frameworks
- 클라이언트 측에서 UI와 상호작용을 개발하기 위해 사용되는 JavaScript 기반 프레임워크

#### 필요 이유
1. 웹이 단순히 읽는 공간에서 무언가를 하는 공간으로 변화
   - 현대적이고 복잡한 대화형 웹 사이트를 **웹 애플리케이션**이라 부름
   - JavaScript 기반이 등장하면서 매우 동적인 대화형 애플리케이션을 훨씬 더 쉽게 구축 가능
2. 다루는 데이터량의 증가
   - 애플리케이션의 기본 데이터를 안정적으로 추저가고 업데이트하는 도구가 필요
   > 애플리케이션의 상태를 변경할 때마다 일치하도록 UI를 업데이트 해야한다.

#### 필요성 정리
1. 동적이고 반응적인 웹 애플리케이션 개발
   - 실시간 데이터 업데이트
2. 코드 재사용성 증가
   - 컴포넌트 기반 아키텍쳐
   - 모듈화된 코드 구조
3. 개발 생산성 향상
   - 강력한 개발 도구 지원

### SPA
- 단일 페이지에서 동작하는 웹 애플리케이션

#### 작동 원리
- 최초 로드 시 필요한 모든 리소스 다운로드
- 이후 페이지 갱신에 대해 필요한 데이터만을 비동기적으로 전달 받아 화면의 필요한 부분만 동적 갱신
- JavaScript를 사용하여 클라이언트 측에서 동적으로 콘텐츠를 생성하고 업데이트
  > CSR 방식

### CSR
- 클라이언트에서 콘텐츠를 렌더링하는 방식

#### 작동 원리
1. 사용자가 웹사이트에 요청을 보낸다.
2. 서버는 최소한의 HTML과 JavaScript 파일을 클라이언트로 전송한다.
3. 클라이언트는 HTML과 JavaScript를 다운로드 받는다.
4. 브라우저가 JavaScript를 실행하여 동적으로 페이지 콘텐츠를 생성한다.
5. 필요한 데이터는 API를 통해 서버로부터 비동기적으로 가져온다.

### SPA와 CSR의 장점
1. 빠른 페이지 전환
   - 페이지가 처음 로드된 후에 필요한 데이터만 가져옴
   - 전체 새로고침 필요 없음
   - 서버로 전송되는 데이터의 양을 최소화
     > 서버의 부하를 방지한다.
2. 사용자 경험
   - 새로고침이 발생하지 않아 네이티브 앱과 유사한 사요자 경험을 제공
3. 프론트엔드와 백엔드의 명확한 분리
   - 프론트엔드는 UI 렌더링 및 사용자 상호 작용 처리를 담당
   - 백엔드는 데이터 및 API 제공을 담당
   > 대규모 애플리케이션을 더 쉽게 개발하고 유지 관리 가능하다!

### SPA와 CSR의 단점
1. 느린 초기 로드 속도
   - 전체 페이지를 보기 전 지연 발생
2. 검색 엔진 최적화 (*SEO*) 문제
   - 페이지를 나중에 그려나가기에 검색에 잘 노출되지 않을 가능성 존재
   - 검색엔진 입장에서 HTML을 읽어서 분석해야 하나 아직 콘텐츠가 모두 존재하지 않기 때문

### MAP와 SSR
- MPA - *Multi Page Application*
  - 여러 개의 HTML 파일이 서버로부터 각각 로드
  - 사용자가 다른 페이지로 이동할 때마다 새로운 HTML 파일이 로드
- SSR - *Server-side Rendering*
  - 서버에서 화면을 렌더링하는 방식
  - 모든 데이터가 담긴 HTML을 서버에서 완성 후 클라이언트에게 전달

## Vue
사용자 인터페이스를 구축하기 위한 JavaScript 프레임워크

#### Vue의 이점
1. 낮은 학습 곡선
   - 간결하고 직관적인 문법
   - 잘 정리된 문서 존재
2. 확정성과 생태계
   - 다양한 플러그인과 라이브러리를 제공
   - 활성화된 커뮤니티의 존재
3. 유연성 및 성능
   - 작은 규모부터 대규모 애플리케이션까지 다양항 프로젝트에 적합
4. 가장 주목받는 클라이언트 기반 프레임워크

#### Vue의 핵심 기능
1. 선언적 렌더링
   - 표준 HTML을 확장하는 **Vue 템플릿 구문**을 사용하여 JavaScript 데이터를 기반으로 화면에 출력될 HTML을 선언적으로 작성
2. 반응성
   - JavaScript 상태 변경을 추적
   - 변경사항이 발생하면 자동으로 DOM을 업데이트

#### 주요 특징
1. 반응형 데이터 바인딩
   - 데이터 변경 시 **자동 UI 업데이트**
2. 컴포넌트 기반 아키텍쳐
   - **재사용 가능**한 UI 조각
3. 간결한 문법과 직관적인 API
   - 낮은 학습 곡선
   - 높은 가독성
4. 유연한 스케일링
   - 작은 프로젝트부터 대규모 앱까지 적합

### Component
- 재사용 가능한 코드 블록

#### 특징
- UI를 독립적이고 재사용 가능한 일부분으로 분할하고 각 부분을 개별적으로 다룰 수 있음
  > 애플리케이션은 자연스러운 중첩된 Component의 트리 형태로 구성된다.

## Vue Application
### Vue Application 생성
1. CDN 작성 (또는 NPM 설치)
2. Application Instance 작성
   - CDN에서 Vue를 사용하는 경우 전역 Vue 객체를 불러오게 됨
   - 구조분해할당 문법으로 Vue 객체의 createApp함수를 할당
   ```javascript
   const { createApp, ref } = Vue
   ```
3. 사용자 기반 새 Application instance를 생성
   ```javascript
   const { createApp, ref } = Vue

   const app = createApp({})
   ```
4. Root Component
   - createApp 함수에 객체(컴포넌트)가 전달
   - 모든 App에는 다른 컴포넌트들을 하위 컴포넌트로 포함할 수 있는 최상위의 Root 컴포넌트가 필요
5. 앱 연결 (*Mounting the App*)
   - HTML 요소에 Vue Application instance를 연결
   - 각 앱 인스턴스에 대해 mount()는 한 번만 호출 가능
   ```javascript
   <div id="app"></div>
   ...

   <script>
    cont { createApp, ref } = Vue

    const app = createApp({})

    // 마운팅하는 부분
    app.mount('#app')
   </script>
   ```

### 반응형 상태
- `ref()` : 반응형 데이터를 선언하는 함수
  - `.value` 속성이 있는 `ref` 객체로 감싸서 반환하는 함수
  - ref로 선언된 변수 값이 변경되면, 해당 값을 사용하는 템플릿에서 자동으로 업데이트
  - 인자는 어떠한 타입도 가능
  ```javascript
  const message = ref('Hello Vue!')
  console.log(message) // ref 객체
  console.log(message.value) // Hello Vue!
  ```

  - 템플릿 참조에 접근하려면 setup 함수에서 선언 및 반환 필요
  - 편의상 템플릿에서 ref를 사용할 때는 .value를 작성할 필요 없음
  ```javascript
  const app = createApp({
    // 템플릿에 접근하기 위한 setup 함수
    setup() {
      const message = ref('Hello Vue!')
      return {
        message  // 템플릿에 반환된다.
        // value를 작성할 필요가 없다.
      }
    }
  })
  ```

  > 즉, 반응형을 가지는 참조 변수를 만드는 함수이다.

### Vue 기본 구조
- createApp()에 전달되는 객체는 Vue 컴포넌트
- 컴포넌트의 상태는 **무조건 setup() 함수** 내에서 선언되어야 함
- **객체 반환은 필수**

#### 템플릿 렌더링
- 이중 중괄호 구문을 사용하여 메시지 값을 기반으로 동적 텍스트를 렌더링
- 콘텐츠는 식별자나 경로에만 국한되지 않으며 유효한 JavaScript 표현식 사용 가능

#### Vue에서의 Event Listener
- `v-on` directive를 사용하여 DOM 이벤트 수신 가능
- 함수 내에서 반응형 변수를 변경하여 구성 요소 상태를 업데이트

## Template Syntax
DOM을 기본 구성 요소 인스턴스의 데이터에 **선언적으로 바인딩** *Vue Instance와 DOM을 연결* 할 수 있는 HTML 기반 **확장된 문법을 제공하는 템플릿 구문**을 사용

### 종류
1. Text Interpolation
  ```html
  <p>Message: {{ msg }}</p>
  ```
  - 데이터 바인딩의 가장 기본적인 형태
  - 이중 중괄호 구문을 사용
  - 구문은 해당 구성 요소 인스턴스의 msg 속성 값으로 대체
  - msg 속성이 변경될 때마다 업데이트

2. Raw HTML
   ```html
   <div v-html="rawHTML"></div>

   ...
   <script>
    const rawHtml = ref('<span style="color:red">This should be red.</span>')
   </script>
   ```
   > 콧수염 구문은 데이터를 일반 텍스트로 해석하기 때문에 실제 HTML을 출력하려면 `v-html`을 사용해야 한다.

3. Attribute Bindings
   ```html
   <div v-bind:id="dynamicId"></div>
   ...

   <script>
    const dynamicId = ref('my-id')
   </script>
   ```
   > 콧수염 구문은 HTML 속성 내에서는 사용이 불가하다.
   >
   > v-bind를 사용하여 id 속성 값을 'dynamicId' 속성과 동기화한다.
   - null이나 undefined가 바인딩 되었다면 렌더링 요소에서 제거됨

4. JavaScript Expressions
   ```javascript
   {{ number + 1}}

   {{ true ? 'YES' : 'NO' }}

   {{ message.split('').reverse().join('')}}

   <div v-bind:id="`list-${id}`"></div>
   ```
   - 모든 데이터 바인딩 내에서 JavaScript 표현식의 모든 기능을 지원
   - 콧수염 구문 내부와 "v-"로 시작하는 특수 속성에서 사용 가능

### 주의사항
- 각 바인딩에는 하나의 단일 표현식만 포함 가능
> 선언식은 작동하지 않는다.

> 제어문은 삼항 표현식을 사용해야 한다.

## 참고
### ref 객체
- Vue는 변수 값이 변경되면 자동으로 DOM을 업데이트
- 바닐라 JS에는 일반 변수의 접근 또는 변형을 감지할 방법이 없음
- 참조 자료형의 객체 타입으로 구현한 ref 객체
- Vue는 렌더링 중에 사용된 모든 ref를 추적하며, ref가 변경되면 추적 구성 요소에 대해 다시 렌더링

### Ref Unwrap 주의사항
> Unwrap은 ref가 최상위 속성인 경우에만 적용가능하다.
  ```javascript
  const object = { id: ref(0) }

  {{ object.id + 1 }}
  ```
> 위의 경우 object.id가 최상위 속성이 아니므로 원하는대로 출력되지 않는다!
  ```javascript
  const object = { id: ref(0) }
  const { id } = object
  ```
> 따라서 id를 최상위 속성으로 분해해야 한다.
>> 다만, 콧수염 구문 내에서 변화가 없을 경우는 속성 분해 없이 unwrap이 가능하다.
  ```javascript
  {{ object.id }}
  // 위의 object.id + 1는 변화가 있으므로 최상위 속성으로 분해해야 한다.
  ```

### SEO
- 검색 엔진 등에 내 서비스나 제품 등이 효율적으로 노출되도록 개선하는 과정을 일컫는 작업
  - 정보 대상은 주로 HTML에 작성된 내용

<br>

- 검색
  - 각 사이트가 운용하는 검색 엔진에 의해 이루어지는 작업
- 검색 엔진
  - 웹 상에 존재하는 가능한 모든 정보들을 긁어 모으는 방식으로 동작

<br>

- 최근에는 SPA, 즉 CSR로 구성된 서비스 비중 증가
- SPA 서비스도 검색 대상으로 넓히기 위해 JS를 지원하는 방식으로 발전 중

### CSR과 SSR
- 애플리케이션의 목적, 규모, 성능 및 SEO 요구 사항에 따라 달라질 수 있음

<br>

- SPA 서비스에서도 SSR을 지원하는 Framework가 발전하고 있음
  - Vue의 Nuxt.js
  - React의 Next.js
