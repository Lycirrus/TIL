# vue 기본 문법
## Template Syntax
DOM을 기본 구성 요소 인스턴스의 데이터에 **선언적으로 바인딩**할 수 있는 HTML 기반 **템플릿 구문**을 사용

### Directive
- `v-` 접두사가 있는 특수 속성

#### 특징
- Directive의 속성 값은 단일 JavaScript 표현식
  > v-for, v-on 제외
- 표현식 값이 변경될 때 DOM에 반응적으로 업데이트를 적용

#### 전체 구문
`v-on:submit.prevent='onSubmit'`
- `v-on` : Name
- `submit` : Argument
  - 일부 directive 뒤에 ':'으로 표시되는 인자
- `Modifiers` : .prevent
  - '.'로 표시되는 특수 접미사
  - directive가 특별한 방식으로 바인딩되어야 함을 나타냄
- `Value` : onSubmit

## Dynamically data binding
### v-bind
- 하나 이상의 속성 또는 컴포넌트 데이터를 표현식에 동적으로 바인딩

### Attribute Bindings
- HTML의 속성 값을 Vue의 상태 속성 값과 동기화
  > 약어 : `:`(콜론)

#### Dynamic attribute name (동적 인자 이름)
- 대괄호로 감싸서 directive argument에 JavaScript 표현식을 사용하도록 함
- 표현식에 따라 동적으로 평가된 값이 최종 argument 값으로 사용<br>
`<button :[key]="myValue"></button`

### Class and Style Bindings
- 동적으로 문자열 값을 할당할 수 없는 class와 style 속성 값에 v-bind를 사용할 때, **객체** 또느 **배열**을 활용하여 작성하도록 하는 기능

#### 가능한 경우
1. Binding HTML Classes
   1. Binding to Objects
      - 객체를 :class에 전달하여 클래스를 동적으로 전환할 수 있음
      - 객체에 더 많은 필드를 포함하여 여러 클래스를 전환할 수 있음
      - 반드시 Inline 방식으로 작성할 필요 없음
      - 반응형 변수를 활용해 객체를 한번에 작성 가능

   2. Binding to Arrays
      - :class를 배열에 바인딩하여 클래스 목록을 적용할 수 있음
      - 배열 구문 내에서 객체 구문을 사용하는 경우

2. Binding Inline Styles
   1. Binding to Objects
      - :style은 JavaScript 객체 값에 대한 바인딩 지원
      - 실제 CSS에서 사용하는 것처럼 :style은 kebab-cased 키 문자열도 지원
      - 반드시 Inline 방식으로 작성할 필요 없음
      - 반응형 변수를 활용해 객체를 한번에 작성 가능
 
   2. Binding to Arrays
      - 여러 스타일 객체를 배열에 작성해서 :style을 바인딩할 수 있음
      - 작성한 객체는 병합되어 동일한 요소에 적용

## Event Handling
### v-on
- DOM 요소에 이벤트 리스너를 연결 및 수신
  > 약어 : `@`

#### 핸들러 종류
1. `Inline handlers` : 이벤트가 트리거 될 때 실행 될 JavaScript 코드
   - 주로 간단한 상황에 사용
2. `Method handlers` : 컴포넌트에 정의된 메서드 이름
   - Inline hanlers로는 불가능한 대부분의 상황에서 사용
   - 트리거하는 기본 DOM event 객체를 자동으로 수신

### Modifiers
#### Event Modifiers
- Event Modifiers를 활용해 `event.preventDefault()`와 같은 구문을 메서드에서 작성하지 않도록 함
- stop, prevent, self등 다양한 modifiers 제공
  > Modifiers는 chained 되도록 작성 가능하다.
  >> 작성된 순서대로 실행되므로 순서에 유의한다.

#### Key Modifiers
- 키보드 이벤트를 수신할 때 특정 키에 관한 별도 modifiers를 사용할 수 있음<br>
  `<input @keyup.enter="onSubmit">`



## From Input Bindings
form을 처리할 때 사용자가 input에 입력하는 값을 실시간으로 JavaScript 상태에 동기화해야 하는 경우
- 양방향 바인딩
  > 1. v-bind와 v-on을 함께 사용
  > 2. v-model 사용

### v-bind with v-on
1. v-bind를 사용하여 input 요소의 value 속성 값을 입력 값으로 사용
2. v-on을 사용하여 input 이벤트가 발생할 때마다 input 요소의 value 값을 별도 반응형 변수에 저장하는 핸들러 호출

### v-model
- form input 요소 또는 컴포넌트에서 양방향 바인딩을 만듦
  - 사용자 입력 데이터와 반응형 변수를 실시간 동기화
    ```javascript
    const inputText = ref('')

    // html

    <p> {{ inputText }}</p>
    <input v-model="inputText">
    ```

> IME가 필요한 언어(*ko, cn, jp*)의 경우 v-model이 제대로 업데이트되지 않는다.

> 해당 언어에 대해서는 v-bind와 v-on 방법을 사용해야 한다.

### v-model 활용
- 단순 Text input 뿐만 아니라 Checkbox, Raido, Select 등의 다양한 타입의 사용자 입력 방식과 함께 사용 가능

## 참고
### 접두어 `$`
- Vue 인스턴스 내에서 제공되는 내부 변수
  > 사용자가 지정한 반응형 변수나 메서드와 구분하기 위함이다.

  > 주로 Vue 인스턴스 내부 상태를 다룰 때 사용한다.

### IME (Input Method Editor)
- 사용자가 입력 장치에서 기본적으로 사용할 수 없는 문자를 입력할 수 있도록 하는 운영체제 구성 프로그램
  > IME가 동작하는 방식과 Vue의 양방향 바인딩 동작 방식이 상충하기 때문에 한국어 입력 시 예상대로 동작하지 않았다.