# Controlling event
## 이벤트
- 웹에서의 이벤트
  - 화면 스크롤
  - 버튼 클릭 시 팝업 창 출력
  - 드래그 앤 드롭
  - 키보드 입력에 따른 새로운 요소 생성

### event 객체
- 무언가 일어났다는 신호나 사건
  > 모든 DOM 요소가 이러한 event를 만들어 낸다.

#### event object
- DOM에서 이벤트가 발생했을 때 생성되는 객체
  > 이벤트 종류
  > - mouse, input, keyboard, touch 등...

#### - Dom 요소에서 이벤트가 발생하면, 해당 event는 연결된 event handler에 의해 처리된다.

### event handler
- 특정 이벤트가 발생했을 때 실행되는 함수
  > 사용자의 행동에 어떻게 반응할지를 JavaScript 코드로 표현한 것이다.

#### `.addEventListener()`
- 대표적인 이벤트 핸들러 중 하나
  > 특정 이벤트를 DOM 요소가 수신할 때마다 콜백 함수를 호출한다.

  <br>`EventTarget.addEventListener(type, handler)`
  - DOM 요소 : EventTarget
  - 수신할 이벤트 : type
    - 수신할 이벤트 이름
    - 문자열로 작성
  - 콜백 함수 : handler
    - 발생한 이벤트 객체를 수신하는 콜백 함수
    - 이벤트 핸들러는 자동으로 event 객체를 매개변수로 받음

  > **대상**에 **특정 이벤트**가 발생하면, **지정한 이벤트를 받아 할 일**을 등록한다.

### addEventListener 활용
- 요소에 `addEventListener`를 연결하게 되면 내부의 this 값은 연결된 요소를 가리키게 됨
  > 콜백 함수의 event 객체의 currentTarget 속성 값(*event.currentTarget*)과 동일

#### 콜백 함수 특징
- 이벤트 핸들러 내부의 this는 이벤트 리스너에 연결된 요소를 가리킴
- 이벤트가 발생하면 event 객체가 생성되어 첫 번째 인자로 전달
- 반환 값 없음

## 버블링
- 한 요소에 이벤트가 발생하면, 그 요소에 할당된 핸들러가 동작하고 이어서 부모 요소의 핸들러가 동작하는 현상
  > 최상단 조상 요소인 document를 만날 때까지 이 과정이 반복된다.

### currentTarget & target 속성
- `currentTarget`
  - '현재' 요소
  - 항상 이벤트 핸들러가 연결된 요소만을 참조하는 속성
  - `this`와 동일
- `target`
  - 이벤트가 발생한 가장 안쪽의 요소를 참조하는 속성
  - 실제 이벤트가 시작된 요소
  - 버블링이 진행되어도 변하지 않음

### 캡처링과 버블링
- 캡처링 : 이벤트가 하위 요소로 전파되는 단계 (*버블링 반대*)
  - table의 하위 요소 td를 클릭하면 이벤트는 먼저 최상위 요소부터 아래로 전파됨
  - 실제 이벤트가 발생한 지점에서 실행된 후 다시 위로 전파
    > 이 과정에서 상위 요소에 할당된 이벤트 핸들러들이 호출
  - 캡처링은 실제 개발자가 다루는 경우가 거의 없음
    > 버블링에 집중

### 버블링의 필요성
> 수많은 버튼들에 1:1로 이벤트 핸들러를 할당하는 것은 낭비이다.
- 각 버튼의 공통 조상 요소에 **이벤트 핸들러 단 하나만 할당**하기
  > 여러 버튼 요소에서 발생하는 이벤트를 한 번에 다룰 수 있다.
  >
  > `event.target`을 이용하면 실제 어느 버튼에서 이벤트가 발생했는지 알 수 있다.

## event handler 활용
1. click 이벤트
    ```javascript
    // 1. 초기값 할당
    let counterNumber = 0

    // 2. 버튼 요소 선택
    const btn = document.querySelector('#btn')

    // 3. 콜백 함수 (버튼에 클릭 이벤트가 발생할때마다 실행)
    const clickHandler = function () {
      counterNumber += 1

      // 출력 요소 선택
      const spanTag = document.querySelector('#counter')

      // 요소의 컨텐츠를 1 증가한 초기값으로 설정
      spanTag.textContent = counterNumber
    }

    // 4. 버튼에 이벤트 핸들러 부착 ( 클릭 이벤트)
    btn.addEventListener('click', clickHandler)
    ```
2. input 이벤트
   ```javascript
   // 1. input 요소 선택
   const inputTag = document.querySelector('#text-input')

   // 2. p 요소 선택
   const pTag = document.querySelector('p')

   // 3. 콜백 함수
   const inputHandler = function (event) {
    // 데이터 누적 위치 찾기
    console.log(event.currentTarget.value)
    // *** console.log(event)는 currentTarget이 이벤트 처리동안에만 사용할 수 있기에 currentTarget 키의 값은 null이된다.
    // currentTarget 이후의 속성 값들은 'target'을 참고한다.

    // p 요소 컨텐츠에 작성하는 데이터 추가
    pTag.textContent = event.currentTarget.value
   }

   // 4. input 요소에 이벤트 핸들러 부착
   inputTag.addEventListener('input', inputHandler)
   ```
3. click & input 이벤트
   ```javascript
   // input 구현
   const inputTag = document.querySelector('#text-input')
   const h1Tag = document.querySelector('h1')

   const inputHandler = function (event) {
    h1Tag.textContent = event.currentTarget.value
   }

   inputTag.addEventListener('input', inputHandler)

   // click 구현
   const btn = document.querySelector('#btn')

   const clickHandler = function () {
    h1Tag.classList.add('blue')
   }

   btn.addEventListener('click', clickHandler)
   ```
4. todo 실습
   ```javascript
   // 1. 필요한 요소 선택
   const inputTag = document.querySelector('.input-text')
   const btn = document.querySelector('#btn')
   const ulTag = document.querySelector('ul')

   const addTodo = function (event) {
    // 2.1 사용자 입력 데이터 저장
    const inputData = inputTag.value
    // 2.1.1 빈문자열 입력 방지
    if (inputData.trim()) {
      // 2.2 ~ 2.5 생성구문
    } else {
      alert('할 일을 입력하세요...')
      // 경고 대화상자 출력
    }

    // 2.2 데이터를 저장할 li 요소 생성
    const liTag = document.createElement('li')

    // 2.3 li 요소 컨텐츠에 데이터 입력
    liTag.textContent = inputData

    // 2.4 li 요소를 부모 ul 요소의 자식 요소로 추가
    ulTag.appendChild(liTag)

    // 2.5 todo 추가 후 input 입력 데이터 초기화
    inputTag.value = ''
   }

   inputTag.addEventListener('input', addTodo)
   ```
5. 로또 번호 생성기
   ```javascript
   const h1Tag = document.querySelector('h1')
   const btn = document.querySelector('#btn')
   const divTag = document.querySelector('div')

   // 1. 로또 번호 생성 함수
   const getLottery = Function (event) {
    const numbers = _.range(1, 46)

    // 6개 번호 추출
    const sixNumbers = _.sampleSize(numbers, 6)

    // 추출한 번호 배열을 반복하며 li 요소 생성
    sixnumbers.forEach((number) => {
      const liTag = document.createElement('li')
      liTag.textcontent = number

      // ul에 추가
      ulTag.appendChild(liTag)
    })

    // 완성된 ul 요소 div에 추가
    divTag.appendChild(ulTag)
   }

   // 2. 이벤트 핸들러 부착
   btn.addEventListener('click', getLottery)
   ```

#### lodash
- 모듈성, 성능 및 추가 기능을 제공하는 JavaScript 유틸리티 라이브러리
- 'array', 'object' 등 자료구조를 다룰 때 사용하는 유용하고 간편한 함수들을 제공

### 이벤트 기본 동작 취소하기
- HTML 각 요소가 기본적으로 가지고 있는 이벤트가 때로는 방해가 되는 경우가 있어 이벤트의 기본 동작을 취소할 필요가 있음

#### `.preventDefault()`
- 해당 이벤트에 대한 기본 동작을 실행하지 않도록 지정

#### 예시
- copy 이벤트 동작 취소
  ```javascript
  ...

  h1Tag.addEventListener('copy', function (event) {
    console.log(event)
    event.preventDefault()
    alert('복사 할 수 없습니다!')
  })
  ```
- form 제출 시 새로고침 동작(submit) 취소
  ```javascript
  const formTag = querySelector('#my-form')

  formTag.addEventHandler('submit', (event) => {
    event.preventDefault()
  })
  ```

## 참고
### addEventListener와 화살표 함수 관계