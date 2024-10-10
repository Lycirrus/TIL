# Database
체계적인 데이터 모음

- 데이터 : 저장이나 처리에 효율적인 형태로 변환된 정보

### 기존 데이터 관리
1. 파일
2. 스프레드시트
   - 일반적으로 약 100만 행까지만 저장가능
   - 단순히 파일이나 링크 소유 여부에 따른 단순한 접근 권한 기능 제공
   - 데이터를 바꿀 수는 있지만 데이터가 여러 시트에 분산되어 있다면 변경에 누락이 생기거나 추가 문제가 발생할 수 있음
    > 크기, 보안, 정확성 부분의 한계가 존재

### 데이터베이스 역할
- 데이터를 저장하고 조작(*CRUD*)

## 관계형 데이터베이스
데이터 간에 **관계**가 있는 데이터 항목들의 모음

- 테이블, 행, 열의 정보를 구조화하는 방식
- **서로 관련된 데이터 포인터**를 저장하고 이에 대한 **액세스**를 제공

### 관계
- 여러 테이블 간의 논리적 연결

  #### 관계로 할 수 있는 것
  - 관계를 이용해 두 테이블에서 데이터를 다양한 형식으로 조회 가능

### 관계형 데이터베이스 관련 키워드
1. Table (Relation)
   - 데이터를 기록하는 곳
2. Field (Column, Attribute)
   - 고유한 데이터 형식이 지정
3. Record (Row, Tuple)
   - 구체적인 데이터 값이 저장
4. Database (Schema)
   - 테이블의 집합
5. Primary Key (기본키, pk)
   - 각 레코드의 고유한 값
   - 관계형 데이터베이스에서 레코드의 **식별자**로 활용
6. Foreign Key (외래키, fk)
   - 테이블의 필드 중 다른 테이블 레코드를 식별할 수 있는 키
   - 다른 테이블의 기본키를 참조
   - 각 레코드에서 서로 다른 테이블 간의 **관계를 만드**는데 사용

## RDBMS
관계형 데이터베이스를 관리하는 소프트웨어 프로그램
> DBMS : 데이터베이스를 관리하는 소프트웨어 프로그램
> > - 데이터 저장 및 관리를 용이하게 하는 시스템
> > - 데이터베이스와 사용자 간의 인터페이스 역할
> > - 사용자가 데이터 구성, 업데이트, 모니터링, 백업, 복구 등을 할 수 있도록 도움

## SQL (Structure Query Language)
데이터베이스에 정보를 저장하고 처리하기 위한 프로그래밍 언어

### SQL Syntax
- SQL 키워드는 대소문자를 구분하지 않음
  - 그러나 대문자 작성 권장 (명시적 구분)
- 각 SQL Statements 끝에는 세미콜론 필요
  - 각 SQL Statements를 구분하는 방법

### SQL Statements
SQL을 구성하는 가장 기본적인 코드 블록

  #### 4가지 유형
  1. DDL : 데이터 정의
  2. DQL : 데이터 검색
  3. DML : 데이터 조작
  4. DCL : 데이터 제어

  |유형|역할|키워드|
  |:--:|:-:|:----:|
  |`DDL`|데이터의 기본 구조 및 형식 변경|**CREATE<br>DROP<br>ALTER**|
  |`DQL`|데이터 검색|**SELECT**|
  |`DML`|데이터의 조작|**INSERT<br>UPDATE<br>DELETE**|
  |`DDL`|데이터 및 작업에 대한 사용자 권한 제어|**COMMIT<br>ROLLBACK<br>GRANT<br>REVOKE**|

### Query
- 데이터베이스로부터 정보를 요청
  
<br></br>

# Single Table Queries
## Querying
### SELECT
- 테이블에서 데이터를 조회
  - SELECT 키워드 다음에 활용할 필드를 입력
  - FROM 키워드 다음에 그 필드가 있는 테이블을 입력
  ```sql
  SELECT field_name FROM table_name;
  ```
  > 전체 조회
  > ```sql
  > SELECT * FROM table_name;
  > ```
  >
  > 조회 시 출력 필드명 설정
  > ```sql
  > SELECT field_name AS fn FROM table_name;
  > ```

## Sorting
### ORDER BY
- 조회 결과의 레코드를 정렬
  - FROM 다음에 위치
  - ASC는 오름차순, DESC는 내림차순
  - 지정하지 않으면 오름차순이 기본으로 적용된다
  ```sql
  SELECT field_name FROM table_name ORDER BY column1 DESC, column2 ASC;
  ```
  - NULL 값은 오름차순에서 가장 먼저 출력

## Filtering
### DISTINCT
- 조회 결과에서 중복된 레코드를 제거
  - SELECT 키워드 바로 뒤에 작성
  - DISTINCT 다음에 고유한 값을 선택하려는 하나 이상의 필드를 지정
  ```sql
  SELECT DISTINCT field_name FROM table_name;
  ```

### WHERE
- 조회 시 특정 검색 조건을 지정
  - FROM 다음에 위치
  - 비교연산자나 논리연산자를 이용하여 조건 설정
  ```sql
  SELECT field_1, field_2, field_3, field_4, field_5 
  FROM table_name 
  WHERE (field_1 = 'case' AND field_2 != 'case' AND field_3 IS NOT NULL) OR field_4 BETWEEN 10 AND 50
  OR field_5 IN ('case1', 'case2', 'case3')
  OR field_1 LIKE '%nn'
  OR field_2 LIKE '___a';

### LIMIT
- 조회하는 레코드 수 제한
  > 처음부터 n개 조회
  > ```sql
  > SELECT * FROM table_name LIMIT n;
  > ```
  > m번째부터 n개 조회
  > ```sql
  > SELECT * FROM table_name LIMIT m - 1, n;
  > ```

### Operators
- `IN` : 값이 특정 목록 안에 있는지 확인
- `LIKE` : 값이 특정 패턴에 일치하는지 확인
  - `%` : 0개 이상의 문자열과 일치하는지 확인
  - `_` : 단일 문자와 일치하는지 확인

## Grouping
### GROUP BY
- 레코드를 집계함수로 그룹화하여 요약본 생성
  - FROM 및 WHERE 절 뒤에 배치
  - GROUP BY 절 뒤에 그룹화 할 필드 목록을 작성
  > 예시
  > ```sql
  > SELECT composer, AVG(bytes) AS avgBytes
  > FROM table_name
  > GROUP BY composer
  > ORDER BY avgBytes DESC;
  > ```
  > ```sql
  > SELECT composer, avg(bytes) AS avgBytes
  > FROM table_name
  > GROUP BY composer
  > HAVING avgBytes < 10;
  > ```
  
  #### HAVING
  - 집계 항목에 대한 세부 조건을 지정
  - 주로 GROUP BY와 함께 사용

  #### 집계 함수
  - 값에 대한 계산을 수행하고 단일한 값을 반환하는 함수
  - `SUM`, `AVG`, `MAX`, `MIN`, `COUNT`

## SELECT Statement 실행 순서

|순번|키워드|내용|
|:-:|:----:|:--|
|1|`FROM`|테이블에서|
|2|`WHERE`|특정 조건에 맞추어|
|3|`GROUP BY`|그룹화 하고|
|4|`HAVING`|그룹 조건을 맞추고|
|5|`SELECT`|조회하여|
|6|`ORDER BY`|정렬하여|
|7|`LIMIT`|특정 위치의 값을 가져온다|