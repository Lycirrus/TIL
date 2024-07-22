# Data Structure #1
데이터 구조
- 여러 데이터를 효과적으로 사용 관리하기 위한 구조
  
자료 구조
- 각 데이터의 효율적인 저장, 관리를 위한 구조를 나눠 놓은 것

데이터 구조의 활용
- 문자열, 리스트, 딕셔너리 등 각 데이터 구조의 <span style = "color:RED">메서드</span>를 호출하여 다양한 기능을 사용

### 메서드
어떠한 객체에 속해있는 함수

  #### 메서드 특징
  - 메서드는 클래스(class) 내부에 정의되는 **함수**
  - 클래스는 파이썬에서 **타입을 표현하는 방법**
  - 데이터 타입별로 다양한 기능을 가진 메서드 존재
    #### Chaining
    - 메서드는 이어서 사용 가능
    - 단, 앞에서 반환된 결과가 있어야 하며 데이터 타입도 맞아야 함

## 시퀀스 데이터 구조
### 문자열
#### 문자열 조회/탐색 및 검증

<div align = "center">

|메서드|설명|
|:----:|:-:|
|`s.find(x)`|x의 첫 번째 위치를 반환<br> 없으면 **-1을** 반환|
|`s.index(x)`|x의 첫 번째 위치를 반환<br> 없으면 **오류** 발생|
|`s.isupper()`|대문자 여부에 따른 Boolean|
|`s.islower()`|소문자 여부에 따른 Boolean|
|`s.isalpha()`|알파벳 문자 여부에 따른 Boolean<br> <span style = "color: #808080">모든 유니코드 상 문자 포함(ex. 한국어)</span>|
</div>

  #### python의 is
  - `is`는 반환값을 True 또는 False이다.
  - 따라서 `is`가 붙은 메서드도 Boolean을 반환한다.
  - 따라서 참거짓을 따지는 개인 함수도 이름에 `is`를 붙이는 것이 좋다.

#### 문자열 조작(새 문자열 반환)

<div align = "center">

|메서드|설명|
|:----:|:-:|
|`s.replace(old, new[,count])`|<span style = "color:RED">바꿀 대상 글자를 새로운 글자로 바꿔서 반환</span>|
|`s.strip([chars])`|<span style = "color:RED">공백이나 특정 문자를 제거</span>|
|`s.split(sep = None, maxsplit = -1)`|<span style = "color:RED">공백이나 특정 문자를 기준으로 분리</span>|
|`separator'.join(iterable)`|<span style = "color:RED">구분자로 iterable의 문자열을 연결한 문자열을 반환</span>|
|`s.capitalize()`|가장 첫 번째 글자를 대문자로 변경<br>그 뒤는 모두 소문자로 변경|
|`s.title()`|문자열 내 띄어쓰기 기준으로 각 단어의 첫글자는 대문자, 나머지는 소문자로 변환|
|`s.upper()`|모두 대분자로 변경|
|`s.lower()`|모두 소문자로 변경|
|`s.swapcase()`|대소문자 서로 변경|
</div>

  - 문자열은 불변 자료형이므로 새로운 문자열을 반환한다.

  #### replace
  바꿀 대상 글자를 새로운 글자로 바꿔서 변환
  - count는 old에 입력되는 문자열이 전체 문자열 내 여러개 있을 경우 몇 개를 new 문자열로 바꿀 것인지 결정

  #### strip
  문자열의 시작과 끝에 있는 공백 혹은 지정한 문자를 제거
  - 인자가 없다면 기본적으로 공백 제거

  #### split
  지정한 문자를 구분자로 문자열을 분리하여 리스트로 반환
  - `sep` 부분을 특별히 지정하지 않을 경우 공백을 기준으로 분리

  #### join
  iterable 문자열을 연결한 문자열을 반환

### 리스트
#### 리스트 값 추가 및 삭제

<div align = "center">

|메서드|설명|
|:----:|:-:|
|`L.append(x)`|<span style = "color:RED">리스트 마지막에 항목 x를 추가</span>|
|`L.extend(m)`|<span style = "color:RED">iterable m의 모든 항목들을 리스트 끝에 추가</span>|
|`L.insert(i, x)`|리스트 인덱스 i에 항목 x를 삽입|
|`L.remove(x)`|리스트 내 항목 x 중 가장 앞 순서의 것을 제거<br>항목이 존재하지 않을 경우 ValueError|
|`L.pop()`|<span style = "color:RED">리스트 마지막 항목을 반환 후 제거</span>|
|`L.pop(i)`|<span style = "color:RED">리스트 인덱스 i에 있는 항목을 반환 후 제거</span>|
|`L.clear()`|리스트의 모든 항목 삭제|
</div>

  #### append
  리스트 마지막에 항목 x 추가
  - 반환이 없는 함수이므로 `.append()`를 프린트할 경우 **None**이 출력됨
  - 인자를 한 개만 받을 수 있음

  #### extend
  리스트에 다른 반복 가능한 객체의 모든 항목을 추가
  - extend의 인자는 iterable해야 한다.
  - int나 str형은 사용 불가
  - 인자를 한 개만 받을 수 있음

  #### pop
  리스트에서 지정한 인덱스의 항목을 **제거**하고 **반환**

#### 리스트 탐색 및 정렬

<div align = "center">

|메서드|설명|
|:----:|:-:|
|`L.index(x)`|리스트의 항목 x 중 가장 빠른 순서의 인덱스를 반환|
|`L.count(x)`|리스트에서 항목 x의 개수를 반환|
|`L.reverse()`|<span style = "color:RED">리스트 순서를 역순으로 변경</span>|
|`L.sort()`|<span style = "color:RED">리스트 정렬</span><br> <span style = "color: #808080">(매개변수 이용가능)</span>|
</div>

  #### reverse
  리스트의 순서를 역순으로 변경
  - 정렬되는 것은 아님
  - 반환값이 없는 함수

  #### sort
  원본 리스트를 오름차순으로 정렬
  - `reverse`라는 매개변수를 사용하여 내림차순으로 변경 가능
     ```python
     my_lst.sort()
     # 오름차순 정렬

     my_lst.sort(reverse = True)
     # 내림차순 정렬
     ```

### 숫자 판별 메서드

<div align = "center">

|메서드|설명|
|:----:|:-:|
|`s.isdecimal()`|문자열이 모두 숫자 문자로만 이루어져 있어야 **True**|
|`s.isdigit()`|지수 및 유니코드 숫자도 인식|
|`s.isnumeric()`|분수, 루트 기호,다른 언어로 표기된 숫자 등 더 많은 유니코드 문자들을 인식|
</div>

- `isdecimal()`, `isdigit()`, `isnumeric()` 순으로 포함 범위가 넓어진다.
- 소수나 음수는 `.`과 `-`가 숫자 기호로 판별되지 않으므로 항상 **False**가 나온다.

## 자체 Q&A
- `.isalpha()`를 숫자와 문자가 혼용된 문자열에 적용했을 때 어떠한 결과가 나타나는가?
  > 혼용되어 있을 경우 모두 **False**가 나왔다.
  > ```python
  > # 숫자로 시작하는 문자열
  > test_word = '2e4Weg'
  > # 문자로 시작하는 문자열
  > test_word_2 = 'eahas5e'
  >
  > print(test_word.isalpha())
  > # 출력 : False
  > print(test_word_2.isalpha())
  > # 출력 : False
  > ```
  > 도중 혼용 문자열을 판별할 수 있는 `.isalnum()`을 발견했다.
  > ```python
  > print(test_word.isalnum())
  > # 출력 : True
  > ```
  > 이 메서드는 혼용 문자열 뿐만 아니라 숫자 단독과 문자 단독 문자열도 **True**를 반환하였다.
  > ```python
  > only_str = 'asgaefa'
  > only_num = '51515'
  >
  > print(only_str.isalnum())
  > # 출력 : True
  > print(only_num.isalnum())
  > # 출력 : True
  > ```
- `.split()` 메서드의 인자 **maxsplit**은 무슨 역할을 하는가?
  > maxsplit은 반복 횟수이다.<br>
  > 기본값은 '-1' 로 되어 있는데, 할 수 있는한 무제한 반복한다는 의미이다.
  > maxsplit에 값을 입력하여 실행해 보았다.
  > ```python
  > test = '1 3 5 7 9'
  > 
  > print(test.split())
  > # 출력 : ['1', '3', '5', '7', '9']
  > print(test.split(maxsplit = 3))
  > # 출력 : ['1', '3', '5', '7 9']
  > ```
  > 보다시피 밑에는 앞에서부터 세번째 공백인 5와 7 사이까지만 분리되고 7과 9는 하나의 요소로 묶여 나왔다.
- 리스트에 `.extend()`를 사용한다. 인자에 튜플을 넣을 경우 어떻게 출력되는가?
  > 정답은 튜플의 요소만 리스트에 추가된다.
  > ```python
  > test = [1, 2]
  > in_test = (1, 3)
  > test.extend(in_test)
  >
  > print(test)
  > # 출력 : [1, 2, 1, 3]
  > ```
  > 그렇다면 key와 value로 구성된 딕셔너리를 넣으면 어떻게 될까?<br>
  > 결과는 key값만 추가되었다.
  > ```python
  > test = [1, 2]
  > in_test = {'one': 1, 'two': 2}
  > test.extend(in_test)
  >
  > print(test)
  > # 출력 : [1, 2, 'one', 'two']
  > ```
  > 그럼 value를 extend하고 싶으면 어떻게 할까?<br>
  > 딕셔너리의 value를 확인하는 `.values()`를 사용하니 할 수 있었다.<br>
  > 추가적으로 `.items()`를 사용하면 key와 value 모두를 튜플형태로 extend할 수 있었다.
  > ```python
  > test = [1, 2]
  > in_test = {'one': 1, 'two': 2}
  > # Case 1
  > test.extend(in_test.values())
  >
  > print(test)
  > # 출력 : [1, 2, 1, 2]
  >
  > # Case 2
  > test.extend(in_test.items())
  >
  > print(test)
  > # 출력 : [1, 2, ('one', 1), ('two', 2)]
  > ```