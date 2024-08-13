# Stack #2
## 계산기
### 계산식 표기법
  #### 중위 표기법
  - 연산자를 피연산자의 가운데 표기하는 방법
  - `A + B`
  
  #### 후위 표기법
  - 연산자를 피연산자 뒤에 표기하는 방법
  - `AB+`

### 후위 표기법으로 변환
  #### 과정
  1. 입력 받은 중위 표기식에서 토큰을 읽는다.
  2. 토큰이 피연산자이면 토큰을 출력한다.
  3. 토큰이 연산자일 때, 이 토큰이 스택 top에 저장되어 있는 연산자보다 우선순위가 높으면 스택에 push하고,<br> 그렇지 않으면 스택 top 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 pop을 한 후 토큰을 push한다.
    
      *우선순위*

      |토큰|스택 밖|스택 안|
      |:--:|:----:|:----:|
      |`)`|-|-|
      |`*`, `/`|2|2|
      |`+`, `-`|1|1|
      |`(`|0|3|

  4. 토큰이 ')'이면 스택 top이 '('이 될 때까지 pop을 수행하고, pop된 연산자는 출력한다.
  5. 중위 표기식을 다 읽었다면 중지하고, 더 읽을 것이 있다면 1번부터 다시 반복한다.
  6. 스택에 남아있는 연산자를 모두 pop하여 출력한다.

### 후위 표기식을 이용한 계산
  #### 과정
  1. 피연산자를 만나면 스택에 push한다.
  2. 연산자를 만나면 필요한 만큼의 피연산자를 pop하여 연산한다.
  3. 연산 결과를 스택에 push한다.
  4. 수식이 끝나면, 마지막으로 스택을 pop하여 출력한다.

## 백트래킹
해를 찾는 도중에 막히면 되돌아가서 다른 해를 찾아 가는 기법

### 백트래킹과 DFS의 차이
- 어떤 노드에서 출발하는 경로가 해가 아닐 것 같으면 따라가지 않음으로써 시도 횟수를 줄인다.
- 결국 불필요한 경로를 추적하는가 아닌가의 차이

### 백트래킹 절차
1. 트리의 DFS를 실시한다.
2. 각 노드가 유망한지 점검한다.
3. 만일 그 노드가 유망하지 않으면, 부모 노드로 돌아가서 검색을 계속한다.

### 백트래킹 단점
- 조건에 따라 함수 실행 횟수가 크게 증가할 수 있다.

### 부분집합 탐색하기
기존 for문을 이용하여 부분집합을 찾을 경우, 집합의 원소의 개수에 따라 엄청나게 많은 다중 for문이 생성된다.<br> 원소 개수가 m 개일 경우 시간복잡도가 O(n^m)이 될 것으로 엄청 비효율적이다.
<br>따라서 백트래킹을 사용하여 탐색해본다.

```python
def backtrack(a, k, n):
  c = [0] * maxcandidates

  if k == n:
    process_solution(a, k)
  else:
    ncandidates = construct_candidates(a, k, n, f)
    for i in range(ncandidates):
      a[k] = c[i]
      backtrack(a, k + 1, n)

def construct_candidates(a, k, n, c):
  c[0] = False
  c[1] = True
  return 2

def process_solution(a, k):
  for i in range(k):
    if a[i]:
      print(num[i], end = ' ')
  print()

maxcandidates = 2
nmax = 4
a = [0] * nmax
num = [1, 2, 3, 4]
backtrack(a, 0, 3)  
```
형식을 갖춘 백트래킹
1. 후보를 추천하고
2. 그 후보를 하나씩 불러온다.

### 순열


### 가지치기
유망하지 않는 노드가 포함된 경로는 더 이상 고려하지 않는 방법

- a[i]의 포함 여부 결정(bit[i]가 1 또는 0)

## 자체 Q&A
- 순열에 메모이제이션을 사용해보자
- nPr 형태의 순열 코드
- 몰빵 계산이 시간이 오래걸린다.
```python
def fmin_sum(i, k):
    global min_sum
    if i == k:  # i가 n과 동일하면
        s = 0  # case 별 합
        for p in range(k):
            s += lst[p][slt[p]]  # 각 행의 선택된 값의 합
        if min_sum > s:
            min_sum = s  # min_sum보다 s가 작다면 min_sum에 s값 재할당
        return
    else:
        for j in range(i, k):
            slt[i], slt[j] = slt[j], slt[i]  # slt배열의 i와 j 위치를 바꾸고
            fmin_sum(i + 1, k)  # 바꾼 slt를 이용하여 함수 실행
            slt[i], slt[j] = slt[j], slt[i]  # 바꿨던 slt를 원상복귀
        return


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(n)]

    slt = [p for p in range(n)]  # 각 행마다 선택되는 열 번호 리스트
    min_sum = 90  # 합의 최소값이 할당될 변수 선언
    fmin_sum(0, n)
    print(f'#{tc} {min_sum}')
```
```python
def f(i, k, s):
    global min_sum
    if i == k:  # i가 n과 동일하면
        if min_sum > s:
            min_sum = s  # min_sum보다 s가 작다면 min_sum에 s값 재할당
        return
    elif min_sum <= s:
        return
    else:
        for j in range(i, k):
            slt[i], slt[j] = slt[j], slt[i]  # slt배열의 i와 j 위치를 바꾸고
            fmin_sum(i + 1, k, s + lst[i][slt[i]])  # 바꾼 slt를 이용하여 함수 실행
            slt[i], slt[j] = slt[j], slt[i]  # 바꿨던 slt를 원상복귀
        return
```

## ㄱㅂ ㄴㅇ ㄷㅇㅂㄱ