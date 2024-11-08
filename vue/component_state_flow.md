# Component State Flow
## Passing Props
### Props
> 공통된 부모 컴포넌트에서 관리하자!
- 부모 컴포넌트로부터 자식 컴포넌트로 데이터를 전달하는데 사용되는 속성
  > `passing props` : 부모가 자식에게 데이터를 전달, 자식이 부모에게 일어난 일 알림

#### 특징
- 부모 속성이 업데이트되면 자식으로 전달
  > 반대는 불가 : 부모에서만 변경 가능
- 부모 컴포넌트가 업데이트 될 때마다 이를 사용하는 자식 컴포넌트의 모든 props가 최신 값으로 업데이트

#### One-Way Data Flow
- 모든 props는 자식 속성과 부모 속성 사이에 **하향식 단방향 바인딩**을 형성

- 단방향의 이유
  - 하위 컴포넌트가 실수로 상위 컴포넌트의 상태를 변경하여 앱에서의 데이터 흐름을 이해하기 어렵게 만드는 것을 방지하기 위함
  > **일관성**과 **단순화**

### Props 선언
- 부모 컴포넌트에서 내려보낸 props를 사용하기 위해서는 자식 컴포넌트에서 명시적인 props 선언이 필요

### Props 작성
- 부모 컴포넌트 Parent에서 자식 컴포넌트 ParentChild에 보낼 Props 작성
  ```vue
  <template>
    <div>
      <ParentChild my-msg="message" />
      <!-- 'my-msg' : props 이름 -->
      <!-- 'message' : props 값 -->
    </div>
  </template>
  ```
- `defineProps()`를 사용하여 props를 선언
  - 인자의 데이터 타입에 따라 선언 방식이 나뉨
  ```vue
  <script setup>
  defineProps()
  </script>

#### Props 선언 2가지 방식
1. *문자열 배열*을 사용한 선언
   - 배열의 문자열 요소로 props 선언
   - 문자열 요소의 이름은 전달된 props의 이름
     ```vue
     <!-- ParentChild.vue -->
     <script setup>
     defineProps(['myMsg'])
     </script>

2. *객체*를 사용한 선언
   - 각 객체 속성의 키가 전달받은 Props의 이름이 되며, 객체 속성의 값은 값이 될 데이터 타입에 해당하는 생성자 함수(Number, String...)여야 함
     ```vue
     <!-- ParentChild.vue -->
     <script setup>
     defineProps({
      myMsg: String
     })
     </script>

#### Props 데이터 사용
- Props 선언 후 템플릿에서 반응형 변수와 같은 방식으로 활용
  ```vue
  <!-- ParentChild.vue -->
  <div>
    <p>{{ myMsg }}</p>
  </div>
  ```

- Props를 객체로 반환하므로 필요한 경우 JavaScript에서 접근 가능
  ```vue
  <script setup>
  const props = defineProps({ myMsg: String })
  console.log(props) // {myMsg: 'message'}
  console.log(props.myMsg) // 'message'
  </script>
  ```

#### 깊은 자식으로 보내기
- parentChild 컴포넌트에서 Parent로부터 받은 Props인 myMsg를 ParentGrandChild에게 전달
  ```vue
  <template>
    <div>
      <p>{{ myMsg }}</p>
      <ParentGrandChild :my-msg="myMsg" />
      <!-- v-bind를 사용하여 동적 props를 전달한다 -->
    </div>
  </template>
  ```

### Props 세부사항
- Props Name Casing
  - 자식 컴포넌트로 전달 할 때는 `kebab-case` 사용
  - 선언 및 템플릿 참조 시 `camelCase`
- Static Props와 Dynamic Props
  - v-bind를 사용하지 않으면 정적(Static) props
  - v-bind를 사용하면 **동적 할당 props** 사용 가능
  - 과정
    - 동적 props 정의
    ```vue
    <!-- Parent.vue -->
    <template>
      <ParentChild my-msg="message" :dynamic-props="name" />
    </template>

    <script>
    import { ref } from 'vue'

    const name = ref('Alice')
    </script>
    ```
    - 동적 props 선언 및 출력
    ```vue
    <!-- ParentChild.vue -->

    <template>
      <p>{{ dynamicProps }}</p>
    </template>

    <script setup>
    defineProps({
      myMsg: String,
      dynamicProps: String,
    })
    </script>
    ```

### Props 활용
- `v-for`와 함께 사용하여 반복되는 요소 props로 전달
  ```vue
  <script setup>
  const items = ref([
    {id: 1, name: '사과'},
    {id: 2, name: '바나나'},
    {id: 3, name: '딸기'}
  ])
  </script>
  ```
  ```vue
  <template>
    <ParentItem
      v-for="item in items"
      :key="item.id"
      :my-prop="item"
    />
  </template>
  ```

## Component Events
### Emit
- 자식 컴포넌트가 이벤트를 발생시켜 부모 컴포넌트로 데이터를 전달하는 역할의 메서드
  > '$' 표기는 Vue 인스턴스 내부 변수들을 가리킴
  >
  > Lifecycle Hooks, 인스턴스 메서드 등 내부 특정 속성에 접근할 때 사용

#### emit 메서드 구조
`$emit(event, ...args)`
- event : 커스텀 이벤트 이름
- args : 추가 인자

### 이벤트 발신 및 수신
- `$emit`을 사용하여 템플릿 표현식에서 직접 사용자 정의 이벤트를 발신
  ```vue
  <button @click="$emit('someEvent')">클릭</button>
  ```
- 부모는 v-on을 사용하여 수신 가능
  ```vue
  <!-- template -->
  <ParentComp @some-event="someCallback" />
  ```
  ```vue
  <!-- script setup -->
  <script setup>
  const someCallback = function () {
    console.log('이벤트 수신')
  }
  </script>
  ```

### emit 이벤트 선언
- `defineEmits()`를 사용하여 발신할 이벤트를 선언
- props와 마찬가지로 `defineEmits()`에 작성하는 인자의 데이터 타입에 따라 선언 방식이 나뉨
- `defineEmits()`는 `$emit` 대신 사용할 수 있는 동등한 함수를 반환

#### 선언 활용
```vue
<!-- ParentChild.vue -->

<template>
  <button @click="buttonClick">클릭</button>
</template>

<script setup>
const emit = defineEmits(['someEvent'])

const buttonClick = function () {
  emit('someEvent')
}
</script>
```

### 이벤트 전달
- 이벤트 발신 시 추가 인자를 전달하여 값 제공 가능
- 추가 인자 전달
  ```vue
  <!-- ParentChild.vue -->
  <!-- 이벤트 발신 -->

  <template>
    <button @click="emitArgs">추가 인자 전달</button>
  </template>

  <script setup>
  const emit = defineEmits(['someEvent', 'emitArgs'])

  ...
  const emitArgs = function () {
    emit('emitArgs', 1, 2, 3)
  }
  </script>
  ```

  ```vue
  <!-- Parent.vue -->
  <!-- 이벤트 수신 -->

  <template>
    <ParentChild
      @some-event="someCallback"
      @emit-args="getNumbers"
      my-msg="message"
      :dynamic-props="name"
    />
  </template>

  <script setup>
  ...
  const getNumbers = function (...args) {
    console.log(args)
    console.log(`${args} 수신 완료`)
  }
  </script>
  ```

### 이벤트 세부사항
- 선언 및 발신 시는 `camelCase`

- 부모 컴포넌트에서 수신 시 `kebab-case`

### emit 이벤트 활용
> 손자 컴포넌트에서 조부 컴포넌트로 요청하기
- 손자 컴포넌트에서 이름 변경 요청 이벤트 발신
  > 한 번에 점프는 불가하다.
  ```vue
  <!-- ParentGrandChild.vue -->

  <template>
    <button @click="updateName">이름 변경</button>
  </template>

  <script setup>
  const emit = defineEmits(['updateName'])

  const updateName = function () {
    emit('updateName')
  }
  </script>
  ```

- 이벤트 수신 후 이름 변경 요청 이벤트 발신
  ```vue
  <!-- ParentChild -->

  <template>
    <ParentGrandChild :my-msg="myMsg" @update-name="updateName" />
  </template>

  <script setup>
  const emit = defineEmits(['updateName'])

  const updateName = function () {
    emit('updateName')
  }
  </script>
  ```

- 조부 컴포넌트에서 이벤트 수신 후 변수 변경 메서드 호출
- props를 받는 모든 곳에서 자동 업데이트
  ```vue
  <!-- Parent -->

  <template>
    <ParentChild @update-name="updateName" />
  </template>

  <script setup>
  const updateName = function () {
    name.value = 'Bella'
  }
  </script>
  ```

## 참고
### 정적 & 동적 props 주의사항
- 정적 props로 문자열 '1' 전달
  - `<SomeComponent num-props="1" />`
- 두번째 동적 props로 숫자 1 전달
  - `<SomeComponent :num-props="1" />`

### Props & Emit 객체 선언 문법
#### 권장 이유
- 컴포넌트를 가독성이 좋게 문서화하는데 도움
- 협업자가 잘못된 유형을 전달할 때 콘솔에 경고 출력

> props와 emit에 대한 **유효성 검사**로서 활용 가능
