# 비동기
- 동기 : 프로그램의 실행 흐름이 순차적으로 진행
  > 하나의 작업이 완료된 후 다음 작업이 실행된다.

- 비동기 : 특정 작업의 실행이 완료될 때까지 기다리지 않고 다음 작업을 즉시 실행하는 방식
  > 작업의 완료 여부를 신경쓰지 않고 **동시에 다른 작업들을 수행할 수 있다**

#### 비동기 특징
- 병렬적 수행 
  - 빠르게 처리할 수 있는 작업을 먼저 처리
  - 시간이 필요한 작업들은 백그라운드에서 실행

## JavaScript와 비동기
- `Thread` : 작업을 처리할 때 실제로 작업을 수행하는 주체
  > JavaScript는 수행 주체가 하나인 Single Thread 언어이다.

### JavaScript Runtime
- JavaScript가 동작할 수 있는 환경(*Runtime*)
  > 브라우저 또는 Node.js
- Single Thread인 JavaScript가 비동기 처리를 할 수 있도록 도와주는 환경 필요

### 브라우저 환경에서의 JavaScript 비동기 처리 관련 요소
1. Call Stack
   - 기본적인 JavaScript의 Single Thread 처리
2. Web API
   - 브라우저에서 제공하는 runtime 환경
   - 시간이 소요되는 작업을 처리
3. Task Queue
   - 비동기 처리된 Callback 함수가 대기하는 Queue
4. Event Loop
   - 작업이 들어오길 기다렸다가 들어왔을 때 처리하고, 처리할 작업이 없는 경우엔 잠듦
     > 끊임없이 돌아가는 JavaScript 내 루프
   - Call Stack과 Task Queue를 지속적으로 모니터링
   - Call Stack이 비어 있으면 Task Queue에서 가장 오래 대기 중인 작업을 Call Stack으로 Push

#### 처리 동작 방식
1. 모든 작업이 **Call Stack**으로 들어간 후 처리
   > Call Stack은 LIFO 방식이다.
2. 오래 걸리는 작업이 Call Stack으로 들어오면 **Web API**로 보내 별도로 처리
3. Web API에서 처리가 끝난 작업들은 Call Stack으로 들어가는 대신 **Task Queue**에 순서대로 입력
   > Task Queue는 FIFO 방식이다.
4. **Event Loop**이 Call Stack이 비어 있는 것을 계속 확인하며, Call Stack이 비었다면 Task Queue에서 가장 오래된 작업을 Call Stack으로 보냄

## Ajax
비동기적인 웹 애플리케이션 개발을 위한 기술
  - 브라우저와 서버간의 데이터를 비동기적으로 교환하는 기술

  > Ajax를 사용하면 페이지 전체를 새로고침 하지 않아도 동적으로 데이터를 불러와 페이지를 갱신할 수 있다.

### Ajax 목적
1. 비동기 통신
   - 웹 페이지 전체를 새로고침하지 않고 서버와 데이터를 주고받을 수 있음
2. 부분 업데이트
   - 전체 페이지가 다시 로드되지 않고 HTML 페이지 일부 DOM만 업데이트
    - 페이지의 일부분만 동적으로 갱신할 수 있어 사용자 경험이 향상
3. 서버 부하 감소
   - 필요한 데이터만 요청하므로 서버의 부하를 줄일 수 있음

### XMLHttpRequest 객체
- 웹 브라우저와 서버 간의 비동기 통신을 가능하게 하는 JavaScript 객체

#### 기능
- JavaScript를 사용하여 서버에 HTTP 요청을 할 수 있는 객체
- 웹 페이지의 전체 새로고침 없이도 서버로부터 데이터를 가져오거나 보낼 수 있음
  > XML뿐만 아니라 모든 종류의 데이터를 가져올 수 있다.

### Axios
- 브라우저와 Node.js에서 사용할 수 있는 Promise 기반의 HTTP 클라이언트 라이브러리

#### 정의 및 특징
- 클라이언트 및 서버 사이에 HTTP 요청을 만들고 응답을 처리하는데 사용되는 JavaScript 라이브러리
- 서버와의 HTTP 요청과 응답을 간편하게 처리할 수 있도록 도와주는 도구
- 브라우저를 위한 XHR 객체 생성
- 간편한 API를 제공하며, Promise 기반의 비동기 요청을 처리
> 주로 웹 애플리케이션에서 서버와 통신할 때 사용

#### Ajax를 활용한 동작
1. XHR 객체 생성 및 요청
2. 응답 데이터 생성
3. JSON 데이터 응답
4. Promise 객체 데이터를 활용해 DOM 조작

#### Promise 객체
- JavaScript에서 비동기 작업을 처리하기 위한 객체
- 주요 메서드
  - `then()` : 작업이 성공적으로 완료되었을 때 실행될 콜백 함수 지정
    > 서버로부터 받은 응답 데이터를 처리 (*response*)
  - `catch()` : 작업이 실패했을 때 실행될 콜백 함수 지정
    > 네트워크 오류나 서버 오류 등의 예외 상황을 처리 (*error*)

> then()이 우선적으로 진행되며, 하나라도 실패하면 중단하고 catch()를 실행한다.

#### 예시
```javascript
axios({
  method: 'get',
  url: [url]
})
  .then((response) => {
    // 응답을 받았을 때 동작
  })
  .catch((error) => {
    // 에러가 발생했을 때 동작
  })
// 이 구문을 콜백함수에 넣어 이벤트 리스너로 사용할 수 있다.
```

### Ajax와 Axios
- Ajax
  - 비동기적인 웹 애플리케이션 개발에 사용되는 기술들의 집합을 지칭
- Axios
  - 클라이언트와 서버 사이에 HTTP 요청을 만들고 응답을 처리하는데 사용되는 JavaScript 라이브러리
  - Promise API 기반으로 비동기 처리를 더 쉽게 할 수 있다.
> 프론트엔드에서 Axios를 활용해 DRF로 만든 API 서버로 요청을 보내고, 받아온 데이터를 비동기적으로 처리하는 로직을 작성하게 된다.

> Frontend <=> (Axios) <=> Backend
- 결국, Ajax는 개념, Axios는 도구

## Callback과 Promise
> 비동기 처리의 어려움
> > 개발자 입장에서 **코드의 실행 순서가 불명확**하다는 단점이 존재한다.

- 비동기 처리 관리 방법
  1. 비동기 콜백
    - 비동기 작업이 완료된 후 실행될 함수를 미리 정의
  2. Promise
    - 비동기 작업의 최종 완료 또는 실패를 나타내는 객체

### 비동기 콜백
- 비동기적으로 처리되는 작업이 완료되었을 때 실행되는 함수
- 연쇄적으로 발생하는 비동기 작업을 **순차적으로 동작**할 수 있게 함
  > 작업 순서와 동작을 제어하거나, 결과를 처리하는 데 사용된다.

```javascript
const asyncTask = function (callback) {
  setTimeout(function () {
    console.log('비동기 작업 완료')
    callback()
  }, 2000)
}

// 콜백 실행
asyncTask(function () {
  console.log('콜백')
}

// 비동기 작업 완료
// 콜백

// 순으로 출력된다.
```

#### 한계
- 실행 결과를 받아서 다른 기능을 수행하기 위하여 사용됨
- 비슷한 패턴의 중복 발생
  > A 작업 후, a callback 실행<br>
  > a callback 실행 후, b callback 실행<br>
  > b callback 실행 후, c callback 실행...<br>
    - 콜백 지옥이 발생
    - 유지보수의 어려움 발생

### 프로미스
- JavaScript에서 비동기 작업의 결과를 나타내는 객체
  > 작업이 끝나면 실행시켜 준다는 약속이다.

#### Chaining
- then과 catch는 모두 항상 promise 객체를 반환
  > 계속되는 chaining을 할 수 있다.
  >> then을 계속 이어 나가면서 작성할 수 있다.
  `axios({}).then(...).then(...).catch(...)`

  > 이전 then의 반환 값이 다음 then의 인자로 전달된다.
- 비동기 작업의 **순차적인** 처리 가능
- 코드를 보다 직관적이고 가독성 좋게 작성할 수 있도록 도움

#### 장점
1. 가독성
   - 비동기 작업의 순서와 의존 관계를 명확히 표현할 수 있어 코드의 가독성 향상
2. 에러 처리
   - 각각의 비동기 작업 단계에서 발생하는 에러를 분할해서 처리 가능
3. 유연성
   - 각 단계마다 필요한 데이터를 가공하거나 다른 비동기 작업을 수행할 수 있어서 더 복잡한 비동기 흐름을 구성할 수 있음
4. 코드 관리
   - 비동기 작업을 분리하여 구성하면 코드를 관리하기 용이

#### 비동기 콜백과 비교하여 Promise의 이점
1. 실행 순서 보장
   - 콜백 함수: JavaScript의 Event Loop가 현재 실행 중인 Call Stack을 완료하기 전에는 호출되지 않음
   - Promise : Event Queue에 배치되는 순서대로 엄격하게 호출
   > 비동기 작업의 실행 순서를 더 예측 가능하게 만든다.
2. 유연한 비동기 처리
   - 비동기 작업이 완료된 후에도 then 메서드를 통해 콜백을 추가할 수 있음
3. Chaining을 통한 연속적인 비동기 처리
   - 여러 개의 콜백 함수를 순차적으로 실행할 수 있음
   - 각 콜백은 주어진 순서대로 실행
   - 이전 Promise 결과를 다음 then에서 사용 가능
   - 복잡한 비동기 로직의 명확성을 높임
4. 에러 처리 일원화
   - catch를 통해 체인 전체의 에러를 한 곳에서 처리 가능
