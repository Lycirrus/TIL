# queue #1
## 큐
스택과 같이 삽입과 삭제의 위치가 제한적인 자료구조
- 뒤에서 삽입하고, 앞에서 삭제한다.
- 큐는 삽입한 순서대로 원소가 저장되어, 가장 먼저 삽입된 원소가 가장 먼저 삭제되는 방식으로 **<span style = "color:red">선입선출</span>** *(FIFO, First-In-Fisrt-Out)* 이라고 부른다.

### 큐의 기본 연산
- 삽입 : enQueue
- 삭제 : deQueue

### 큐의 주요 연산

|연산|기능|
|:--:|:-:|
|`enQueue(item)`|큐의 뒤쪽에 원소를 삽입하는 연산|
|`deQueue()`|큐의 앞쪽에서 원소를 삭제하고 반환하는 연산|
|`createQueue()`|공백 상태의 큐를 생성하는 연산|
|`isEmpty()`|큐가 공백상태인지를 확인하는 연산|
|`isFull()`|큐가 포화상태인지를 확인하는 연산|
|`Qpeek()`|큐의 앞쪽에서 원소를 삭제 없이 반환하는 연산|

## 선형큐
1차원 배열을 이용한 큐
  #### 삽입 : enQueue(item)
  마지막 원소 뒤에 새로운 원소를 삽입
  - rear 값을 하나 증가시켜 새로운 원소를 삽입할 자리를 마련한다.
  - Q[rear]에 item을 저장한다.
  ```python
  def enQueue(item):
    global rear
    if isFull() : print("Queue_Full")
    else:
      rear <- rear + 1
      Q[rear] <- item
  ```

  #### 삭제 : deQueue()
  가장 앞의 원소를 삭제
  - front 값을 하나 증가시켜 큐에 남아있는 첫 번째 원소로 이동한다.
  - 새로운 첫 번째 원소를 리턴하여 삭제와 동일하게 기능한다.
  ```python
  def deQueue():
    if isEmpty() : print("Queue_Empty")
    else:
      front <- front + 1
      return Q[front]
  ```

  #### 공백 및 포화 검사
  - 공백상태 : front == rear
  - 포화상태 : rear == n - 1
  ```python
  def isEmpty():
    return front == rear
  
  def isFull():
    return rear == len(Q) - 1
  ```

  #### 검색 : Qpeek()
  -가장 앞에 있는 원소를 검색하여 반환한다.
  ```python
  def Qpeek():
    if isEmpty() : print("Queue_Empty")
    else:
      return Q[front + 1]
  ```

## 원형큐
> 선형큐는 삽입과 삭제를 반복하면, 배열 앞부분에 활용할 공간이 생겨도 rear가 n - 1이 되어 포화상태로 인식하게 된다.
- 해결 방법
1. 매 연산마다 저장된 원소들을 배열의 앞 부분으로 모두 이동시킨다.
    > 원소 이동에 많은 시간이 소요되어 큐의 효율성이 급격히 떨어진다.
2. 1차원 배열을 사용하지만 처음과 끝이 연결되는 원형 큐를 이룬다고 가정하고 사용한다.
    > 인덱스의 순환을 위해 나머지를 활용한다.

- 공백 상태와 포화 상태 구분을 위해 front 자리를 사용하지 않는 방식으로 한다.
  > 그래서 원형 큐는 front가 비어있는 상태가 Full이 된다.
- 위치를 나타내는 rear과 front를 큐 길이로 나눈 나머지를 인덱스로 한다.

  #### 원형큐 공백과 포화
  - 공백상태 : front == rear
  - 포화상태 : front == rear + 1
  ```python
  def isEmpty():
    return front == rear
  
  def isFull():
    return (rear + 1) % len(Q) == front
  ```

  #### 원형큐의 삽입
  - 선형큐와 비슷하지만 (rear + 1)을 Queue의 길이로 나눈 값을 인덱스로 한다.
  ```python
  def enQueue(item):
    global rear
    if isFull():
      print("Queue_Full")
    else:
      rear = (rear + 1) % len(Q)
      Q[rear] = item
  ```

  #### 원형큐의 삭제
  - 삽입과 동일하게 선형큐와 유사하지만, Queue의 길이로 나눈 나머지 값을 인덱스로 한다.
  ```python
  def deQueue():
    global front
    if isEmpty():
      print("Queue_Empty")
    else:
      front = (front + 1) % len(Q)
      return Q[front]

## 연결큐
- 큐의 원소 : 단순 연결 리스트의 노드
- 큐의 원소 순서 : 노드의 연결 순서
- front : 첫번째 노드를 가리키는 링크
- rear : 마지막 노드를 가리키는 링크

### 상태 표현
- 초기상태 : front == rear == null
- 공백상태 : front == rear == null

### deque
연결큐의 형태를 하고 있다.
- 사이즈가 큰 Queue를 만들 때는 deque을 쓰면 좋다.
- 그러나 크기가 정해졌을 경우, front와 rear를 쓰는 것이 가장 빠르다.
- 다만 크기의 제한이 없는 경우는 deque이 제약이 없기에 좋다.

## 우선순위 큐 개념
- 우선순위를 가진 항목들을 저장하는 큐
- 기존 큐의 FIFO가 아니라 우선순위가 높은 순서대로 나간다

### 구현
- 원소를 삽입하는 과정에서 우선순위를 비교하여 적절한 위치에 삽입한다.
  > 무조건 rear 삽입이 아니다.

### 문제점
- 배열을 사용하므로, 삽입이나 삭제 연산이 일어날 때마다 원소의 재배치가 발생한다.
  > 소요되는 시간이나 메모리가 크므로 낭비가 발생한다.

## 버퍼
데이터를 한 곳에서 다른 곳으로 전송하는 동안 일시적으로 그 데이터를 보관하는 메모리 영역
> **버퍼링** :<br>
> 버퍼를 활용하는 방식 또는 버퍼를 채우는 동작을 의미한다. 

### 버퍼 자료 구조
- 순서대로 입력하고 출력되고 전달되어야 하므로 FIFO 방식의 Queue가 사용된다.

## BFS
탐색 시작점의 인접한 정점들 모두를 먼저 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식

  #### 예시
  ```python
  def BFS(G, v): # 그래프 G, 탐색 시작점 v
    visited = [0] * (n + 1) # 방문 판단
    queue = [] # 큐 생성
    queue.append(v) # 시작점 v를 큐에 삽입
    # 여기까지가 준비 단계
    while queue:
      t = queue.pop(0) # front 반환(방문할 노드)
      if not visited[t]: # 방문 안한 곳이면
        visited[t] = True # 방문 표시
        visit(t) # 정점 t에서 할 일
        for i in G[t]: # t와 연결된 모든 정점에 대해
          if not visited[i]: # 방문하지 않았으면
            queue.append(i) # 큐에 넣기
            # for문은 대기열을 생성
  ```

  아래와 같이 하면 출발에서부터 거리가 어떻게 되는지 알 수 있다.
  ```python
  def bfs(G, s, v): # 여기서는 s가 시작점, v는 정점의 개수다
    visited = [0] * (v + 1)
    queue = []
    queue.append(s)
    visited[s] = 1
    while queue:
      t = queue.pop(0)
      visit()
      for w in G[t]:
        if not visited[w]:
          queue.append(w)
          visited[w] = visited[t] + 1
          # 마지막 구문에서 거리는 이전 노드의 +1이 된다.
  ```

## 자체 Q&A


## ㄱㅂ ㄴㅇ ㄷㅇㅂㄱ