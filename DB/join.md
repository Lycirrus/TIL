# Multi Table Query
- 관계
  - 여러 테이블 간의 논리적 연결

## JOIN
둘 이상의 테이블에서 데이터를 검색하는 방법

### INNER JOIN
두 테이블에서 값이 일치하는 레코드에 대해서만 결과를 반환
```sql
SELECT select_list
FROM table_a INNER JOIN table_b
    ON table_b.fk = table_a.pk;
```
- FROM 절 이후 메인 테이블 지정
- INNER JOIN 절 이후 메인 테이블과 조인할 테이블을 지정
- ON 키워드 이후 조인 조건을 작성
- 조건은 조인되는 두 테이블의 레코드를 일치시키는 규칙으로 지정

### LEFT JOIN
오른쪽 테이블의 일치하는 레코드와 함께 왼쪽 테이블의 모든 레코드 반환
```sql
SELECT select_list
FROM table_a LEFT JOIN table_b
    ON table_b.fk = table_a.pk;
```
- INNER JOIN과 다르게 LEFT JOIN에서 ON을 이용해 조건을 작성하면, 양쪽 테이블이 아닌 **왼쪽 테이블**의 각 레코드를 오른쪽 테이블의 모든 레코드와 일치시킴
> 따라서, 결과에 왼쪽 테이블의 모든 레코드가 표시된다.
>
> 오른쪽 테이블과 매칭되지 않는 레코드는 해당 필드에 NULL을 표시한다.