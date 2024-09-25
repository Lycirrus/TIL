# Django Form
### HTML 'form'
사용자로부터 데이터를 제출 받기위해 활용한 방법
- 비정상적 혹은 악의적인 요청을 필터링 할 수 없음
- `유효한 데이터인지에 대한 확인 필요`

### 유효성 검사
- 수집한 데이터가 정확하고 유효한지 확인하는 과정

  #### 유효성 검사의 어려움
  - 유효성 검사를 구현하기 위해 입력값, 형식, 중복, 범위, 보안 등 많은 것들을 고려해야 함
  - 위 과정을 Django에서 제공하는 Form을 사용하여 진행

## Django Form
사용자 입력 데이터를 수집하고, 처리 및 유효성 검사를 수행하기 위한 도구
- 유효성 검사를 단순화하고 자동화할 수 있는 기능을 제공

  #### Form class 정의
  ```python
  # forms.py

  from django import forms

  class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()
  ```

  #### Form class 적용
  - view 함수 변경
  ```python
  # views.py

  from .forms import ArticleForm

  def new(request):
    form = ArticleForm()
    context = {
      'form' = form,
    }
    return render(request, 'articles/new.html', context)
  ```

  - html에서 form 인스턴스 출력
  ```html
  <form action="{% url 'articles:create' %}" method="POST">
    {{ form }}
    <input type="submit">
  </form>
  ```

### Widgets
HTML 'input' 요소의 표현을 담당

  #### 사용법
  - form의 함수 요소로 사용
  ```python
  class ArticleForm(forms.Form):
    ...
    content = forms.CharField(widget=forms.Textarea)
  ```

## Django ModelForm
- ModelForm : 사용자 입력 데이터를 DB에 저장해야 할 때 사용
  > Model과 연결된 Form을 자동으로 생성해주는 기능을 제공한다.

  #### 예시
  ```python
  class ArticleForm(forms.Form):
    class 
  ```

### Meta class



### ModelForm 적용




## HTTP 요청 다루기



### View 함수 구조 변화




### new & create 함수 결합




### edit & update 함수 결합




## 참고
### ModelForm의 키워드 인자 구성




### Widgets 응용




### 필드를 수동으로 렌더링