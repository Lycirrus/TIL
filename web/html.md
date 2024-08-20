# Html & CSS
## 웹
- WWW(World Wide Web)
  : 인터넷으로 연결된 컴퓨터들이 정보를 공유하는 거대한 정보 공간
- Web : Web Site나 Application 등을 통해 사용자들이 정보를 검색하고 상호 작용하는 기술
- Web Site : 인터넷에서 여러 개의 Web page가 모인 것으로, 사용자들에게 정보나 서비스를 제공하는 공간
- Web page : HTML, CSS 등의 웹 기술을 이용하여 만들어진, "Web Site"를 구성하는 하나의 요소

### 웹 페이지 구성요소
웹 페이지는 크게 **구조, 스타일, 작동 방식**이 있다.
1. 구조 : HTML
2. 스타일 : CSS
3. 작동 : Javascript

## 웹 구조화
### HTML
웹 페이지의 의미와 **구조**를 정의하는 언어

- HyperText Markup Language

  #### HyperText
  웹 페이지를 다른 페이지로 연결하는 링크

  #### HyperText 특징
  - 비선형성
  - 상호 연결성
  - 사용자 주도적 탐색

  #### Markup Language
  태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어

### HTML의 구조
- `<!DOCTYPE html>`
  - 해당 문서가 html 문서라는 것을 나타냄
- `<html></html>`
  - 전체 페이지의 콘텐츠를 포함
- `<title></title>`
  - 브라우저 탭 및 즐겨찾기 시 표시되는 제목으로 사용
- `<head></head>`
  - HTML 문서에 관련된 설명, 설정 등의 컴퓨터가 식별학는 메타데이터를 작성
  - 사용자에게 보이지 않음
- `<body></body>`
  - HTML 문서의 내용을 나타냄
  - 페이지에 표시되는 모든 콘텐츠를 작성
  - 한 문서에 하나의 body 요소만 존재

  #### HTML 요소
  하나의 요소는 **여는 태그**와 **닫는 태그** 그리고 그 안의 **내용**으로 구성됨
  - 닫는 태그는 태그 이름 앞에 슬래시가 포함됨
  - 닫는 태그가 없는 태그도 존재

  #### HTML 속성
  사용자가 원하는 기준에 맞도록 요소를 설정하거나 다양한 방식으로 요소의 동작을 조절하기 위한 값
  - 나타내고 싶지 않지만 추가적인 기능, 내용을 담고 싶을 때 사용
  - CSS에서 스타일 적용을 위해 해당 요소를 선택하기 위한 값으로 활용됨

  #### HTML 속성 규칙
  1. 속성은 요소 이름과 속성 사이에 공백이 있어야 함
     >`<meta name=...>`
  2. 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백으로 구분함
     >`<... name="" content="">`
  3. 속성 값은 열고 닫는 따옴표로 감싸야 함
     >`"UTF-8"`

### HTML Text Structure
HTML의 주요 목적 중 하나는 **텍스트 구조와 의미**를 제공하는 것

  #### 대제목
  `<h1>대제목</h1>` : **현재 문서의 최상위 제목**이라는 의미 부여
  - 여러 번 사용가능하나, 관용적으로 한 번만 사용!

  #### 기울임꼴
  `<em>기울임꼴</em>` : 글자를 기울임

  #### 볼드체
  `<strong>볼드체</strong>` : 글자를 볼드체로 변경

  #### 리스트
  - 순서가 있는 리스트
  ```html
  <ol>
    <li>파이썬</li>
    <li>알고리즘</li>
    <li>웹</li>
  </ol>
  ```
  > 앞에 숫자가 매겨지는 리스트가 만들어진다.
  - 순서가 없는 리스트
  ```html
  <ul>
    <li>파이썬</li>
    <li>알고리즘</li>
    <li>웹</li>
  </ul>
  ```
  > 앞에 기호(동그라미)로 매겨지는 리스트가 만들어진다.

## 웹 스타일링
### CSS
웹 페이지의 디자인과 레이아웃을 구성하는 언어

  #### CSS 구문
  ```CSS
  h1 {
    color: red;
    font-size: 30px;
  }
  ```
  - `h1` : 선택자 (Selector)
  - `color: red;` : 선언 (Declaration)
  - `color` : 속성 (Property)
  - `red` : 값 (Value)

  > CSS는 들여쓰기를 하지 않아도 된다. 그러나 가시성을 위해 들여쓴다.<br>
  
  > CSS의 선언 끝에는 `;`를 넣어 종료를 알린다.

  #### CSS 적용 방법
  1. 인라인(Inline) 스타일
     - HTML 요소 안에 style 속성 값으로 작성
     ```HTML
     <h1 style="color: blue; background-color:yellow;"></h1>
     ```
  2. 내부(Internal) 스타일 시트
     - head 태그 안에 style 태그에 작성
     ```HTML
     <head>
      <style>
        h1 {
          color: blue;
          background-color: yellow;
        }
      </style>
     </head>
     ```
  3. 외부(External) 스타일 시트
     - 별도 CSS 파일 생성 후 HTML link 태그를 사용해 불러오기
     ```HTML
     <!-- HTML -->
     <link rel="stylesheet" href="style.css">
     ```
     ```CSS
     /* CSS */
     h1 {
      color: blue;
      background-color: yellow;
     }
     ```

### CSS 선택자
HTML 요소를 선택하여 스타일을 적용할 수 있도록 하는 선택자

- 기본 선택자
  
  |선택자|범위|
  |:---:|:--:|
  |전체 선택자|`*`|
  |요소 선택자|`tag`|
  |클래스 선택자|`class`|
  |아이디 선택자|`id`|
  |속성 선택자|`attr`|

- 결합자
  - 자손 결합자 (" " (space))
  - 자식 결합자 (**">"**)

  #### 기본 선택자
  - 전체 선택자
    - HTML 모든 요소를 선택
    ```HTML
    <style>
      * {}
    </style>
    ```
  - 요소 선택자
    - 지정한 모든 태그를 선택
    ```HTML
    <style>
      h1 {}
    </style>
    ```

### 명시도
결과적으로 요소에 적용할 CSS 선언을 결정하기 위한 알고리즘

### Cascade
한 요소에 동일한 가중치를 가진 선택자가 적용될 때, CSS에서 마지막에 나오는 선언이 사용됨

  #### 명시도 순서
  1. Importance<br>
   `!important`
  2. Inline 스타일
  3. 선택자
  - `id 선택자 > class 선택자 > 요소 선택자`
  4. 소스 코드 선언 순서 

  > 작업 과정에서의 혼란을 줄이기 위해 class 선택자로 통일<br>

  > id 선택자는 요소 한 개에만 적용하기에 혹은 그런 의미기에 거의 사용하지 않음

### CSS 상속
부모 요소의 속성을 자식에게 상속해 재사용성을 높임

  #### CSS 속성 분류
  - 상속 되는 속성

## CSS Box Model(수정 필필요)
웹 페이지의 모든 HTML 요소를 감싸는 사각형 상자 모델

  #### 박스 타입
  1. Block box : 
  2. Inline box

## CSS Position
### CSS Layout
각 요소의 **위치**와 **크기**를 조정하여 웹 페이지의 디자인을 결정하는 것
- `Display`, `Position`, `Flexbox` 등이 있다.

### CSS Position
요소를 Normal Flow에서 제거하여 다른 위치로 배치하는 것
- 다른 요소 위에 올리거나 화면의 특정 위치에 고정시키기

  #### Position의 이동 방향
  1. top
  2. bottom
  3. left
  4. right
  5. Z axis
      > ppt에서 맨 위로 보내기, 맨 아래로 보내기와 같은 기능 