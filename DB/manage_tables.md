# Managing Tables
테이블을 생성, 구조 변경, 삭제 등의 행위가 테이블을 관리하는 것이다.
- 사용 키워드
  - `CREATE`, `DROP`, `ALTER`

## CREATE TABLE
```sql
CREATE TABLE table_name (
  column_1 data_type constraints,
  column_2 data_type constraints,
  ...,
);
```
- 각 필드에 적용할 데이터 타입 작성
- 테이블 및 필드에 대한 제약조건 작성

  #### 예시
  ```sql
  CREATE TABLE table_name (
    exId INTEGER PRIMARY KEY AUTOINCREMENT,
    last_name VARCHAR(50) NOT NULL,
    first_name VARCHAR(50) NOT NULL
  );
  ```

### PRAGMA
```sql
PRAGMA table_info('table_name');
```
- 데이터의 구조를 확인하는데 사용

> `cid`
> - Column ID를 의미한다.
> - 각 컬럼의 고유한 식별자로 사용되는 정수
> - PRAGMA 명령과 같은 메타데이터 조회에서 출력 값으로 활용

### SQLite 데이터 타입
- `NULL` : 아무런 값도 포함하지 않음을 나타냄
- `INTEGER` : 정수
- `REAL` : 부동 소수점
- `TEXT` : 문자열
- `BLOB` : 이미지, 동영상, 문서 등의 바이너리 데이터

### Constraints
테이블의 필드에 적용되는 규칙 또는 제한 사항
- 데이터의 무결성을 유지하고, 일관성을 보장한다.

  #### 대표 Constraints
  - `PRIMARY KEY` : 해당 필드를 기본키로 지정
    > `INTEGER` 타입에만 적용되며, `INT`나 `BIGINT`와 같은 다른 정수 유형은 적용되지 않는다.
  - `NOT NULL` : 해당 필드에 NULL 값을 허용하지 않도록 지정
  - `FOREIGN KEY` : 다른 테이블과의 외래 키 관계를 정의

### AUTOINCREMENT
- 자동으로 고유한 정수 값을 생성하고 할당하는 필드 속성

  #### 특징
  - 필드의 자동 증가를 나타내는 특수한 키워드
  - 주로 PRIMARY KEY에 적용
  - INTEGER PRIMARY KEY AUTOINCREMENT가 작성된 필드는 항상 새로운 레코드에 대해 이전 최대 값보다 큰 값을 할당
  - 삭제된 값은 무시되며, 재사용할 수 없음

## ALTER TABLE

|명령어|역할|
|:---:|:--:|
|`ADD COLUMN`|필드 추가|
|`RENAME COLUMN`|필드 이름 변경|
|`DROP COLUMN`|필드 삭제|
|`RENAME TO`|테이블 이름 변경|

### ADD COLUMN
```sql
ALTER TABLE
  table_name
ADD COLUMN
  column_definition;
```
- 추가하고자 하는 새 필드 이름과 데이터 타입 및 제약 조건 작성
- 단, NOT NULL 제약조건이 있을 경우 NULL이 아닌 기본값 설정 필요

### RENAME COLUMN
```sql
ALTER TABLE
  table_name
RENAME COLUMN
  current_name TO new_name;
```
- 바꾸려는 필드의 이름을 지정하고 TO 키워드 뒤에 새 필드 이름을 지정

### DROP COLUMN
```sql
ALTER TABLE
  table_name
DROP COLUMN
  column_name;
- 삭제할 필드 이름 지정
```

### RENAME TO
```sql
ALTER TABLE
  table_name
RENAME TO
  new_table_name;
```
- 새로운 테이블 이름 지정

## DROP TABLE
```sql
DROP TABLE table_name;
```
삭제할 테이블 이름 작성

# Managing Data
## INSERT
```sql
INSERT INTO table_name (c1, c2, ...)
VALUES (v1, v2, ...);
```
- 테이블 이름을 적고 괄호 안에 필드 목록 작성
- VALUES 키워드 다음 괄호 안에 해당 필드에 삽입할 값 목록 작성

## UPDATE
```sql
UPDATE table_name
SET column_name=expression
[WHERE condition];
```
- 수정할 필드와 새 값을 지정
- WHERE 절에서 수정할 레코드를 지정하는 조건 작성
- WHERE 절을 작성하지 않으면 모든 레코드 수정

## DELETE
```sql
DELETE FROM table_name
[WHERE condition];
```
- 삭제할 레코드가 있는 테이블 이름 작성
- WHERE 절에서 삭제할 레코드를 지정하는 조건 작성
- WHERE 절을 작성하지 않으면 모든 레코드 삭제