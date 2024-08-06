# Stack #1
## 스택
물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조
- 스택은 선형 구조이다.
  > 자료 간의 관계가 1대 1이다.
- 스택은 자료를 위로 쌓아올리고, 위에서부터 꺼내 쓰는 방식으로, **<span style = "color:red">후입선출</span>** *(LIFO, Last-In-Fisrt-Out)* 이라고 부른다.
- 마지막으로 삽입된 원소의 위치를 **top** 이라고 부른다.

### 스택의 구현
  #### 자료구조
  - 자료를 선형으로 저장할 저장소
  - 배열 사용 가능
  - 저장소 자체를 스택이라 부르기도 함
  #### 연산
  - 삽입 : 저장소에 자료 저장 *(push)*
  - 삭제 : 저장소에서 자료 추출 *(pop)*
  - 공백 확인 : *isEmpty*
  - top 원소 반환 : *peek*

### 스택의 과정
1. stack 배열을 빈 배열로 생성한다.
  ![stack_step1](./image/bin_stack.PNG)
2. 값을 push 한다.
  ![stack_step2_1](./image/push1.PNG)
  ![stack_step2_2](./image/push2.PNG)
3. top에서부터 pop을 진행한다.
  ![stack_step3](./image/pop.PNG)

### 스택의 구현
  #### push
  ```python
  def push(item, size):
    global top
    top += 1 # top 인덱스를 1 증가시킨다.
    if top == size:
      # 증가한 top이 stack 배열을 초과한다면
      print('Overflow..!')
    else:
      # 초과하지 않는다면 item을 해당 칸에 할당한다.
      stack[top] = item

  size = 5
  stack = [0] * size
  top = -1
  # stack 배열과 top의 초기값 설정

  push(1, size)
  push(2, size)

  # stack 출력 : [1, 2, 0, 0, 0]
  ```

  #### pop
  ```python
  def stack_pop():
    global top
    if top == -1:
      # stack 배열의 길이가 0이면
      print('Underflow..!')
      # 여기서는 위의 기능을 top이 -1일 때로 입력하였다.
      return 0 # else문의 형식과 맞춰주기 위함
    else:
      # 길이가 0이 아니라면
      top -= 1 # top을 먼저 감하고
      return stack[top + 1] # 감하기전 top의 stack 값을 반환

      # 다만 이 경우 stack 배열 길이를 감소시킬 수는 없다. 
      # (완전한 pop의 기능은 아니다.)
  ```

## 함수에서의 스택 기본
### Function call
프로그램에서 함수 호출과 복귀에 따른 수행 순서를 관리
![function call](./image/function_call.PNG)
- 가장 **마지막에 호출**된 함수가 **가장 먼저 실행**을 완료하고 복귀하는 후입선출 구조
- 동일한 구조인 <span style = "color:red">스택</span>을 이용하여 수행순서를 관리할 수 있다!!!
  > 정의를 봤을 때, 재귀호출과 동일해 보인다.<br>
  > 처음 호출된 함수부터 마지막으로 호출된 함수 *<span style = "color : #808080">(결과가 a + func()이 아닌 경우)</span>* 까지 돌고,<br>
  > 그 반환값이 마지막 함수부터 반환되기 때문이다.<br>
  
  > 그러나 Function call이 더 큰 개념이었다.<br>
  > 재귀함수는 유사한 기능의 함수를 반복하는 것이지만,<br>
  > Function call은 그에 상관 없이 어느 한 함수 안에 다른 함수가 있는 모든 경우를 칭하기 때문이다.

### Memoization


## DP


## DFS


## 자체 Q&A


##