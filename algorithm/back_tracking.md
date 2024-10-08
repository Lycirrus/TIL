# 백트래킹과 그래프
## 백트래킹 응용
여러 가지 선택지들이 존재하는 상황에서 한가지를 선택하는 것을 반복하여 해답을 찾는 방식
> 트리는 자료구조, 백트래킹은 알고리즘

### 백트래킹과 DFS 차이
- 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않는다. *(Prunning, 가지치기)*

### 접근법
DFS로 접근을 한 후에 가지치기로 경우의 수를 제거한다.
- 따라서 최악의 경우는 DFS일 때 이다.
- 가지치기를 이용해서 경우의 수를 줄인다.

  #### 절차
  1. 상태 공간 트리의 DFS를 실시한다.
  2. 설계단계에서 유망하지 않은 경우를 생각하고 구현한다.
  3. 각 노드가 유망한지 점검한다.
  4. 유망하지 않은 경우 부모 노드로 돌아가서 검색을 재개한다.

  #### 예시
  N-Queen 문제
  - 8개의 퀸을 경로가 겹치지 않게 두는 방법을 찾는 문제이다.
    - 퀸 8개를 64칸의 체스판에서 위치를 정해주는 것이므로 기본적으로는 '64C8'의 경우를 구해야 한다.
      > 약 44억 가지 경우

      > 지나치게 경우의 수가 많다.
    - 하나의 가로줄에 하나만 놓을 경우, '8^8'이 된다.
      > 약 1,678만 가지 경우

      > 기존보단 줄었지만 그래도 경우의 수가 많다.
    - 하나의 가로줄 및 세로줄에 하나의 퀸을 둘 경우를 찾으면 '8!'만큼만 탐색하면 된다.
      > 약 4만 가지 경우

      > 가로줄과 세로줄 당 하나인 경우의 가지만 남기고 다른 가지를 모두 쳐냄으로써 탐색해야하는 경우의 수를 크게 줄였다.
    - 퀸은 대각선도 이동할 수 있으므로, 대각선으로 겹치는 경우도 가지치기 하면 경우를 더 줄일 수 있다.
  
## 이진 트리
이전의 1차원 배열 리스트로 이진 트리를 표현할 경우, 삭제 과정이 있다면 메모리 낭비가 있어서 사용하지 않아야 한다.
- 연결 리스트 활용


## BST
탐색작업을 효율적으로 하기 위한 자료구조

### 특징
1. 모든 원소는 서로 다른 유일한 키를 갖는다.
2. 항상 루트 노드와 비교하여 작은 값이 왼쪽 서브트리에, 큰 값이 오른쪽 서브트리에 존재한다.
3. 각각의 왼쪽과 오른쪽 서브트리도 하나의 이진 탐색 트리이다.
4. 중위 순회하면 오름차순으로 정렬된 값을 얻을 수 있다.

### 탐색 연산
1. 루트에서 탐색 시작
2. 탐색할 키 값 x를 루트 노드의 키 값 k와 비교
    - `x == k` : 탐색 성공
    - `x < k` : 왼쪽 서브트리에 대해 탐색 연산 수행
    - `x > k` : 오른쪽 서브트리에 대해 탐색 연산 수행
3. 서브 트리에 대해 순환적으로 탐색 연산을 반복
    - 탐색 수행할 서브 트리가 없다면 탐색 실패