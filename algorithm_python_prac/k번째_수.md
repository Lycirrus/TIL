# k번째 수
- N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열의 S번째부터 E번째까지의 수를 오름차순 정렬했을 때 k번째로 나타나는 숫자를 출력하는 프로그램을 작성하시오.

<br>
<details>
  <summary>입력설명</summary>
  <div markdown = 1>
    첫째 줄에 테스트 케이스 T<span style="color: #808080">(1<=T<=10)</span>가 주어진다.<br>
    케이스마다<br>
    첫째 줄은 자연수 N<span style = "color: #808080">(5<=N<=500)</span>, S, E, k가 차례로 주어진다.<br>
    둘째 줄에 N개의 숫자가 차례로 주어진다.
  </div>
</details>
<br>
<details>
  <summary>출력설명</summary>
  <div markdown = 1>
    각 케이스별 k번째 수를 "<em>#1 n</em>"의 형태로 출력하시오.
  </div>
</details>
<br>

## 접근방법
N개의 숫자를 list 형식으로 받은 뒤 S번째부터 E번째까지를 새로운 리스트로 생성한다. 해당 리스트를 `sort`를 이용하여 오름차순으로 정렬한 뒤 k번째 값을 프린트하기로 했다.

## 코드 순서
- 먼저 테스트 케이스 횟수 t를 받아왔다.

  ```python
  t = int(input())
  ```

- 그다음 N, S, E, k와 nlist를 int형으로 받았다.
  ```python
  n, s, e, k = map(int, input().split())
  nlist = list(map(int, input().split()))
  ```

- 리스트는 index가 0부터 시작하므로 받은 리스트의 `[S-1:E]`만큼을 새로운 리스트로 생성했다.
  
  ```python
  ninli = nlist[s-1:e]
  ```

- 마지막으로 sort로 정렬하고, k번째 값을 print하였다.
  ```python
  ninli.sort()
  print("#%d %d" %(j+1, ninli[k-1]))
  ```
  #### 전체코드
  ```python
  t = int(input())
  for j in range(t):
  n, s, e, k = map(int, input().split())
  nlist = list(map(int, input().split()))
  ninli = nlist[s-1:e]
  ninli.sort()
  print("#%d %d" %(j+1, ninli[k-1]))
  ```