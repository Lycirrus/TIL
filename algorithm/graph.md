# 그래프
정점들의 집합과 이들을 연결하는 간선들의 집합으로 구성된 자료구조이다.

### 그래프 유형
- 무향 그래프 : 노드 간 양방향으로 이동할 수 있는 그래프
- 유향 그래프 : 정해진 방향(단방향)으로마나 이동할 수 있는 그래프
- 가중치 그래프 : 간선에 가중치가 부여된 그래프
  > 양방향의 가중치가 동일하다면 무향, 방향에 따라 다르다면 유향으로 볼 수 있다.
- 사이클 없는 방향 그래프 : 순환이 없는 사이클
  > 트리가 대표적이다.
- 완전 그래프 : 정점들 간에 가능한 모든 간선을 가진 그래프
  > 최악의 케이스로 자주 활용된다.
- 부분 그래프 : 원래 그래프에서 일부의 정점이나 간선을 제외한 그래프

### 그래프 표현
- 인접 행렬
  - 2차원 배열을 이용하여 연결 여부를 저장하는 방식
  
  #### 장점
  연결 여부를 한 번에 파악할 수 있다.

  #### 단점
  연결 되지 않은 노드끼리도 표현되다 보니 메모리 누수가 발생한다.

- 인접 리스트
  - 각 정점마다 해당 정점으로 나가는 간선의 정보를 저장
  > 인접 행렬과 다르게 연결 정보만 저장한다.

  #### 장점
  연결된 노드 간의 정보만 담아 메모리 활용이 효율적이다.

  #### 단점
  연결 정보 확인을 한 눈에 파악하기 힘들다.

> 다만 실무에서는 데이터의 삽입/삭제가 많이 발생하므로, 연결 리스트를 활용한다.

## Disjoint Set


## 최소 신장 트리(MST)
그래프에서의 최소 비용 문제는 아래와 같이 있다.

1. 모든 정점을 연결하는 간선들의 가중치의 합이 최소가 되는 트리
2. 두 정점 사이의 최소 비용 경로 탐색

- 신장 트리
  - **무방향 그래프**에서 모든 n개의 정점이 연결되어 n - 1개의 간선으로 이루어진 트리

최소 신장트리는 **무방향 가중치 그래프**에서 신장 트리를 구성하는 간선들의 **가중치 합이 최소**인 신장 트리를 말한다.

## MST 구현 방법
1. **Prim 알고리즘**
2. **Kruskal 알고리즘**

### 두 방법의 공통점과 차이점
- 공통점 : 그리디 방식으로 접근한다.
  > 작은 것부터 선택하게 된다.

- 차이점 :
  - `Prim 알고리즘` : 정점을 기준으로 생각한다.
  - `Kruskal 알고리즘` : 간선을 기준으로 생각한다.

### Prim 알고리즘
하나의 정점에서 연결된 간선들 중 하나를 선택하면서 MST를 만들어 가는 방식이다.

- 서로소인 2개의 집합 정보를 유지한다.
  - 트리 정점 : MST를 만들기 위해 선택된 정점들의 집합
  - 비트리 정점 : 선택되지 않은 정점들의 집합

#### 순서
1. 임의의 정점을 하나 선택하여 시작한다.
2. 선택한 정점과 인접하는 정점들 중 최소 비용의 간선이 존재하는 정점을 선택한다.
3. 모든 정점이 선택될 때까지 1 ~ 2번 과정을 반복한다.

### Kruskal 알고리즘
간선을 하나씩 선택해서 최소 신장 트리를 찾는 방식이다.

#### 순서
1. 처음에 모든 간선을 가중치에 따라 **오름차순** 정렬한다.
2. 최소 가중치 간선부터 선택하여 트리를 증기시킨다.
   > 사이클이 존재하면 다음으로 가중치가 낮은 간선을 선택한다.
   >
   > n - 1개가 넘어가 신장 트리가 깨지게 된다.
   >
   > **Union Find**를 활용하여 같은 집합에 방문했는지 확인하여 사이클을 방지한다.
3. n - 1개(모든 정점의 연결)의 간선이 선택될 때까지 2번을 반복한다.

## 최단 경로 탐색
- 한 시작 정점에서 끝 정점까지의 최단 경로
  - `다익스트라` : 음의 가중치 불허
  - `벨만-포드` : 음의 가중치 허용
- 모든 정점들에 대한 최단 경로
  - `플로이드-워샬`

### 다익스트라
시작 정점에서 **거리가 최소**인 정점을 선택해 나가면서 최단 경로를 구하는 방식이다.
> 탐욕 기법을 사용한 알고리즘의 MST의 프림 알고리즘과 유사한다.
>> 다만 차이점이 존재한다.
>>
>> - Prim : 인접 정점 중 가장 가중치가 적은 것 선택
>> - Dijkstra : 인접 정점 중 가장 누적 가중치가 적은 것 선택