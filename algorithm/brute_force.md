# 완전 검색
## 반복과 재귀



## 순열



## 완전탐색기법




## 부분 집합
부분 집합을 구현하는 방법은 크게 2가지가 있다.
1. 완전 탐색
2. Binary Counting

### 완전 탐색 방식
- 부분 집합에 어떤 원소를 포함할지 안 할지 결정한다.
  - '포함한다'와 '포함하지 않는다'의 두 가지 경우가 있으므로 가지는 2개이다.
  - 원소 3개에 대한 부분 집합을 구하기 위해 만든 그래프의 높이는 원소의 개수와 동일한 3이다.

```python
arr = [True, False]  # 갈래 (branch)
path = []  # 갈래를 담는 리스트
name = ['Amy', 'Ian', 'Mark']  # 이름 리스트

def print_name():
  for i in range(3):
    if path[i]:  # 만약 갈래가 True면
      print(name[i], end=' ')  # 이름을 출력한다.
  print()

def run(lev):  # lev는 학생의 번호로 생각
  if lev == 3: # 3번 판단했으면
    print_name()  # 출력 함수로 넘어간다
    return

  for i in range(2):  # 한 사람의 TF 판단
    path.append(arr[i])  # path에 현 사람의 갈래 담음
    run(lev + 1) # 다음 사람으로
    path.pop() # 복구(반환)

run(0)
```

### Binary Counting 방식
원소 수에 해당하는 N개의 비트열을 이용한다.
- 원소의 선택 여부를 0과 1로 나타낸다.
- 비트를 이용해 돌면서 그 여부를 파악하고 부분 집합에 넣는다.
```python
arr = ['A', 'B', 'C']
n = len(arr)

def get_sub(tar):
  for i in range(n):
    if tar & 0x1:
      print(arr[i], end=' ')
    tar >>= 1

for tar in range(0, 1 << n):
  print('{', end='')
  get_sub(tar)
  print('}')
```

## 조합




## 그리디 알고리즘
