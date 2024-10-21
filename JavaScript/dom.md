# DOM
## History of JavaScript
### ECMAScript
- Ecma International이 정의하고 있는 표준화된 스크립트 프로그래밍 언어 명세
  > 스크립트 언어가 준수해야 하는 규칙, 세부사항 등을 제공

### JavaScript
- JavaScript는 ECMAScript 표준을 구현한 구체적인 프로그래밍 언어
- ECMAScript의 명세를 기반으로 하여 웹 브라우저나 Node.js와 같은 환경에서 실행

  > ECMAScript는 JavaScript의 표준이며, JavaScript는 ECMAScript 표준을 따르는 구체적인 포로그래밍 언어
  > ECMAScript는 언어의 핵심을 정의하고, JavaScript는 ECMAScipt 표준을 따라 구현된 언어로 사용

#### ECMAScript의 역사
- ECMAScript 5 (*ES5*)에서 안정성과 생산성을 크게 높임 : 2019년
- ECMAScript 2015 (*ES6*)에서 객체지향 프로그래밍 언어로써 많은 발전을 이루어, 역사상 가장 중요한 버전으로 평가 : 2015년

#### JavaScript의 현재
- 현재는 다양한 웹 브라우저가 경쟁하고 있으며, 모바일 등 시장이 다양화 되어있음
  - 기존 JavaScript는 브라우저에서만 웹 페이지의 동적인 기능을 구현하는 데에만 사용되었음
  - 그러나 Node.js의 출시로 브라우저 외부에서도 실행 가능해져 서버 사이드 개발에도 사용되기 시작함
- 다양한 프레임워크와 라이브러리들이 개발되면서, 웹 개발 분야에서는 필수적인 언어로 자리 잡음

## 변수
### 작성 규칙
  #### 식별자 작성 규칙
  - 반드시 문자, '$', '_'로 시작
  - 대소문자 구분
  - for, if, function 등의 예약어 사용 불가

  #### Naming case
  - 카멜 케이스 (camel`C`ase)
    - 변수, 객체, 함수에 사용
  - 파스칼 케이스 (`P`ascal`C`ase)
    - 클래스, 생성자에 사용
  - 대문자 스네이크 케이스 (`SNAKE_CASE`)
    - 상수에 사용

### 선언 키워드
1. let
   - 블록 스코프(`block scope`)를 갖는 지역 변수를 선언
   - 재할당 가능
   - 재선언 불가능
   - ES6에서 추가
    ```javascript
    let number = 10 // 1. 선언 및 초기값 할당
    number = 20 // 2. 재할당

    // 아래처럼 같은 변수명으로의 재선언은 불가능 
    let number = 30

    // 초기값이 없다면 'undefined'가 할당 (python의 None)
    let number
    // 그러나 작동한다고 초기값을 할당하지 않으면 안된다.
    ```

2. const
   - 블록 스코프를 갖는 지역 변수를 선언
   - 재할당 불가능
   - 재선언 불가능
   - ES6에서 추가
    ```javascript
    const number = 10 // 1. 선언 및 초기값 할당

    number = 20 // (x) 재할당 불가능
    const number = 20 // (x) 재선언 불가능
    const number // (x) 선언 시 반드시 초기값 필요
    ```

#### 블록 스코프
- if, for, 함수 등의 **중괄호 내부**
- 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능

#### 기본 변수 선언 키워드
- 기본은 const
- 필요할 경우 let으로 전환
  - 재할당 필요할 경우
  - 의도적인 변경 가능성을 내재시킬 경우
  - 코드의 유연성을 확보할 경우

#### const가 기본인 이유
- 코드 의도 명확화
  - 해당 변수가 재할당되지 않을 것임을 명확히 표현
  - 개발자에게 변수의 용도와 동작을 더 쉽게 이해할 수 있도록 안내
- 버그 예방
  - 의도치 않은 변수 값 변경으로 인한 버그를 예방
  - 큰 규모의 프로젝트나 팀 작업에서의 안정성

## DOM
`The Document Object Model`
- 웹 페이지를 구조화된 객체로 제공하여 프로그래밍 언어가 페이지 구조에 접근할 수 있는 방법을 제공
> 웹 페이지에서의 JavaScript
> 웹 페이지의 동적 기능 구현
> 문서 구조, 스타일, 내용 변경

#### JavaScript 실행 환경 종류
1. HTML script 태그
2. js 확장자 파일
3. 브라우저 Console

#### DOM API
- 다른 프로그래밍 언어가 웹 페이지에 접근 및 조작 할 수 있도록 **페이지 요소들을 객체 형태로 제공**하며 이에 따른 메서드 또한 제공

### 특징
- DOM에서 모든 요소, 속성, 텍스트는 하나의 객체
- 모두 document 객체의 하위 객체로 구성

### DOM tree
- 브라우저는 HTML 문서를 해석하여 DOM tree라는 객체 트리로 구조화
  > 객체 간 상속 구조가 존재한다.

### DOM 핵심
- 문서의 요소들을 **객체**로 제공하여 **다른 프로그래밍 언어에서 접근하고 조작**할 수 있는 방법을 제공하는 API

### document 객체
- 웹 페이지 객체
- DOM Tree 진입점
- 페이지를 구성하는 모든 객체 요소를 포함

#### 예시
- HTML의 <title> 변경하기
  ```javascript
  document.title = 'Hello :)'
  ```

## DOM 선택과 조작
> 웹 페이지를 조작한다는 것은 웹 페이지를 **동적**으로 만든다는 것이다.

### 순서
1. 조작하고자 하는 요소를 **선택**
2. 선택된 요소의 콘텐츠 또는 속성을 **조작**

## DOM 선택
### 선택 메서드
- `document.querySelector(selector)`
  - 제공한 선택자와 일치하는 element **한 개** 선택
  - 제공한 선택자를 만족하는 **첫 번째** element 객체를 반환
  - 없으면 null 반환
- `document.queyrSelectorAll(selector)`
  - 제공한 선택자와 일치하는 **여러** element 선택
  - 제공한 선택자를 만족하는 **NodeList**를 반환

#### 예시
```html
<body>
  <h1 class="heading">DOM 선택</h1>
  <a href="https://www.google.com/">google</a>
  <p class="content">content1</p>
  <p class="content">content2</p>
  <p class="content">content3</p>
  <ul>
    <li>list1</li>
    <li>list2</li>
  </ul>
  <script>
    console.log(document.querySelector('.heading'))
    // 출력 : <h1 class="title heading">DOM 선택</h1>

    console.log(document.querySelector('.content'))
    // 출력 : <p class="content">content1</p>
    // 맨 처음 content 클래스를 출력

    console.log(document.querySelectorAll('.content'))
    // 출력 :
    // 0: p.content
    // 1: p.content
    // 2: p.content
    //  length: 3
    // [[Prototype]]: NodeList

    // Node리스트의 형태로 객체 명과 그 클래스가 출력된다.

    console.log(document.querySelectorAll('ul > li'))
    // 출력 :
    // 0: li
    // 1: li
    //  length: 2
    // [[Prototype]]: NodeList
```

## DOM 조작
- 속성 조작
  - 클래스 속성 조작
  - 일반 속성 조작
- HTML 콘텐츠 조작
- DOM 요소 조작
- 스타일 조작

### 속성 조작
1. 클래스 속성 조작
   - `classList` property : 요소의 클래스 목록을 DOMTokenList (*유사 배열*) 형태로 반환
   
   #### classList method
   - `element.classList.add()`
     - 지정한 클래스 값을 추가
   - `element.classList.remove()`
     - 지정한 클래스 값을 제거
   - `element.classList.toggle()`
     - 클래스가 존재한다면 제거 후 False 반환
     - 클래스가 존재하지 않으면 추가 후 True 반환
2. 일반 속성 조작
   #### 일반 속성 조작 method
   - `element.getAttribute()`
     - 해당 요소에 지정된 값을 반환
   - `element.setAttribute(name, value)`
     - 지정된 요소의 속성 값을 설정
     - 속성이 이미 있으면 기존 값을 갱신
     - 속성이 없으면 지정된 이름과 값으로 새 속성이 추가
   - `element.removeAttribute()`
     - 요소에서 지정된 이름을 가진 속성 제거

### HTML 콘텐츠 조작
- `textContent` property : 요소의 텍스트 콘텐츠를 표현

  #### 예시
  ```html
  const h1Tag = document.querySelector('.heading')

  <!-- HTML 콘텐츠 조작 -->
  h1Tag.textContent = '내용 수정'
  console.log(h1Tag.textContent)
  ```

### DOM 요소 조작
  #### DOM 요소 조작 메서드
  - `document.createElement`(tagName)`
    - 작성한 tagName의 HTML 요소를 생성하여 반환
  - `Node.appendChild()`
    - 한 Node를 특정 부모 Node의 자식 NodeList의 마지막에 삽입
    - 추가된 Node 객체 반환
  - `Node.removeChild()`
    - DOM에서 자식 Node 제거
    - 제거된 Node 반환
  
  #### 예시
  ```html
  <!-- 생성 -->
  const h1Tag = document.createElement('h1')
  h1Tag.textContent = '제목'

  <!-- 추가 -->
  const divTag = document.querySelector('div')
  divTag.appendChild(h1Tag)

  <!-- 삭제 -->
  const pTag = document.querySelector('p')
  divTag.removeChild(pTag)
  ```

### style 조작
- `style` property : 해당 요소의 모든 style 속성 목록을 포함하는 속성

#### 예시
```html
const pTag = document.querySelector('p')

pTag.style.color = 'crimson'
pTag.style.fontSize = '2rem'
pTag.style.border = '1px solid black`
```


## 참고
### Node
- DOM의 기본 구성 단위
- DOM 트리의 각 부분은 Node라는 객체로 표현
  - Document Node => HTML 문서 전체
  - Element Node => HTML 요소
  - Text Node => HTML 텍스트
  - Attribute Node = 'HTML 요소의 속성

### NodeList
- DOM 메서드를 사용해 선택한 Node의 목록
- 배열과 유사한 구조
- index 형태로만 각 항목에 접근 가능
- JavaScpipt의 배열 메서드 사용 가능
- `querySelectorAll()`에 의해 반환되는 NodeList는 DOM의 변경사항을 실시간으로 반영하지 않음
  - DOM이 나중에 변경되더라도 이전에 이미 선택한 NodeList 값은 변하지 않음

### Element
- Node의 하위 유형
- DOM 트리에서 HTML 요소를 나타내는 특별한 유형의 Node
- Node의 속성과 메서드 및 특화 기능을 가지고 있음
  > 모든 Element는 Node

### Parsing
브라우저가 문자열을 해석해서 DOM Tree로 만드는 과정

### JS에서의 세미콜론
- JavaScript 문장 마지막에는 ';'이 들어감
  - 선택적으로 사용 가능
  - 없으면 '*자동 세미콜론 삽입 규칙*'에 의해 자동으로 세미콜론 삽입

### 변수 선언 키워드 var
- ES6 이전 변수 선언 키워드
- 재할당 가능
- 재선언 가능
- 함수 스코프를 가짐
  > 함수의 중괄호 내부
  > 바깥에서는 접근 불가능
- 선언하기 전 사용할 수 있는 "호이스팅"이 되는 특성으로 예기치 못한 문제 발생 가능
  > 호이스팅 :<br>
  > 변수 선언이 끌어올려지는 현상
  >
  > var로 선언한 변수는 선언 위치와 상관 없이 함수에서는 시작 지점에서, 전역에서는 코드가 시작될 때 처리됨
- 변수 선언 시 키워드를 사용하지 않으면 자동으로 var로 선언됨
