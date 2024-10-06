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

  #### form 예시
  ```python
  from .models import Article

  class ArticleForm(forms.ModelForm):
    class Meta:
      model = Article
      fields = '__all__'
  ```
  > 내부 클래스는 Django 제작자 측에서 단순히 이렇게 사용하라는 용도로 만들어둔 것이다.

### Meta class
- Meta data : 데이터의 데이터
- model form 에서의 Meta class
  - model form에 대한 정보를 작성하는 클래스이다.

  #### Meta class 속성
  - model 속성 : 기반이 되는 모델을 입력
  - fields 속성 : 모델이 가지는 필드들 중 사용할 필드를 정의
  - exclude 속성 : 모델에서 포함하지 않을 필드를 지정

### ModelForm 적용
  #### create 로직
  ```python
  # views.py

  from .forms import ArticleForm

  def create(request):
    # 1. 모델폼 인스턴스 생성 (+ 사용자 입력 데이터를 통째로 인자로 작성)
    form = ArticleForm(request.POST)

    # 2. 유효성 검사
    if form.is_valid():
      article = form.save()
      return redirect('articles:detail', article.pk)
      ## 실패하면 Django에서 실패 이유를 form과 함께 넘겨준다.
    context = {
      'form': form,
    }
    return render(request, 'articles/new.html', context)
  ```

  - `is_valid()` : 여러 유효성 검사를 실행하고, 데이터가 유효한지에 대한 여부를 Boolean 형태로 반환한다.

  #### edit 로직
  ```python
  # views.py

  def edit(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(instance=article)
    context = {
      'article': article,
      'form': form,
    }
    return render(request, 'articles/edit.html', context)
  ```

  #### update 로직
  ```python
  def update(request, pk):
  article = Article.objects.get(pk=pk)
  form = ArticleForm(request.POST, instance=article)
  if form.is_valid():
    form.save()
    return redirect('articles:detail', article.pk)
  context = {
    'article': article,
    'form': form,
  }
  return render(request, 'articles/edit.html', context)
  ```

### Save 메서드
- `save()` : DB 객체를 만들고 저장하는 ModelForm의 인스턴스 메서드

  #### save 메서드가 생성과 수정을 구분하는 법
  키워드 인자 **instance** 여부를 통해 생성과 수정을 결정한다.

## HTTP 요청 다루기
- new와 create 함수의 공통점 및 차이점
  - 공통점 : 데이터 생성을 구현하기 위해 존재한다.
  - 차이점 : new는 `GET` method 요청만을, create는 `POST` method 요청만을 처리한다.

### new & create 함수 결합
```python
def create(request):
  # POST 일 경우
  if request.method == "POST":
    # 객체 생성 및 자료 저장 로직
    form = ArticleForm(request.POST)
    if form.is_valid():
      article = form.save()
      return redirect('articles:detail', article.pk)
  # POST가 아닐 경우
  else:
    # new함수에서의 form 인스턴스 생성
    form = ArticleForm()
  # POST인데 타당하지 않은 form일 경우 반환점이 필요하다.
  context = {
    'form': form,
  }
  return render(request, 'articles/create.html', context)
```

- 요청에 따른 변화
  - `GET`: 게시글 **생성 페이지**를 요청
  - `POST`:게시글 **생성**을 요청

### edit & update 함수 결합
```python
def update(request, pk):
  article = Article.objects.get(pk=pk)
  if request.method == "POST":
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid():
      form.save()
      return redirect('articles:detail', article.pk)
  else:
    form = ArticleForm(instance=article)
  context = {
    'article': article,
    'form': form,
  }
  return render(request, 'articles/update.html', context)
```

## 참고
### ModelForm의 키워드 인자 구성
ModelForm의 생성자 함수를 보면
> `data`는 첫번째 인자이다.
>
> `instance`는 9번째 인자이다.

- 따라서 data인 request.POST는 data 키워드를 사용하지 않아도 되지만, instance는 그렇지 않다.

### Widgets 응용
Form 클래스 안, Meta 클래스 위쪽에 입력한다.
```python
... # widget은 표현담당
title = forms.CharField(widget = forms.TextInput(
  attrs = {
    'class': 'my-title',
    'placeholder': 'Enter the title',
    'maxlength': 10,
    'rows': 5,
    'cols': 50,
  }
error_messages = {'오류 메세지!'}
))
```
