# List #2
## 2차원 배열
  #### Input 시 2차원 배열 생성
  ```python
  n = int(input)
  lst = [list(map(int, input().split())) for _ in range(n)]
  ```
  으로 한 줄로 들어오는 값을 2차원 배열 형태로 만들 수 있다.

  #### 지그재그 순회
  ```python
  for i in range(n):
    for j in range(m):
      lst[i][j + (m - 1 - 2 * j) * (i % 2)]

  # n = 3, m = 4일 경우
  for i in range(3):
    for j in range(4):
      lst[i][j + (3 - 2 * j) * (i % 2)]
  
  # 0행에서는 'i % 2 = 0'이 되므로 'lst[i][j]와 동일하다.
  # 1행에서는 'i % 2 = 1'이 되어 'lst[i][3 - j]로 작동한다.
  # 결국 홀수 행에서 열번호는 역순으로 돌게 되니, 지그재그로 순회하게 된다!
  ```

  #### 전치 행렬
  ```python
  for i in range(n):
    for j i range(n):
      if i < j:
        arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
  ```
  으로 전치행렬을 만들 수 있다.<br>
  `a, b = b, a`라는 파이썬만의 a와 b의 값을 교환하는 특별한 문법덕분에 간단하게 만들어졌다.<br>
  `i < j`라는 조건문이 없으면, 하나의 교환쌍에 대해 교환이 2번 일어나기에 원래대로 돌아가게 된다.
  `zip`을 이용하여 간단하게 만들 수 있다.
  ```python
  narr = list(zip(*arr))
  ```
  다만 내부는 튜플형이 되기에, 내부 리스트가 필요하다면 위의 방식을 고려할 수도 있을 것이다.

  > N * N 행렬에서 오른쪽 위를 향하는 대각의 요소를 구하는 방법<br>
  > 조건을 `i < j` 대신 `2 - i == j`로 하면 된다.<br>
  > 인덱스 i와 j의 합이 (N - 1)이 되는 요소만 뽑아내는 것이다.

## 부분집합 생성
`main_set = [1, 2, 3]`의 set형은 아니지만 집합이 있다고 하자.<br>
우선 해당 집합의 부분집합 개수는 '2^3'인 `8개`이다.

### 비트 검사
부분집합을 1과 0으로 표현하니 2진수를 보았다.


## 검색
저장되어 있는 자료 중에서 원하는 항목을 찾는 작업
- 목적하는 탐색키를 가진 항목을 찾는 것
  > 탐색기는 자료를 구별하여 인식할 수 있는 키

### 순차 검색
일렬로 되어 있는 자료를 순서대로 검색하는 방법
- 순서가 있는 리스트나 튜플에서 원하는 항목을 찾을 때 유용하다.
- 구현은 쉽지만 검색 수가 많아질수록 수행시간이 급격히 증가하여 효율이 떨어진다.
  > 10억개쯤 되면 문제가 발생할 수 있다고 한다.

  #### 자료가 정렬되어 있지 않은 경우
  - 과정<br>
    1. 첫번째 원소부터 검색 대상과 키 값이 같은 원소를 비교하여 찾는다.
    2. 동일한 원소를 찾으면 그 원소의 인덱스를 반환한다.
    3. 자료구조의 마지막에 이를 때까지 찾지 못하면 검색이 실패한다.

  #### 정렬되지 않은 자료의 순차 탐색 시간복잡도
  > 첫번째 원소를 찾을 땐 1번, 두번째 원소는 2번, 마지막 원소는 n번 비교한다.<br>
  > => **n(n+1)/2** <br>
  > 평균은 전체 개수로 나누는 것이다.<br>
  > => **1/n** <br>
  > 두 식을 곱하면,<br>
  > **(n+1)/2** <br>
  > 따라서 시간복잡도는 **<span style = "color: red">O(n)</span>** 이 된다.

  #### 자료가 정렬되어 있는 경우
  - 과정<br>
    1. 자료를 순차적으로 검색하며 키 값을 비교한다.
    2. 동일한 원소를 찾으면 그 원소의 인덱스를 반환한다.
    3. 비교하였을 때 원소 키 값이 검색 키 값보다 크면, 찾는 원소가 없는 것이므로 검색을 종료한다.

  #### 정렬되어 있는 자료의 순차 탐색 시간복잡도
  > 첫번째 원소를 처음에, 마지막 원소를 마지막에 찾는 것은 정렬되지 않은 자료와 동일하다.<br>
  > 다만 자료 내에 없는 항목을 찾을 경우 정렬되지 않은 자료는 무조건 n번을 돌지만,<br>
  > 정렬되어 있을 경우 중간에서 멈추게 될것이다.<br>
  > 만약 정렬 리스트에서 1번에서 실패하는 원소부터 n번에서 실패하는 원소까지 n개의 수가 있다고 하면,<br>
  > 정렬된 리스트에서의 탐색 횟수 평균은 **(n(n+1)/2) * (1/n) = (n+1)/2**, 정렬 되지 않은 리스트에서의 탐색 횟수 평균은 **n^2 * (1/n) = n**일 것으로 추측된다.<br>
  > 이 결과대로면, 정렬되어 있을 때의 순차 탐색이 정렬되어 있지 않을 때의 순차 탐색보다 시간이 절반정도 감소한다고 볼 수 있다.<br>
  > 그래도 최고 차수는 둘 다 n이라서, 시간복잡도는 똑같이 **O(n)**이었다.

### 이진 검색
자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행하는 방법
- 자료가 정렬되어 있어야만 한다.
  > 대소 비교를 진행하므로 정렬되어야 함이 맞다.
- 다만 정렬되어야 있어야 한다는 특성때문에 생기는 문제도 있다.
  > 기존 자료에 새로운 자료가 삽입이나 삭제되어 정렬이 어그러지면, 다시 정렬하는 추가 작업이 필요하다.

  #### 구현
  비교되지 않은 원소가 하나라도 남아있으면, 탐색을 진행해야 한다.
  ```python
  def binarySearch(arr, n, key):
    start = 0
    end = n - 1
    while start <= end: # 비교되지 않은 원소가 없을 때까지 돈다.
      middle = (start + end) // 2
      if a[middle] == key:
        return True
      elif a[middle] > key:
        end = middle - 1
      else:
        start = middle + 1
    return False # 탐색동안 key값을 찾지 못했을 때
  ```
  중간 인덱스의 값보다 크거나 작다만 비교한다고 생각했었다.<br>그러나 `if a[middle] == key: return True` 구문이 없다면, 중간 인덱스 값과 key가 같을 경우는 비교가 두 번 이상되어 비효율적이고, 다른 if문에 True를 반환하지 않기에 탐색에 성공할 수도 없었다.

### 인덱스 - 이진 탐색 트리


## 선택 정렬
주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치를 교환하는 방식

  #### 과정
  1. 주어진 리스트에서 최소값을 찾는다.
  2. 그 값을 리스트 맨 앞 값과 바꾼다.
  3. 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복한다.

  #### 시간복잡도
  **O(n^2)**
  - 간단하지만 연산량이 많다.

  #### 구현
  ```python
  def selection_sort(arr, n):
    for i in range(n - 1):
      min_idx = i
      for j in range(i + 1, n):
        if arr[min_idx] > arr[j]:
          min_idx = j
      arr[i], arr[min_idx] = arr[min_idx], arr[i]
  ```

## 자체 Q&A


## 공부 내용 돌아보기