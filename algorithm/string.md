# string
## 문자열
파이썬 str 클래스의 메모리 배치는 Java와 유사
sys.getsizeof()

  #### 문자열을 input하는 방법간 차이
  - `list(input())` 
    ```python
    # 입력 : 'abc'
    print(list(input()))

    # 출력 : ['a', 'b', 'c']
    ```
    `list`로 감쌀 경우, 문자의 철자 하나하나 나누어 리스트 형태로 들어온다.
  - `input()`
    ```python
    # 입력 : 'abc'
    print(input())

    # 출력 : abc
    ```
    `input()`만 사용할 경우, 입력한 문자열 그래도 들어온다.

## 패턴 매칭
### 고지식한 알고리즘
본문 문자열을 처음부터 끝까지 순회하여 패턴 내의 문자들을 일일이 비교하는 방식

  #### 예시
  ```python
  sp = 'is'
  tt = 'This is a book~!'
  def Gozisic_al(sp, tt):
    i = 0 # tt의 인덱스
    j = 0 # sp의 인덱스
    while j < len(sp) and i < len(tt):
      if tt[i] != sp[j]:
        i -= j # 일치하지 않을 경우 지금까지 일치했던 개수만큼 뺴고
        j = -1 # j에 -1을 할당한다.
      i += 1
      j += 1 # 모든 순간에 한 칸 뒤로 전진하므로, 위에서 j를 -1로 초기화 하였다.
    if j == M:
      return i - M
    else:
      return -1
    # sp의 모든 요소를 돌았다면, 시작하는 인덱스 i - M을 출력한다.
  ```

### KMP 알고리즘
불일치가 발생한 앞 부분에 대하여 다시 비교하지 않고 매칭을 수행하는 방식

  #### 예시
  ```python
  def kmp(sp, tt):
    n = len(tt)
    m = len(sp)
    lps = [0] * (m + 1)
    # 전처리
    j = 0
    lps[0] = -1
    for i in range(1, m):
      lps[i] = j
      if sp[i] == sp[j]:
        j += 1
      else:
        j = 0
    lps[m] = j
    # 탐색
    i = j = 0
    while i < n and j <= m:
      if j == -1 or tt[i] == sp[j]:
        i += 1
        j += 1
      else:
        j = lps[j]
      if j == m:
        print(i - m, end=' ')
        j = lps[j]
  ```

### 보이어-무어 알고리즘
오른쪽에서 왼쪽으로 비교하는 방식
> 전체 문자열과 찾는 문자열을 비교하여 일치하지 않았을 때,<br>
> 전체 문자열 부분의 마지막 요소가 찾는 문자열 내에 있으면<br>
> 그 문자열과 찾는 문자열을 맞추고 다시 판별한다.<br>
> 없다면 찾는 문자열의 길이만큼 점프한다!

## 자체 Q&A


## 