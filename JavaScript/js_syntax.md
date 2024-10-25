# 자바스크립트 문법
## 데이터 타입

|**원시 자료형**|**참조 자료형** (*Objects*)|
|:--------:|:--------:|
|Number|Object|
|String|Array|
|Boolean|Function|
|null||
|undefined||

- 원시 자료형 : 변수에 값이 직접 저장되는 자료형
  > 불변 - 값 복사
- 참조 자료형 : 객체의 주소가 저장되는 자료형
  > 가변 - 주소 복사

### 원시 자료형
1. `Number` : 정수 또는 실수형 숫자를 표현하는 자료형
   > 무한대 : `Infinity`
   >
   > Not a Number : `NaN`

2. `String` : 텍스트 데이터를 표현하는 자료형
   > `+` 연산자를 사용해 문자열끼리 결합
   >
   > 그 외 사칙연산 기호는 사용 불가능

   - Template literals
     - 내장된 표현식을 허용하는 문자열 작성 방식
     - 백틱 사용
     - 표현식은 `${expression}`으로 표기
     - ES6+ 부터 지원

3. `null` : 프로그래머가 의도적으로 **값이 없음**을 나타낼 때 사용

4. `undefined` : 시스템이나 JavaScript 엔진이 **값이 할당되지 않음**을 나타낼 때 사용

5. `Boolean` : true/false
   > 조건문 또는 반복문에서 Boolean이 아닌 데이터 타입은 "자동 형변환 규칙"에 따라 true나 false로 변환된다.

   - 자동 형변환

     |데이터 타입|`false`|`true`|
     |:-------:|:-----:|:----:|
     |`undefined`|항상 false|x|
     |`null`|항상 false|x|
     |`Number`|0, -0, NaN|그 외|
     |`String`|'' 빈 문자열|그 외|

## 연산자
- 할당 연산자
  - `=`
- 증가 & 감소 연산자
  - `++` : 피연산자를 1 증가시킴
    > 연산자의 위치에 따라 증가하기 전이나 후의 값을 반환
  - `--` : 피연산자를 1 감소시킴
    > 연산자의 위치에 따라 감소하기 전이나 후의 값을 반환

    ```javascript
    let x = 3
    const y = x++
    // x = 3, y = 4

    let a = 3
    const b = ++a
    // a = 4, b = 4
    ```

- 비교 연산자
  - `<`, `>` : 피연산자들을 비교하고 결과 값을 boolean으로 반환

    ```javascript
    3 > 2 // true
    'A' < 'B' // true
    'Z' < 'a' // true
    '가' < '나' // true

- 동등 연산자
  - `==` : 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean을 반환
    > '암묵적 타입 변환'으로 타입을 일치시킨 후 같은 값인지 비교
    >
    > 두 피연산자가 모두 객체일 경우 주소가 같은지 판별

- 일치 연산자
  - `===` : 두 연산자의 값과 타입이 모두 같은 경우 true 반환
    > 같은 객체를 가리키거나, 같은 타입이면서 같은 값인지를 비교
    >
    > 암묵적 타입 변환이 일어나지 않음
    >
    > 특수 경우를 제외하고 **일치 연산자 사용 권장**

- 논리 연산자
  - `&&` : and
  - `||` : or
  - `!` : not
    > 단축 평가를 지원한다.

## 조건문
### JavaScript의 if문
  #### 예시
  ```javascript
  if (name === 'admin') {
    ...
  } else if (name === 'customer') {
    ...
  } else {
    ...
  }
  ```
### 삼항 연산자
  #### 예시
  ```javascript
  condition ? expression1 : expression2
  ```
  - condition
    - 평가할 조건
  - expression1
    - 조건이 true일 경우 반환값 또는 표현식
  - expression2
    - 조건이 false일 경우 반환값 또는 표현식

## 반복문
### while
- 조건문이 참이면 문장을 계속해서 수행
  ```javascript
  while (condition) {
    ...
  }
  ```

### for
- 특정 조건이 거짓으로 판별될 때까지 반복
  ```javascript
  for ([초기문]; [조건문]; [증감문]) {
    ...
  }
  // 실행순서
  // 1. 초기문
  // 2. 조건문
  // 3. for문 내용
  // 4. 증감문
  ```

### for in
- 객체의 열거 가능한 속성에 대한 반복
  ```javascript
  for (variable in object) {
    statement
  }
  ```

### for of
- 반복 가능한 객체에 대한 반복
  ```javascript
  for (variable of iterable) {
    statement
  }
  ```

### for in과 for of
- 객체 관점에서 배열의 인덱스는 *정수 이름을 가진 열거 가능한 속성*
  - `for in`은 배열에서 열거 가능한 속성인 인덱스를 반환
    > 반복자가 아닌 단순 열거이므로 특정 순서로 반환받는다를 보장할 수 없다.
  - `for of`가 배열에 있는 값을 반환

따라서,
- `for in`은 인덱스의 순서가 중요한 **배열에서 사용하지 않음**
- `for of`는 순서가 없는 **Object에서 사용하지 않음**

### 반복문에서의 const
- for문
  - 최초 정의한 i를 **재할당**하면서 사용하기 때문에 **const 사용 시 오류 발생**
- for in문, for of문
  - 매번 다른 속성 이름이 변수에 지정되므로 **const를 사용해도 에러가 발생하지 않음**
  - 그러나 const 특성상 블록 내부에서 변수를 수정할 수 없음

### 반복문 종합

|키워드|특징|
|:---:|:--:|
|`while`|.|
|`for`|.|
|`for in`|object 순회|
|`for of`|iterable 순회|

> 모두 블록 스코프

## 참조 자료형
### 함수
- 모든 함수는 `Function object`

#### 함수 정의
```javascript
function name ([param[, param, [..., param]]]) {
  statements
  return value
}
```
> return 값이 없다면 undefined를 반환

#### 함수 정의 방법
- 선언식
  ```javascript
  function funcName () {
    statements
  }
  ```
  > 호이스팅 가능
  >
  > 코드의 구조와 가독성 면에서 상대적인 장점이 있다.

- 표현식
  ```javascript
  const funcName = function () {
    statements
  }
  ```
  > 호이스팅 되지 않음
  >
  > 함수 이름이 없는 '익명 함수'를 사용할 수 있다.

#### 표현식 사용 권장 이유
- 예측 가능성
  - 호이스팅의 영향을 받지 않아 코드의 실행 흐름을 더 명확하게 예측할 수 있음
- 유연성
  - 변수에 할당되므로 함수를 값으로 다루기 쉬움
- 스코프 관리
  - 블록 스코프를 가지는 let이나 const와 함께 사용하여 더 엄격한 스코프 관리 가능

#### 매개변수
1. 기본 함수 매개변수
   - 전달하는 인자가 없거나 undefine가 전달될 경우 이름 붙은 매개변수를 기본값으로 초기화
   ```javascript
   const funcName = function (name = 'name') {
    ...
    return ...
   }
   ```

2. 나머지 매개변수
   - 임의의 수의 인자를 '배열'로 허용하여 가변 인자를 나타내는 방법
     > 작성 규칙
     > - 함수 정의 시 나머지 매개변수는 하나만 작성 가능
     > - 나머지 매개변수는 함수 정의에서 매개변수 마지막에 위치해야 함

#### 매개 변수와 인자 개수 불일치 경우
- 매개변수가 더 많을 경우
  - 누락된 인자는 `undefined` 할당
- 인자가 더 많을 경우
  - 초과 입력한 인자는 사용하지 않음

#### Spread syntax
- `...` : 전개 구문
  - 반복 가능한 항목을 펼치는 것
  - 전개 대상에 따라 역할이 다름
    > 배열이나 객체의 요소를 **개별적인 값으로 분리**<br>
    > 다른 배열이나 객체의 요소를 현재 배열이나 객체에 **추가**

<br>

- 전개 구문 활용처
  1. 함수와의 사용
     - 함수 호출 시 인자 확장
       ```javascript
       function myFunc(x, y, z) {
        return x + y + z
       }

       let numbers = [1, 2, 3]

       console.log(myFunc(...numbers)) // 6
       // 파이썬의 `*`의 느낌이다.
       ```
     - 나머지 매개변수 (압축)
       ```javascript
       function myFunc(x, y, ...restArgs) {
        return [x, y, restArgs]
       }

       console.log(myFunc(1, 2, 3, 4, 5)) // [1, 2, [3, 4, 5]]
       console.log(myFunc(1, 2)) // [1, 2, []]
       ```
  2. 객체와의 사용
  3. 배열과의 활용처

#### 화살표 함수 표현식
- 함수 표현식의 간결한 표현법
```javascript
// 일반적인 함수
const arrow = function (name) {
  return `hello, ${name}`
}

// 화살표 함수
const arrow = name => `hello, ${name}`
```

- 작성 과정
  ```javascript
  const arrow = function (name) {
    return `hello, ${name}`
  }
  ```

  1. `function` 키워드를 제거하고 매개변수와 중괄호 사이에 `=>` 작성
      ```javascript
      const arrow = (name) => {return `hello, ${name}`}
      ```

  2. 함수 매개변수가 하나 뿐일 때, `()` 제거 가능
     > 생략하지 않는 것을 권장
      ```javascript
      const arrow = name => { return `hello, ${name}` }
      ```

  3. 함수 본문 표현식이 한 줄이면, `{}`와 `return` 제거 가능
      ```javascript
      const arrow = name => `hello, ${name}`
      ```

## 객체
키로 구분된 데이터 집합을 저장하는 자료형

### 객체 구조
- 중괄호로 작성
- `key: value` 쌍으로 구성된 속성을 여러 개 작성 가능
- key는 문자형만 허용
- value 모든 자료형 허용

### 속성 참조
- `.` 또는 `[]`로 객체 요소에 접근
- key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능
```javascript
// 조회
console.log(user.name)
console.log(user[name])

// 추가
user.address = 'Korea'

// 수정
user.name = 'Bella'

// 삭제
delete user.name
```

### `in` 연산자
- 속성이 객체에 존재하는지 여부를 확인

### 메서드
- 객체 속성에 정의된 함수
  > `object.method()` 방식으로 호출
  
  > `this` 키워드를 사용해 객체에 대한 특정한 작업을 수행할 수 있다.

- `this` 키워드
  - 함수나 메서드를 호출한 객체를 가리키는 키워드
    > 함수 내에서 객체의 속성 및 메서드에 접근하기 위해 사용

  ```javascript
  const person = {
    name: 'Alice',
    greeting: function () {
      return `Hello my name is ${this.name}`
    },
  }

  console.log(person.greeting())
  ```
  - `this`는 **함수 호출 방법**에 따라 가리키는 대상이 달라짐

    |호출 방법|대상|
    |:------:|:--:|
    |단순 호출|전역 객체|
    |메서드 호출|메서드를 호출한 객체|

  1. 단순 호출
     ```javascript
     const myFunc = function () {
      return this // window
     }
     ```
  2. 메서드 호출
     ```javascript
     const myObj = function () {
      data: 1,
      myFunc: function () {
        return this // myObj
      }
     }
     ```

  #### 중첩된 함수에서 this 문제점
  - `forEach()`의 경우 일반적인 함수 호출이므로 this가 전역을 가리킴
  - **화살표 함수는 자신만의 this를 가지기 때문에** 외부 함수에서의 this 값을 가져옴

  #### `this` 정리
  - 함수가 호출될 때 암묵적으로 this를 전달 받음
  - this는 함수가 호출되는 방식에 따라 결정되는 현재 객체를 나타냄
  - Python의 `self`와 Java의 `this`가 선언 시 이미 값이 정해지는 반면, JavaScript의 `this`는 **함수가 호출되기 전까지 값이 할당되지 않고 호출 시에 결정**됨
    > 동적 할당
    - 장점 : 함수를 하나만 만들어 여러 객체에서 재사용할 수 있다.
    - 단점 : 위와 같은 유연함이 실수로 이어질 가능성이 있다.
      > 따라서 this의 동작 방식을 충분히 이해하는 것이 중요!!!

### 추가 객체 문법
- 단축 속성
  - key 이름과 value에 사용하는 이름이 같은 경우
    ```javascript
    const name = 'Alice'
    const age = 30

    const user = {
      name, // name = name
      age, // age = age
    }
    ```
  - 메서드 선언 시 function 키워드 생략 가능
    ```javascript
    const myObj = {
      myFunc() {
        return 'Hello'
      }
    }
    ```

- 계산된 속성
  - 키가 `[]`로 둘러싸여 있는 속성
    > 고정값이 아닌 변수 값을 사용 가능하다.
    ```javascript
    const front = 'my'
    const rear = 'property'

    const bag = {
      [front + rear]: 'value',
    }

    console.log(bag) // {myproperty: 'value'}
    ```

- 구조 분해 할당
  - 배열 또는 객체를 분해하여 객체 속성을 변수에 쉽게 할당하는 문법
    ```javascript
    const userInfo = {
      name: 'Alice',
      userId: 'alice123',
      email: 'alice123@gmail.com'
    }

    const {name} = userInfo
    const {name, userId} = userInfo
    const {name, userId, email} = userInfo
    // name, userId, email 순서
    ```
    - 함수의 매개변수로 객체 구조 분해 할당 활용 가능
    ```javascript
    const person = {
      name: ...,
      age: ...,
      city: ...,
    }

    function printInfo({ name, age, city }) {
      ...
    }
    ```

- 복사
  - 얕은 복사를 아래와 같이 진행 가능
    ```javascript
    const obj = {b: 2, c: 3, d: 4}
    const newObj = {a: 1, ...obj, e: 5}

    // 출력 :
    // {a: 1, b: 2, c: 3, d: 4, e: 5}
    ```

- 유용한 객체 메서드
  - `Object.keys(object)` : key 값들을 리스트로 반환
  - `Object.values(object)` : value 값들을 리스트로 반환

- Optional chaining
  - 속성이 없는 중첩 객체를 에러 없이 접근할 수 있는 방법
  - 만약 참조 대상이 null 또는 undefined라면 에러가 발생하는 것 대신 **평가를 멈추고 undefined를 반환**
  - 사용하지 않는다면, `&&` 연산자를 사용해야 함
    ```javascript
    const user = {
      name: ...,
      greeting: function () {
        ...,
      }
    }

    console.log(user.address && user.address.street) // undefined
    ```

  - 장점 :
    - 참조가 누락될 가능성이 있는 경우, 이를 확인하기 위해 접근 시 더 짧고 간단한 표현식을 작성할 수 있음
    - 어떤 속성이 필요한지에 대한 보증이 확실하지 않은 경우에 객체의 내용을 보다 편리하게 탐색 가능
  
  - 주의사항 :
    - 존재하지 않아도 괜찮은 대상에만 사용
      - `?.` 왼쪽 평가 대상이 없어도 괜찮은 경우만 선택적으로 사용
      - 중첩 객체를 에러 없이 접근하는 것이 목표임을 상기
    - `?.` 앞에는 무조건 변수가 선언되어 있어야 함

  - 정리:
    1. `obj?.prop` : obj가 존재하면 obj.prop을 반환하고, 그렇지 않으면 undefined 반환
    2. `obj?.[prop]` : obj가 존재하면 obj[prop]을 반환하고, 그렇지 않으면 undefined 반환
    3. `obj?.method()` : obj가 존재하면 obj.method()를 호출하고, 그렇지 않으면 undefined 반환

## JSON
Key-Value 형태로 이루어진 자료 표기법
- Object와 유사한 구조이나, JSON은 형식이 있는 **문자열**
- JavaScript에서 JSON을 사용하기 위해서는 Object 자료형으로 변경 필수

```javascript
const obj = {
  name: 'Alice',
  hobby: 'reading',
}

// Object -> JSON
const objToJson = JSON.stringify(obj)
// 출력 :
// {"name": "Alice", "hobby": "reading}

// JSON -> Object
const jsonToObj = JSON.parse(objToJson)
// 출력 :
// {name: 'Alice', hobby: 'reading'}
```

## 배열
순서가 있는 데이터 집합을 저장하는 자료구조
- 대괄호로 작성
- 요소 자료형은 제약 없음
- `length` 속성으로 배열에 담긴 요소 개수 확인 가능

### 주요 메서드

|위치|메서드|역할|
|:-:|:----:|:-:|
|배열 끝|`push`|추가|
||`pop`|삭제|
|배열 앞|`unshift`|추가|
||`shift`|제거|

> 모든 제거 메서드는 그 값을 반환한다.

## Array Helper Methods
배열 조작을 보다 쉽게 수행할 수 있는 특별한 메서드 모음
- 배열의 각 요소를 **순회**하며 그에 대한 함수를 호출
- 따라서, 인자로 함수(**콜백함수**)를 받음

### 콜백 함수
- 다른 함수에 인자로 전달되는 함수
  > 외부 함수 내에서 호출되어 일종의 루틴이나 특정 작업을 진행

#### forEach
- 배열의 각 요소를 반복하며, 모든 요소에 대해 함수를 호출
- 구조
  - `arr.forEach(callback(item[, index[, array]]))`
    1. `item` : 처리할 배열의 요소
    2. `index` : 처리할 배열 요소의 인덱스
    3. `array` : forEach를 호출한 배열 (arr)
     > index와 array는 선택 인자이다.
  - 반환 값은 **undefined**

#### map
- 배열의 모든 요소에 대해 함수를 호출하고, 반환 된 호출 값을 모아 **새로운 배열을 반환**
- 구조
  - `arr.map(callback(item[, index[, array]]))`
  - 반환 값은 각 요소에 실행한 callback 함수의 **결과 모음 배열**
- python `map`과의 비교
  ```python
  new_iter = list(map(function, iterable))
  ```
  ```javascript
  const new_array = object.map(callBackFunction)
  ```
  - python과 javascript 모두 반복 객체의 각 요소에 함수를 적용한다는 점은 동일
  - python은 map의 인자 iterable의 각 요소에 function 함수에 인자로 넘김
  - javascript는 object의 각 요소를 map의 인자 callBackFunction 함수에 인자로 넘김

### 배열 순회 종합

|방식|특징|탈출 키워드 가능|비고|
|:-:|:--:|:--:|
|`for loop`|배열의 인덱스를 이용하여 각 요소에 접근|O||
|`for of`|배열 요소에 바로 접근 가능|O||
|`forEach()`|간결하고 가독성이 높음<br>콜백함수를 이용하여 각 요소를 조작하기 용이|X|사용 권장|

### 기타 Array Helper Methods

|메서드|역할|
|:---:|:--:|
|`filter`|콜백 함수 반환 값이 참인 요소들만 모아서 새로운 배열 반환|
|`find`|콜백 함수 반환 값이 참이면 해당 요소를 반환|
|`some`|배열 요소 중 **하나라도 콜백 함수를 통과**하면, true를 반환하고 배열 순회 중지|
|`every`|배열 **모든 요소가 콜백 함수를 통과**하면, true를 반환|

### 전개 구문을 이용한 배열
- 배열 복사
  ```javascript
  let parts = ['어깨', '무릎']
  let lyrics = ['머리', ...parts, '발']

  // 출력 : ['머리', '어깨', '무릎', '발']
  ```

## 참고
### NaN를 반환하는 예시
1. 숫자로서 읽을 수 없을 때
   - `Number(undefined)`
2. 결과가 허수인 수학 계산식
   - `Math.sqrt(-1)`
3. 피연산자가 NaN
   - `7 ** NaN`
4. 정의할 수 없는 계산식
   - `0 * Infinity`
5. 문자열을 포함하면서 덧셈이 나닌 계산식
   - `'가' / 3`

### null과 undefined
1. 역사
   - `null`은 처음부터 존재했으며, '객체가 없음'을 나타내기 위해 도입
   - `undefined`는 나중에 추가되어 '값이 할당되지 않음'을 나타내기 위해 도입
2. null의 타입이 Object인 이유
   - 초기 버전에서 값의 타입을 나타내기 위해 32비트 시스템 사용
   - 타입 태그로 하위 3비트 사용
     > `000` : 객체
   - null은 모든 비트가 0인 특별한 값으로 표현되었고, 그로 인해 하위 비트가 객체와 동일해져 잘못 해석됨
3. ECMAScript의 표준화
   - ECMAScript 명세에서는 null을 원시 자료형으로 정의
   - 그러나 위의 이유로 null이 object 형을 유지
   - 기존 웹사이트들의 호환성 문제로 수정하지 못함

### 화살표 함수 심화
1. 인자가 없다면 `()` 또는 `_`로 표시 가능
   ```javascript
   const noArgs1 = () => 'No args'
   const noArgs2 = _ => 'No args'
   ```
2. object의 return
   1. object를 return 한다면, return을 명시적으로 작성
      ```javascript
      const returnObject = () => { return { key: 'value' } }
      ```
   2. return을 작성하지 않으려면 객체를 소괄호로 감쌈
      ```javascript
      const returnObject = () => ({ key: 'value' })

### 클래스
- 객체를 생성하기 위한 템플릿
  > 객체의 속성, 메서드를 정의하는 청사진 역할

#### 기본 문법
- 클래스 생성
  ```javascript
  class MyClass {
    constructor() { ... } // 생성자 메서드
    method() { ... }
    method2() { ... }
  }

  // constructor(name, age) {
  //  this.name = name,
  //  this.age = age
  // }
  // 객체 생성 방식을 객체 지향적으로 표현하고 싶어서 만들어진 생성자 메서드
  // 그래서 클래스는 내부적으로 생성자 함수를 기반으로 동작한다.
  ```
- 클래스 활용
  ```javascript
  class MyClass {
    constructor(name, age) {
      this.name = name,
      this.age = age
    }
    sayHi() {
      console.log(`Hello, ${this.name}!`)
    }
  }

  const member1 = new MyClass('Alice', 30)
  // 객체를 클래스에 기반하여 생성
  ```

#### `new` 연산자
- 클래스나 생성자 함수를 사용하여 새로운 객체를 생성
  > 클래스의 생성자 메서드는 new 연산자에 의해 자동으로 호출한다.

  > 특별한 절차 없이 객체를 초기화 할 수 있다.

  > new 없이 클래스를 호출하면 `TypeError` 발생

### 콜백 함수의 이점
1. 함수의 재사용성 측면
   - 콜백 함수의 동작을 자유롭게 변경 가능

2. 비동기적 측면
   - 코드의 순서대로 작동하지 않도록 할 수 있음
     - `setTimeout()` : n 밀리초 후에, 인자 함수 실행
   - 특정 작업을 다른 곳으로 넘기고, 그 이후의 코드를 우선 실행
     - 다른 코드의 실행을 방해하지 않음
     - `Call Stack`으로 넘김
   > 처리 속도가 늦는 작업은 뒤로 미루고, 다른 작업을 먼저 진행 할 수 있다.

   > 병렬적으로 작업을 처리한다.

### 배열과 객체
- 배열도 키와 속성들을 담고 있는 참조 타입의 객체
- 배열의 키는 숫자
  > 숫자형 키를 사용하여, 객체 기본 기능 이외에도 
  > **순서가 있는 컬렉션**을 제어하게 해주는 특별한 메서드를 제공하는 것이다.
- 배열의 길이인 length가 속성으로 존재
  > 그래서 `arr.length`로 간단히 배열의 길이를 알 수 있다.