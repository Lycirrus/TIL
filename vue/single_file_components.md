# Single-file Components
### Component
- 재사용 가능한 코드 블록

#### 특징
- UI를 독립적이고 재사용 가능한 일부분으로 분할하고 각 부분을 개별적으로 다룰 수 있음
  > 자연스럽게 앱은 중첩된 Component의 트리 형태로 구성된다.

### Single-File Components (SFC)
- 컴포넌트의 템플릿, 로직 및 스타일을 하나의 파일로 묶어낸 특수한 파일 형식 
  > *(.vue 파일)*

### SFC 구성요소
- 최상위 언어 블록 <template>, <script>, <style>로 구성됨
  > 일반적으로 <template> -> <script> -> <style> 순서로 작성한다.

#### <template> 블록
- 각 vue 파일은 하나의 template 블록만 포함 가능

#### <script setup> 블록
- 각 vue 파일은 하나의 script setup 블록만 포함 가능
- 컴포넌트의 setup() 함수로 사용되며 컴포넌트의 각 인스턴스에 대해 실행
  > 변수 및 함수는 동일한 컴포넌트의 템플릿에서 자동으로 사용 가능하다.

#### <style scoped> 블록
- 하나의 vue 파일에 여러 style 태그가 포함될 수 있음
- scoped가 지정되면 CSS는 현재 컴포넌트에서만 적용됨

> 컴포넌트는 일반적인 방법으로 실행할 수 없다.
>> Vite와 같은 공식 빌드 도구 사용

## SFC build tool
### Vite [비트]
프론트 엔드 개발 도구

- `Build` : 프로젝트의 소스 코드를 최적화하고 번들링하여 배포할 수 있는 형식으로 변환하는 과정
  - 최종 소프트웨어 제품을 생성하는 작업
  > Vite는 이러한 빌드 프로세스를 수행하는데 사용되는 도구이다.

### Vue Project
- Vue Project 생성 (Vite 기반)
  > `npm create vue@latest`
- 프로젝트 폴더 이동
  > `cd vue-project`
- 패키지 설치
  > `npm install`
- Vue 프로젝트 서버 실행
  > `npm run dev`

### NPM
- Node.js의 기본 패키지 관리자

#### Node.js
- Chrome의 V8 JavaScript 엔진을 기반으로 하는 Server-Side 실행 환경

- 영향 :
  - 기존에 브라우저 안에서만 동작했던 JavaScript를 브라우저가 아닌 서버 측에서도 실행할 수 있게 함
    > 프론트와 백을 동일한 언어로 개발할 수 있게 되었다.

  - NPM을 활용해 수많은 오픈 소스 패키지와 라이브러리를 제공하여 개발자들이 손쉽게 코드를 공유하고 재사용할 수 있게 함

### 모듈과 번들러
- `Module` : 프로그램을 구성하는 독립적인 코드 블록 *(.js 파일)*

#### 모듈 필요성
- 개발 애플리케이션의 크기가 커지고 복잡해짐
  > 파일 하나에 모든 기능을 담을 수 없어졌다.
- 자연스럽게 파일을 여러 개로 분리하여 관리하는 방향으로 발전
  > 각각의 분리된 파일을 `모듈`이라 한다.
  >
  > *.js 파일 하나가 하나의 모듈

#### 모듈의 한계
- 애플리케이션의 발전으로 처리 모듈 개수도 기하급수적으로 증가
- 성능 병목 현상, 모듈 간의 연결성 심화로 인해 문제 발생 시 연관 모듈을 파악하기 어려워짐
  > 복잡하고 깊은 모듈 간 의존성 문제를 해결하기 위한 도구가 `Bundler`

#### Bundler
- 여러 모듈과 파일을 하나나 여러 개의 번들로 묶어 최적화하여 애플리케이션에서 사용할 수 있게 만들어주는 도구
- 역할 :
  - 의존성 관리
  - 코드 최적화
  - 리소스 관리
  > Bundler가 하는 작업을 Bundling이라 한다.

## Vue Project 구조
- node_modules
  - Node.js 프로젝트에서 사용되는 외부 패키지들이 저장되는 디렉토리
  - 프로젝트의 의존성 모듈을 저장하고 관리하는 공간
  - 프로젝트가 실행될 때 필요한 라이브러리와 패키지들을 포함
  > .gitignore에 작성된다.

- package-lock.json
  - 패키지들의 실제 설치 버전, 의존성 관계, 하위 패키지 등을 포함하여 패키지 설치에 필요한 모든 정보를 포함
  - 패키지들의 정확한 버전 보장
    > 여러 개발자가 **협업**하거나 서버 환경에서 **일관성 있는 의존성**을 유지하는데 도움을 준다.

- package.json
  - 프로젝트의 메타 정보와 의존성 패키지 목록을 포함
  - 프로젝트의 이름, 버전, 작성자, 라이선스 등과 같은 메타 정보를 정의
  > 프로젝트의 의존성 관리와 버전 충돌 및 일관성을 유지하는 역할을 한다.

- public 디렉토리
  - 정적 파일들이 위치
    - 소스코드에서 참조되지 않는 파일
    - 항상 같은 이름을 갖는 파일
    - import 할 필요 없는 파일
  - 항상 root 절대 경로를 사용하여 참조

- src 디렉토리
  - 프로젝트의 주요 소스 코드를 포함
  - 컴포넌트, 스타일, 라우팅 등 프로젝트의 핵심 코드 관리

  - `scr/assets`
    - 프로젝트 내에서 사용되는 자원을 관리
    - 컴포넌트 자체에서 참조하는 내부 파일을 저장하는데 사용
    - 컴포넌트가 아닌 곳에서는 public 디렉토리에 위한 파일 사용
  - `src/components`
    - Vue 컴포넌트들을 작성하는 곳
  - `src/App.vue`
    - Vue 앱의 최상위 Root 컴포넌트
    - 다른 하위 컴포넌트들을 포함
    - 앱 전체의 레이아웃과 공통적인 요소 정의
  - `src/main.js`
    - Vue 인스턴스를 생성하고, 앱을 초기화하는 역할
    - 필요한 라이브러리를 import하고 전역 설정을 수행

- index.html
  - Vue 앱의 기본 HTML 파일
  - 앱의 진입점
  - Root 컴포넌트인 App.vue가 해당 페이지에 마운트
  - 부트스트랩 같은 외부 리소스를 로드할 수 있음

- 기타 설정 파일
  - `jsconfig.json` : 컴파일 옵션, 모듈 시스템 등 설정
  - `vite.config.js` : 플러그인, 빌드 옵션, 개발 서버 설정 등

## Vue Component 활용
### 사전 준비
1. App.vue를 제외한 초기 컴포넌트 삭제
2. App.vue 초기화

### 컴포넌트 사용 2단계
1. 컴포넌트 파일 생성
   - MyComponent.vue 생성

2. 컴포넌트 등록 (import)
   - App 컴포넌트에 MyComponent 등록
     ```vue
     <!-- App.vue -->

     <template>
      <MyComponent />

      <!-- 컴포넌트의 재사용성 확인 -->
      <MyComponentItem />
      <MyComponentItem />
      <MyComponentItem />
     </template>

     <script setup>
     // import MyComponent from './components/MyComponent.vue'
     import MyComponent from '@/components/MyComponent.vue'
     // App.vue에 MyComponent.vue를 등록하므로서 부모 자식 관계를 형성한다.
     // @는 src/ 경로를 뜻하는 약어이다.

     import MyComponentItem from '@/components/MyComponentItem.vue'
     
     ```

## 추가 주제
### Virtual DOM
- 가상의 DOM을 메모리에 저장하고 실제 DOM과 동기화하는 프로그래밍 개념
- 실제 DOM과의 변경 사항 비교를 통해 변경된 부분만 실제 DOM에 적용하는 방식
- 웹 어플리케이션의 성능을 향상시키기 위한 Vue의 내부 렌더링 기술

#### 장점
- 효율성
  - 실제 DOM 조작을 최소화하고, 변경된 부분만 업데이트
- 반응성
  - 데이터의 변경을 감지하고, Virtual DOM을 효율적으로 갱신하여 UI 자동 업데이트
- 추상화
  - 개발자는 실제 DOM 조작을 Vue에게 맡기고 컴포넌트와 템플릿을 활용하는 추상화된 프로그래밍 방식으로 원하는 UI 구조를 구성하고 관리

#### 주의사항
- 실제 DOM에 접근하지 말 것
  > Vue의 ref()와 Lifecycle Hooks 함수를 사용해 간접적으로 접근 조작해야 한다.

- 직접 접근해야 하는 경우에는 ref 속성 하용
  ```vue
  <template>
    <input ref="input">
  </template>

  <script setup>
  import { ref, onMounted } from 'vue'

  // 변수명은 템플릿 ref 값과 일치해야만 한다.
  const input = ref(null)

  onMounted(() => {
    console.log(input.value) // <input>
  })
  </script>
  ```

### Composition API & Option API
- Vue를 작성하는 2가지 스타일
  - Composition API
  - Option API

#### Composition API
- import 해서 가져온 API 함수들을 사용하여 컴포넌트의 로직 정의
  > Vue3에서의 권장 방식

#### Option API
- data, method 및 mounted 같은 객체를 사용하여 컴포넌트의 로직을 정의
  > 주로 Vue2에서 사용

#### API 별 권장 사항
- Composition API + SFC
  - 규모가 있는 앱의 전체를 구축하려는 경우
- Option API
  - 빌드 도구를 사용하지 않거나 복잡성이 낮은 프로젝트에서 사용하려는 경우

## 참고
### Single Root Element
- Vue는 컴포넌트의 최상위 코드 블록은 하나만 하는 것을 권장
  ```Vue
  <!-- 권장 예시 -->
  <template>
    <div>
      <h2>Head</h2>
      <p>HI</p>
    </div>
  </template>

  <!-- 비권장 예시 -->
  <template>
    <div>
      <h2>Head</h2>
    </div>
    <div>
      <p>HI</p>
    </div>
  </template>
  ```

### CSS scoped
- scoped 속성을 사용하면 해당 CSS는 현재 컴포넌트 요소에만 적용
- 그러나 자식 컴포넌트의 최상위 요소는 부모 CSS와 본인 CSS 모두에게서 영향을 받음
  > 자식 컴포넌트의 최상위 요소는 부모에서 사용되기 때문이다.

### Scaffolding (스캐폴딩)
- 새로운 프로젝트나 모듈을 시작하기 위해 초기 구조와 기본 코드를 자동으로 생성하는 과정
  > - 개발자의 시간과 노력을 절약
  > - 일관된 구조 유지

- 요근래는 단순 파일 유형이 아닌, **사용 목적**에 따라 결합
