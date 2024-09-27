# Web with Django
## Data Science 복기
### 프로세스
1. 문제정의
2. 데이터 수집 (OPEN API, 캐글 다운로드 등)
3. 데이터 전처리 (결측치 처리, 형변환 등)
4. 데이터 분석
5. 결과 해석 및 공유 (시각화)

## Django에서의 데이터 분석
- Matplotlib, Pandas, Numpy를 Django에서 구동한다.
  > Django에서 사용하면 결과를 웹 페이지에서 보여줄 수 있다.

## Django에 Matplotlib 그래프 적용
- View 에서 Template로 이미지 형식의 데이터는 직접 전달할 수 없다.
- **저장된 이미지의 경로를 전달**하여 Template에서 출력한다.
- matplotlib의 그래프를 이미지 형식으로 **버퍼에 저장** 후 저장된 경로를 전달한다.
  > buffer : 임시로 데이터를 저장하는 공간
- python "BytesIO" 클래스 :
  - 파이썬의 입출력을 위한 내장 모듈인 "io" 모듈에 포함된 클래스
  - 메모리 내에 이진 데이터를 저장 및 조작할 수 있는 기능 제공

# Project 4주차
