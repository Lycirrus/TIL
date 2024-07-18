# Modules & Control of flow
## Modules
### 모듈 활용
- 개요
  - 개발자가 프로그램 전체를 모두 혼자 힘으로 작성하는 것은 드문 일
  - 생산성 측면에서 다른 개발자가 이미 작성해 놓은 코드를 사용하는 것이 좋음

<br>
한 파일로 묶인 변수와 함수의 모음

- 특정한 기능을 하는 코드가 작성된 파이썬 파일

### 모듈 활용
  #### 모듈을 가져오는 방법
1. import문 사용
  - 모듈 명을 명시해야 함
  ```python
  import math

  print(math.sqrt(4))
  ```
2. from절 사용
  - 모듈 명을 명시하지 않음
  ```python
  from math import sqrt

  print(sqrt(4))
  ```
  - from절은 사용 함수가 모듈의 함수인지 개발자 본인이 만든 함수인지, 어떤 모듈의 함수인지를 알 수 없기 때문에 import문을 권장한다.
  #### 모듈 사용하기
  `.` *(dot)* 연산자는 점의 왼쪽 객체에서 점의 오른쪽 함수명을 찾으라는 의미
  #### 모듈 주의사항
  - 서로 다른 모듈이 같은 이름의 함수를 제공할 경우 문제 발생
  - 이 경우 마지막에 import된 함수로 기능함
    > 별칭을 지어줘야 함 => `as`
    ```python
    from math import sqrt
    from my_math import sqrt as my_sqrt
    ```

## 파이썬 표준 라이브러리
파이썬 언어와 함께 제공되는 다양한 모듈과 패키지의 모음

### 패키지
연관된 모듈들을 하나의 디렉토리에 모아 놓은 것<br>
`모듈 < 패키지 < 라이브러리`<br></br>

1. PSL 내부 패키지
  - 설치 없이 바로 import하여 사용

2. 외부 패키지
  - **<span style = "color:red">`pip`을 사용</span>** 하여 설치 후 import하여 사용

  #### pip
  - 외부 패키지들을 설치하도록 도와주는 파이썬의 패키지 관리 시스템
  - 기본 사용 시 전역 Scope에 설치됨
  - 일반적으로는 가상 환경을 만들어서 그곳에 설치

  #### 패키지 설치
  - 아래와 같은 3가지 방법이 있음
  1. 최신 버전
     ```python
     pip install <package> 
     ```
  2. 특정 버전
     ```python
     pip install <package>==1.0.5
     ```
  3. 최소 버전
     ```python
     pip install <package>>=1.0.4
     ```

  #### requests 패키지
  - 개발자의 요청을 외부 API로 보내는 패키지
  - `pip install requests`를 bash에 입력하여 설치
    ```python
    import requests

    reponse = requests.get(url).json()
    ```
  - `requests.get`을 통해 해당 url에서 데이터를 받음
  - `json()`은 받은 데이터를 딕셔너리 형태로 만들어줌

  #### 패키지 사용목적
  - 모듈들의 이름공간을 구분하여 충돌을 방지
  - 모듈들을 효율적으로 관리하고 재사용할 수 있도록 돕는 역할

## 제어문
코드의 실행 흐름을 제어하기 위해 사용되는 구문
- **<span style = "color:red">조건</span>** 에 따라 코드 블록을 실행하거나 **<span style = "color:red">반복</span>** 적으로 코드를 실행
  - 위에서 아래로 진행되는 코드의 흐름을 바꿀 수 있는 도구

## 조건문
주어진 조건식을 평가하여 해당 조건이 참인 경우에만 코드 블록을 실행하거나 건너뜀
```python
if '표현식':
    코드 블록
elif '표현식':
    코드 블록
else:
    코드 블록
```
- `if`에서 실행이 된다면 밑은 실행되지 않음
- `elif` 조건을 만족하면 `if`의 코드블록은 실행되지 않음
- `elif`와 `else`는 단독 사용 불가

  #### 복수 조건문
  - 조건식을 동시에 검사하는 것이 아닌 맨 위 `if` 부분부터 **<span style = "color:red">순차적</span>** 으로 비교한다.

  #### 중첩 조건문
  - 한 `if`의 코드블록에 새로운 `if`문을 작성할 수 있다.

## 반복문
주어진 코드 블록을 여러번 반복해서 실행하는 구문

### for
- 임의의 시퀀스의 항목들을 그 시퀀스에 들어있는 순서대로 반복
- 구조
  ```python
  for 변수 in 반복 가능한 객체:
    코드블록
  ```

  #### 반복 가능한 객체
  - 반복문에서 순회할 수 있는 객체<br>
  `시퀀스 객체` `dict` `set` 

### while
- 주어진 조건이 참인 동안 반복적으로 수행
- 거짓이 될 때까지 반복적으로 수행
- 구조
  ```python
  while 조건식:
    코드 블록
  ```
  #### 주의사항
  - 반드시 **종료 조건**이 필요

### 적절한 반복문 선택
- for
  - 반복 횟수가 명확하게 정해져 있는 경우에 유용
- while
  - 반복 횟수가 불명확하거나 조건에 따라 반복을 종료해야 할 경우 유용

### 반복 제어
반복문은 본문 내 모든 코드를 실행하지만 상황에 따라 일부만 실행하고 싶을 때 사용

<div align = "center">

|반복 제어 키워드|내용|
|:-------------:|:-:|
|`break`|반복을 즉시 중지|
|`continue`|다음 반복으로 건너뜀|
|`pass`|아무런 동작도 수행하지 않고 넘어감|

</div>

  #### break 예시
  ```python
  for i in range(10):
    if i == 5:
        break
    print(i, end = ' ')

  # 출력 : 0 1 2 3 4
  ```
  #### continue 예시
  ```python
  for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end = ' ')

  # 출력 : 1 3 5 7 9
  ```

  #### pass 예시
  - 조건문에서 아무런 동작을 수행하지 않아야 할 때
  ```python
  if condition:
    pass
  else:
    코드 블록
  ```
  - 코드 작성 중 미완성 부분
  ```python
  def my_func():
    pass
  ```
### List Comprehension
간결하고 효율적인 리스트 생성 방법<br>
`[expression for 변수 in iterable if 조건식]`
- `if 조건식`은 생략 가능하다.

#### 활용 예시
  - 2차원 배열 생성
    - 0 배열
     ```python
     [[0 for _ in range(3)] for _ in range(3)]
     # 출력 :
     # [[0, 0, 0],
     # [0, 0, 0],
     # [0, 0, 0]]
     ```
  - 순차 배열
     ```python
     [i for i in range(4)]
     # 출력 :
     # [0, 1, 2, 3, 4]
     ```
  
  #### 주의사항
  - comprehension은 많은 정보를 한 줄에 적는다.
  - 의도를 파악하기가 어렵기에 남용하지 않아야 한다.
  - **comprehension의 목적은 리스트 생성**

  #### 리스트 생성 방법별 성능 비교
  - 일반적으론 list comprehension이 가장 빠르고, map, loop 순이다.
  - 그러나 복잡한 로직의 경우 loop이 직관적인 코드를 작성할 수 있다.
  - 버전 업데이트에 따라 성능 차이는 거의 미미해졌으므로, **코드의 가독성**과 **유지보수성**을 고려하여 선택하면 된다.

## 참고
### 모듈 살펴보기
내장함수 `help()`를 사용해 모듈에 들어있는 내용을 확인 가능하다.

### enumerate
iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수<br>
`enumerate(iterable, start = 0)`
- `iterable` : 리스트 등의 컬렉션
- `start` : 시작으로 설정하고 싶은 번호

  #### 예시
  ```python
  fruits = ['apple', 'banana', 'cherry']

  for idx, x in enumerate(fruits, 5):
    print(idx, x)

  # 출력 :
  # 5 apple
  # 6 banana
  # 7 cherry
  ```

## 자체 Q&A
- `List Comprehension`에는 for문과 if문을 이용해 한줄로 특정 배열을 생성할 수 있다. 특정 조건을 만족하는 값들로 배열을 만드는 것이기에 쓰일 일은 없겠지만, `List Comprehension`에도 `If ~ else문`을 **사용**할 수 있을까?
  > 사용할 수는 있지만 같은 문법은 아니다!!<br>
  > 기존의 `[출력값 for i in <iterate> if 조건]`에서 `if`문은 **필터**이다.<br>
  > **Comprehension if** 라고 한다.
  > 구문이 참일 경우 담고, 거짓일 경우 지나치는 방식이다.<br>
  > 이미 조건이 True일때와 False일때의 작동 방식이 정해져 있는 상황에서 추가적인 else문은 불필요하다.<br>
  >
  > `if else`를 사용하고자 할 때는 아래 방식으로 사용할 수 있다.
  > `[출력값 if 조건 else 또 다른 출력 방식 for i in <iterate>]` <br>
  > 이 경우 반복문 앞에 붙게 된다.<br>
  > 앞선 comprehension if와는 다르게 출력값에 영향을 주는 방식이다. <br>
  > if문의 조건에 부합하면 기존 출력값 형태로 출력하되, 그렇지 않다면 else문의 방식으로 출력한다는 구문이다.
  > 일종의 **지시자**로 볼 수 있다.

## 공부 내용 돌아보기
지금까지 파이썬을 써오며 가장 많이 마주했던 것들을 배웠다. 조건문과 반복문은 단순 코드 테스트 외에도 프로젝트에서도 많이 사용한 것들이다. 패키지는, 그 보다도 라이브러리인 numpy와 pandas, tensorflow 등을 import해서 수차례 사용해왔다. 그러기에 이해가 쉬웠다.<br> 다만, `enumerate`는 몇 번 마주했지만 어색한 함수다. 리스트에서 인덱스와 값을 함께 반환한다. 처음에는 사용처가 어디일까 생각했다. 생각난건, 순차적으로 번호를 매겨 분류하는 상황에서 유용할 것이라 생각되었다. 머신러닝을 배우며 알게된 'one-hot encoding`과 형태가 약간 유사하다는 느낌도 들었다.