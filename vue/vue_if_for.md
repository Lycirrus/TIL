# Vue Basic Syntax
## Computed Property
### Computed
- "계산된 속성"을 정의하는 함수
  > 미리 계산된 속성을 사용하여 템플릿에서 표현식을 단순하게 하고 불필요한 반복 연산을 줄임

#### 분석
- 기존
  ```javascript
  const todos = ref([
    { text: 'Vue 실습' },
    { text: '자격증 공부' },
    { text: 'TIL 작성' }
  ])
  // html
  <p>{{ todos.length > 0 ? '할 일 남음' : '종료' }}</p>
  ```
  - 계산이 템플릿에 여러 번 사용하는 경우 반복이 발생
- Computed
  ```javascript
  const { createApp, ref, computed } = Vue

  const restOfTodos = computed(() => {
    return todos.value.length > 0 ? '할 일 남음' : '종료'
  })

  // html
  <p?>{{ restOfTodos }}</p>
  // Todos가 변경될 때만 restOfTodos 업데이트
  ```
  - 반응형 데이터를 포함하는 복잡한 로직의 경우 computed를 활용하여 미리 값을 계산하여 사용

#### 특징
- 반환되는 값은 computed ref이며 일반 refs와 유사하게 계산된 결과를 `.value`로 참조 가능
- computed 속성은 의존된 반응형 데이터를 **자동으로 추적**
- 의존하는 데이터가 **변경될 때만 재평가**

### Computed vs. Methods
- 공통점
  - method로도 computed의 기능을 동일하게 정의 가능
- 차이점
  - computed 속성은 **의존된 반응형 데이터를 기반으로 캐시(*cached*)**
  - 의존하는 데이터가 변경된 경우에만 재평가
  - method 호출은 다시 렌더링이 발생할 때마다 항상 함수 실행

#### Cache
- 데이터나 결과를 일시적으로 저장해두는 임시 저장소
- 같은 데이터나 결과를 계산하지 않고 빠르게 접근하도록 함 

#### computed와 method의 적절한 사용처
- computed
  - 의존하는 데이터에 따라 결과가 바뀌는 계산된 속성을 만들 때 유용
  - 동일한 의존성을 가진 여러 곳에서 사용할 때 계산 결과를 캐싱하여 중복 계산 방지
  - **의존된 데이터가 변경되면 자동으로 업데이트**
- method
  - 단순히 특정 동작을 수행하는 함수를 정의할 때 사용
  - 데이터와 관계없이 항상 동일한 결과를 반환하는 함수
  - **호출 시에만 실행**

## Conditional Rendering
### v-if
- 표현식 값의 tf를 기반으로 요소를 조건부로 렌더링
  ```javascript
  // script
  const isSeen = ref(true)

  // html
  // v-if로 조건문 만듦
  // v-else로 else 블록을 나타낼 수 있다.
  // v-else-if로 else if 블록을 나타낼 수 있다.
  <p v-if="isSeen">true일 경우 표시</p>
  <p v-else>false일 경우 표시</p>
  // <p v-else-if="조건문">...</p>
  ```

#### 여러 요소에 대해 v-if 적용
- HTML template 요소에 v-if를 사용하여 하나 이상의 요소에 대해 적용 가능
  ```javascript
  <template v-if="name === 'Cathy'">
    <div>Cathy</div>
    <div>age : 30</div>
  </template>
  ```

#### <template> element
- 페이지가 **로드 될 때 렌더링 되지 않**지만, JavaScript를 사용하여 **나중에 문서에서 사용**할 수 있도록 하는 HTML을 보유하기 위한 메커니즘

### v-if vs. v-show
- `v-show` : 표현식 값의 tf를 기반으로 요소의 가시성을 전환
  - 항상 DOM에 렌더링 되어있음
  - CSS display 속성만 전환
  ```javascript
  const is Show = ref(false)

  // html
  <div v-show="isShow">v-show</div>
  // ==> <div style="display: none;">v-show</div>
  ```

#### v-if와 v-show의 적절한 사용처
- `v-if`
  - 초기 조건이 false인 경우 아무 작업도 실행하지 않음
  - 토글 비용이 높음
- `v-show`
  - 초기 조건에 관계 없이 항상 렌더링
  - 초기 렌더링 비용이 더 높음

> 콘텐츠를 매우 자주 전환해야 하는 경우에는 v-show
>
> 실행 중에 조건이 변경되지 않는 경우네는 v-if

## List Rendering
### v-for
- 소스 데이터를 기반으로 요소 또는 템플릿 블록을 여러 번 렌더링
  - v-for는 `alias in expression` 형식의 특수 구문 사용
    ```html
    <div v-for="item in items">
      {{ item.text }}
    </div>
    ```
  - 인덱스에 대한 별칭 지정 가능
    ```html
    <div v-for="(item, index) in arr"></div>

    <div v-for="(value, key, index) in object"></div>
    ```
  - 중첩 for문 사용 가능
    ```html
    <ul v-for="item in myInfo">
      <li v-for="friend in item.friends">
        ...
      </li>
    </ul>
    ```

#### 여러 요소에 대한 v-for 적용
- `v-if`와 마찬가지로 HTML template 요소에 `v-for`를 사용하여 적용
  ```html
  <ul>
    <template v-for="item in myArr">
      <li>{{ item.name }}</li>
      <li>{{ item.age }}</li>
      <hr>
    </template>
  </ul>
  ```

### v-for with key
- 반드시 `v-for`와 `key`를 함께 사용
  > 내부 컴포넌트의 상태를 일관 되게 하여 데이터의 예측 가능한 행동을 유지하기 위해서이다.

- key는 반드시 각 요소에 대한 **고유한 값을 나타낼 수 있는 식별자**여야 함
  ```html
  <div v-for="item in items" :key="item.id">
    ...
  </div>
  ```

#### 내장 특수 속성 `key`
- number 혹은 string으로만 사용
- Vue 내부 가상 DOM 알고리즘이 이전 목록과 새 노드 목록을 비교할 때 각 node를 식별하는 용도로 사용

### v-for with v-if
- 동일 요소에 `v-for`와 `v-if`를 **함께 사용하지 않는다**
  - 동일한 요소에서 `v-if`가 `v-for`보다 우선순위가 더 높음
  > `v-if`의 조건은 `v-for` 범위의 변수에 접근할 수 없다.

#### 해결방법
1. computed 활용
   - 이미 필터링 된 목록을 반환하여 반복
   ```javascript
   const completeTodos = computed(() => {
    return todos.value.filter((todo) => !todo.isComplete)
   })
   ```
   ```html
   <ul>
     <li v-for="todo in completeTodos" :key="todo.id">
       ...
     </li>
   </ul>
   ```

2. v-for와 template 요소를 사용
   ```html
   <ul>
     <template v-for="todo in todos" :key="todo.id">
       <li v-if="!todo.isComplete">
         ...
       </li>
     </template>
   </ul>
   ```

## Watchers
### watch
- `watch()` : 하나 이상의 반응형 데이터를 감시하고, 감시하는 데이터가 변경되는 콜백 함수를 호출

#### 구조
```javascript
watch(source, (newValue, oldValue) => {
  ...
})
```
- 첫번째 인자 : `source`
  - watch가 감시하는 대상 (*반응형 변수, 값을 반환하는 함수 등*)
- 두번째 인자 : `callback function`
  - source가 변경될 때 호출되는 콜백 함수
    - newValue : 감시하는 대상이 변화된 값
    - oldValue : 감시하는 대상의 기존 값

- 배열을 활용하여 여러 대상 감시 가능
  ```javascript
  watch([foo, bar], ([newFoo, newBar], [prevFoo, prevBar]) => {
    ...
  })
  ```

### computed vs. watch

||**Computed**|**Watchers**|
|:-:|:-------:|:----------:|
|동작|의존하는 데이터 속성의 계산된 값을 반환|특정 데이터 속성의 변화를 감시하고 작업을 수행|
|사용 목적|계산된 값을 캐싱하여 **중복 계산 방지**|데이터 변화에 따른 **특정 작업 수행**|
|사용 예시|연산 된 길이, 필터링 된 목록 계산 등|DOM 변경, 다른 비동기 작업 수행, 외부 API와 연동 등|

> 공통점 : 데이터의 변화를 감지하고 처리

> Computed와 Watch 모두 감시하는 원본 데이터를 직접 변경하지 않는다.

## Lifecycle Hooks
Vue 컴포넌트의 생성부터 소멸까지 각 단계에서 실행되는 함수

### 활용 예시
1. Mounting
   - Vue 컴포넌트 인스턴스가 **초기 렌더링 및 DOM 요소 생성이 완료된 후** 특정 로직 수행
     ```javascript
     const { createApp, ref, onMounted } = Vue

     const app = createApp({
      setup() {
        onMounted(() => {
          console.log('mounted')
        })
      }
     })
     ```
2. Updating
   - 반응형 데이터의 변경으로 인해 컴포넌트의 **DOM이 업데이트된 후** 특정 로직 수행
     ```javascript
     const { createApp, ref, onMounted, onUpdated } = Vue 

     onUpdated(() => {
       message.value = 'update'
     })
     ```

## Vue Style Guide
Vue 스타일 가이드 규칙의 우선순위 4 범주
1. 우선순위 A : 필수 (Essential)
   - 오류를 방지하는데 도움이 되므로 어떤 경우에도 규칙을 학습하고 준수
2. 우선순위 B : 적극 권장 (Strongly Recommended)
   - 가독성 및 개발자 경험 향상
   - 정당한 사유가 있을 때만 규칙 위반 가능
3. 우선순위 C : 권장 (Recommended)
   - 일관성을 보장하도록 임의의 선택을 할 수 있음
4. 우선순위 D : 주의 필요 (Use with Caution)
   - 잠재적 위험 특성 고려

#### 우선순위 A와 v-if, v-for
1. v-for에 key 작성하기
2. 동일 요소에 v-if와 v-for 함께 사용 금지

## 참고
### Computed 주의 사항
1. Computed의 반환 값은 변경하지 말 것
   - Computed의 반환 값은 의존하는 데이터의 파생 값
   - 계산된 값은 읽기 전용으로 취급하여야 함
   - 의존 데이터를 업데이트하는 쪽으로 변경
2. Computed 사용 시 원본 배열 변경하지 말 것
   - `reverse()`나 `sort()` 사용 시 원본 배열 변경됨
   - 원본 배열의 복사본을 만들어 진행
     ```javascript
     // 원본 배열을 변경하지 않기
     // 금지 예시
     return numbers.reverse()

     // 옳은 예시
     return [...numbers].reverse()
     ```

### Lifecycle Hooks 주의사항
**Lifecycle Hooks는 동기적으로 작성**

1. 컴포넌트 상태의 일관성 유지
   - 컴포넌트의 생명주기 동안 상태가 예측 가능하고 일관되게 유지되도록 보장
   - 비동기적으로 실행될 경우, 컴포넌트의 상태가 예상치 못한 시점에 변경될 수 있어 버그 발생 가능성이 높아짐

2. Vue 내부 메커니즘과의 동기화
   - Vue 내부 로직은 컴포넌트의 Lifecycle에 맞추어 최적화되어 있음
   - 동기적 실행을 통해 Vue 내부 프로세스와 개발자가 작성한 코드가 정확히 동기화

### 배열과 v-for
1. 변화 메서드
   - 호출하는 원본 배열을 변경
   - `push()`, `pop()`, `shift()`, `unshift()`, `splice()`, `sort()`, `reverse()`

2. 배열 교체
   - 원본 배열을 수정하지 않고 항상 새 배열을 반환
   - `filter()`, `concat()`, `slice()`

**※배열의 인덱스를 v-for의 key로 사용하지 말 것※**
- 인덱스는 식별자가 아닌 배열의 항목 위치만 나타냄
- 새 요소가 삽입되거나 요소가 삭제되었을 경우 인덱스 번호의 변경이 발생
  > key로서의 역할 수행 불가
