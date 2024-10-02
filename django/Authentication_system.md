# Authentication System
## Cookie & Session
### HTTP
HTML 문서와 같은 리소스들을 가져올 수 있도록 해주는 규약

  #### 특징
  1. 비 연결 지향
    - 서버는 요청에 대한 응답을 보낸 후 연결을 끊음
  2. 무상태
    - 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음
  > 상태가 없으면 로그인 상태를 유지할 수 없다.

### 쿠키
서버가 사용자의 웹 브라우저에 전송하는 작은 데이터 조각
- **서버가 제공**하여 클라이언트 측에 저장되는 **작은 데이터 파일**
- 사용자 인증, 추적, 상태 유지 등에 사용되는 데이터 저장 방식

  #### 동작 예시
  1. 브라우저가 웹 서버에 웹 페이지를 요청
  2. 웹 서버는 요청된 페이지와 함께 쿠키를 포함한 응답을 브라우저에게 전송
  3. 브라우저는 받은 쿠키를 저장소에 쿠키의 속성(만료 시간, 도메인, 주소 등)과 함께 저장
  4. 이후 브라우저가 같은 웹 서버에 웹 페이지를 요청할 때, 저장된 쿠키 중 해당 요청에 적용 가능한 쿠키를 포함하여 함께 전송
  5. 웹 서버는 받은 쿠키 정보를 확인하고, 필요에 따라 사용자 식별이나 세션 관리 등을 수행
  6. 웹 서버는 요청에 대한 응답을 보내며, 필요한 경우 새로운 쿠키를 설정하거나 기존 쿠키를 수정할 수 있음

  #### 작동 원리
  1. 쿠키 저장 방식
    - 브라우저는 쿠키를 KEY-VALUE 데이터 형식으로 저장한다.
    - 쿠키에는 이름, 값 외에도 만료시간, 도메인, 경로 등의 추가 속성이 포함된다.
  2. 쿠키 전송 과정
    - 서버는 HTTP 응답 헤더의 Set-Cookie 필드를 통해 클라이언트에게 쿠키를 전송한다.
    - 브라우저는 받은 쿠키를 저장해 두었다가, 동일한 서버에 재요청 시 HTTP 요청 헤더의 Cookie 필드에 저장된 쿠키를 함께 전송한다.
  3. 쿠키의 주요 용도
    - 두 요청이 동일한 브라우저에서 들어왔는지 아닌지를 판단할 때 주로 사용된다.
    - 이를 이용해 사용자의 로그인 상태를 유지할 수 있다.
    - 상태가 없는 HTTP 프로토콜에서 상태 정보를 기억시켜 주는 역할을 한다.

  > 서버에게 로그인된 사용자라는 인증 정보가 담긴 쿠키를 매 요청마다 보내는 것이다.

  #### 쿠키 사용 목적
  1. 세션 관리
    - 로그인, 아이디 자동완성, 공지 하루 안 보기, 팝업 체크, 장바구니 등의 정보 관리
  2. 개인화
    - 사용자 선호 설정 저장
  3. 트래킹
    - 사용자 행동을 기록 및 분석

### 세션
서버 측에서 생성되어 클라이언트와 서버 간의 상태를 유지하고, **상태 정보를 저장**하는 데이터 저장 방식
> 요청마다 세션 데이터를 함께 보낸다.

  #### 세션 작동 원리
  1. 클라이언트가 로그인 요청 후에 인증에 성공하면 서버가 세션 데이터를 생성하고 저장한다.
  2. 생성된 세션 데이터에 인증 할 수 있는 id를 발급한다.
  3. 발급한 id를 클라이언트에게 응답한다.
  4. 클라이언트는 응답 받은 id를 쿠키에 저장한다.
  5. 클라이언트가 다시 동일한 서버에 접속하면 요청과 함께 쿠키를 서버에 전달한다.
  6. 쿠키에 요청 때마다 서버에 함께 전송되므로 서버에서 id를 확인해 로그인 되어있음을 계속해서 확인하도록 한다.
  
  > ---
  >
  > - 서버 측은 세션 데이터를 생성하고 저장한다.<br>이후 데이터에 접근할 수 있는 세션 ID를 생성한다.
  >
  > - ID는 클라이언트 측에 전달한다.
  >
  > - 클라이언트는 쿠키에 이 ID를 저장한다.
  >
  > - 재요청 시마다 저장해 둔 쿠키도 요청과 함께 전송한다.

  #### 쿠키와 세션의 목적
  1. 클라이언트와 서버 간의 상태 정보를 유지
  2. 사용자를 식별

### Django Authentication System
사용자 인증(신원확인)과 관련된 기능을 모아 놓은 시스템 : `너, 누구야!`

## Custom User Model


### Login
로그인은 세션을 Create하는 과정

- `AuthenticationFrom()` : 로그인 인증에 사용할 데이터를 입력 받는 built-in form

  #### Login view
  ```python
  # views.py
  # 앱의 create 로직과 거의 동일하다.

  from django.contrib.auth.forms import AuthenticationForm
  from django.contrib.auth import login as auth_login

  def login(request):
    if request.method == 'POST':
      form = AuthenticationForm(request, request.POST)
      # 인증된 사용자라면 로그인 진행(세션데이터 생성)
      if form.is_valid():
        auth_login(request, form.get_user())
        return redirect('articles:index')
    else:
      form = AuthenticationForm()
    context = {
      'form': form,
    }
    return render(request, 'accounts/login.html', context)
  ```

  - `login(request, user)` : AuthenticationForm을 통해 인증된 사용자를 로그인 하는 함수
  - `get_user()` : AuthenticationForm의 인스턴스 메서드
    > 유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환

### Logout
로그아웃은 세션을 Delete하는 과정

- `logout(request)` :
  1. DB에서 현재 요청에 대한 세션 데이터를 삭제
  2. 클라이언트의 쿠키에서도 세션 ID를 삭제
  
  #### Logout View
  ```python
  def logout(request):
    # 세션 데이터 삭제
    auth_logout(request)
    return redirect('articles:index')
  ```

## Template with Authentication data
템플릿에서 인증 관련 데이터를 출력하는 방법

> index.html은 context로 `user`를 받지 않았지만 사용할 수 있다.

### context processors
- 템플릿이 렌더링 될 때 호출 가능한 컨텍스트 데이터 목록
- 작성된 컨텍스트 데이터는 기본적으로 템플릿에서 사용 가능한 변수로 포함됨
  > django에서 사용자 편의를 위해 자주 사용하는 데이터 목록을 미리 템플릿에 로드 해두었다.

## 참고
### 쿠키의 수명
1. Session Cookie
   - 현재 세션이 종료되면 삭제된다.
   - 브라우저 종료와 함께 세션이 삭제된다.
2. Persistent Cookie
   - Expires 속성에 지정된 날짜 혹은 Max-Age 속성에 지정된 기간이 지나면 삭제된다.

### 쿠키의 보안
- 제한된 정보
  - 쿠키에는 보통 중요하지 않은 정보만 저장
  > 핵심 데이터는 서버가 암호화하여 가지고 있음
- 만료 시간
  - 쿠키에는 만료 시간을 설정 시간이 지나면 자동으로 삭제
- 도메인 제한
  - 쿠키는 특정 웹사이트에서만 사용할 수 있도록 설정할 수 있음

### 쿠키의 개인정보 보호
- 많은 국가에서 쿠키 사용에 대한 사용자 동의를 요구하는 법규를 시행 중이다.
- 웹사이트는 쿠키 정책을 명시하고, 필요한 경우 사용자의 동의를 얻어야 한다.

### Django의 세션 관리
- `database-backed sessions` : DB에 세션을 저장하는 방식
- 세션 정보는 DB의 `django_session` 테이블에 저장
- Django는 요청 안에 특정 세션 ID를 포함하는 쿠키를 사용해서 각각의 브라우저와 사이트가 연결된 세션 데이터를 알아냄

### AbstractUser class
관리자 권한과 함께 완전한 기능을 가지고 있는 User model을 구현하는 추상 기본 클래스

  #### 추상 기본 클래스
  - 몇 가지 공통 정보를 여러 다른 모델에 넣을 때 사용하는 클래스
  - DB 테이블을 만드는 데 사용되지 않으며, 대신 다른 모델의 기본 클래스로 사용되는 경우 해당 필드가 하위 클래스의 필드에 추가 됨
    > 따라서 migrations 시에 제외된다.

## 회원 가입
User 객체를 Create 하는 과정

- `UserCreationForm()` : 회원 가입 시 사용자 입력 데이터를 받는 built-in ModelForm
  > 사용자가 입력한 정보를 그대로 받아서 DB에 저장되어야 하기 때문에 ModelForm 사용

### 회원가입 코드



### 회원가입 에러
> 회원 가입에 사용하는 UserCreationForm은 커스텀 유저 모델이 아닌, 과거 Django **기본 유저 모델로 작성**된 클래스이므로 오류 발생
> - `accounts.User`가 아닌 `auth.User`로 되어있다!

> 따라서 클래스 Meta의 **모델을 재작성** 해주어야한다.

```python
# forms.py

class CustomUserCreationForm(UserCreationForm):
  class Meta(UserCreationForm.Meta):
    model = get_user_model()
```
- `get_user_model()` : 현재 프로젝트에서 **활성화된 사용자 모델**을 반환하는 함수


## 회원 탈퇴
User 객체를 Delete 하는 과정

- User객체는 request에 들어있다.


## 회원정보 수정
User 객체를 Update 하는 과정

- `UserChangeForm()` : 회원정보 수정 시 사용자 입력 데이터를 받는 built-in ModelForm


## 비밀번호 변경
인증된 사용자의 Session 데이터를 Update 하는 과정

- `PasswordChangeForm()` : 비밀번호 변경 시 사용자 입력 데이터를 받는 built-in Form


## 로그인 사용자에 대한 접근 제한
1. `is_authenticated` 속성
2. `login_required` 데코레이터

### is_authenticated 속성
사용자가 인증 되었는지 여부를 알 수 있는 User model의 속성
- 모든 **User 인스턴스**에 대해 항상 **True**인 읽기 전용 속성
- **비인증 사용자**에 대해서는 항상 **False**

### login_required 데코레이터
인증된 사용자에 대해서만 view 함수를 실행시키는 데코레이터
- **비인증 사용자**의 경우 `/accounts/login/` 주소로 redirect


## 참고