# Django와 Ajax
## Ajax with follow
### 절차
1. form 요소에 Event Handler 할당
2. submit 이벤트의 기본 동작 취소
3. axios 초기 작성
   ```javascript
   formTag.addEventListener('submit', function (event) {
    event.preventDefault()
    axios({
      method: 'post',
      url: `/accounts/${}/follow/`
    })
   })
   ```
4. user pk 가져오기
   ```html
   <form ... data-user-id="{{ person.pk }}">
    ...
   </form>
   ```
   ```javascript
   formTag.addEventListener('submit', function (event) {
    ...
    const userId = event.currentTarget.dataset.userId
    // const userId = this.dataset.userId
    // const userId = formTag.dataset.userId

    axios({
      method: 'post',
      url: `/accounts/${userId}/follow/`
    })
   })
   ```
   - `data-*` 속성
     - 사용자 지정 데이터 특성을 만들어 **임의의 데이터를 HTML과 DOM 사이에서 교환** 할 수 있는 방법
     - JavaScript에서 `dataset` 속성을 통해 접근
     > 주의사항 :
     > 1. 'xml'문자로 시작 불가
     > 2. 세미콜론 포함 불가
     > 3. 대문자 포함 불가
5. csrf 토큰 전송 파트 작성
   ```javascript
   const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

   formTag.addEventListener('submit', function (event) {
    ...

    axios({
      ...
      headers: {'X-CSRFToken': csrftoken,},
    })
   })
   ```
6. 현재 상태 JavaScript에 전달
   ```python
   # views.py

   from django.http import JsonResponse

   @login_required
   def follow(request, user_pk):
    ...
    if person != request.user:
      if person.followers.filter(pk=request.user.pk).exists():
        person.followers.remove(request.user)
        is_follow = False
      else:
        person.followers.add(request.user)
        is_follow = True
      context = {
        'is_follow': is_follow,
      }
      # 응답을 HTML이 아닌 JSON 데이터로 응답하도록 변경
      return JsonResponse(context)
    ...
   ```
   > 이후 JavaScript에서 `console.log(response.data)`를 통해 정상적으로 전송되었는지 확인하는 것이 좋다.
7. 응답 데이터에 따라 팔로우 버튼 조작
   ```javascript
   ...
   axios({
    ...
   }).then((response) => {
    const isFollow = response.data.is_follow
    const followBtn = document.querySelector('input[type=submit]')
    if (isFollow === true) {
      followBtn.value = 'Unfollow'
    } else {
      followBtn.value = 'Follow'
    }
   })
   ```
8. 웹페이지 개발자도구에서 수발신 확인
   > 개발자도구 - Network 창에서 'xhr' 객체 확인
9. 팔로우 & 팔로워 수 연동
    - 요소 선택을 위한 span 태그와 id 속성 추가
    - `views.py`에서 계산한 값을 context에 포함하여 JavaScript에 전송
    - 응답 데이터를 받아 각 태그에 `textContent`를 이용하여 값 변경

## Ajax with likes
팔로우 기능과 유사하나, 좋아요는 한 페이지에 여러 개가 존재할 수 있다는 차이가 존재한다.
- 버블링을 활용한다.
  > 전체 버튼을 감싸는 조상 Tag를 만들어, 해당 Tag에 Event Listener를 할당한다!

### 절차
1. 최상위 요소 선택
2. 이벤트 핸들러 할당
3. submit 기본 이벤트 취소
4. 좋아요 form에 article.pk 부여
   ```html
   <form data-article-id="{{ article.pk }}">
    ...
   </form>
5. article.pk 값을 JavaScript에서 참조
   ```javascript
   articleContainer.addEventListener('submit', function (event) {
    ...
    // articleContainer 안에 하나의 좋아요 폼에 대해서만 작동해야 하므로
    // 이벤트 핸들러가 연결된 요소를 참조하는 속성인 currentTarget가 아닌
    // 이벤트가 발생한 가장 안쪽 요소를 참조하는 target 속성을 입력한다.
    const articleId = event.target.dataset.articleId
    axios({
      ...
      url: `/articles/${articleId}/likes/`
      ...
    }).then(...)
      .catch(...)
   })
6. 좋아요 상태 여부를 JavaScript에 전달할 데이터 작성 및 JSON 데이터 응답
   ```python
   # views.py
   from django.http import JsonResponse

   ...
   def likes(request, article_pk):
    ...
    if request.user in article.like_users.all():
      article.like_users.remove(request.user)
      is_liked = False
    else:
      article.like_users.add(request.user)
      is_liked = True
    context = {
      # 팔로우처럼 임의의 확인 변수를 만들어 JavaScript에 전달한다.
      'is_liked': is_liked,
    }
    return JsonResponse(context)
   ```
   ```html
   <!-- axios의 then 콜백 함수가 실행되는 과정에서 어떤 게시글의 좋아요 버튼이 선택되었는지 구분이 필요하다 -->
   <!-- 따라서 각 input에 개별 id를 적용한다. -->
   <input type="submit" id="like-{{ article.pk }}">
   ```
   ```javascript
   ...
   axios({
    ...
   }).then((response) => {
    const isLiked = response.data.is_liked
    const likeBtn = document.querySelector(`#like-${articleId}`)
    if (isLiked === true) {
      likeBtn.value = '좋아요 취소'
      likeBtn.value = '좋아요'
    }
   })
   ```

