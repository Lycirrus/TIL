# State Management
#### 컴포넌트 구조
- 상태 (State)
  - 앱 구동에 필요한 기본 데이터
- 뷰 (View)
  - 상태를 선언적으로 매핑하여 시각화
- 기능 (Actions)
  - 뷰에서 사용자 입력에 대해 반응적으로 상태를 변경할 수 있게 정의된 동작
> 단방향 데이터 흐름의 간단한 표현

#### 단순성 붕괴 시점
- 여러 컴포넌트가 상태를 공유할 때
  1. 여러 뷰가 동일한 상태에 종속되는 경우
    - props의 깊이로 인한 문제점
  2. 서로 다른 뷰의 기능이 동일한 상태를 변경시켜야 하는 경우
    - emit된 이벤트들의 변경 및 동기화로 인한 문제점

#### 해결 방법
- 각 컴포넌트의 공유 상태를 추출하여, 전역에서 참조할 수 있는 저장소에서 관리
  > Vue의 공식 상태 관리 라이브러리 => "Pinia"

## State management library
### Pinia
- Vue 공식 상태 관리 라이브러리

### Pinia 구조
- store
  - 중앙 저장소
  - `defineStore()` 사용
  - defineStore()의 반환 값의 이름은 use와 store를 사용하는 것을 권장
  - 첫번째 인자는 애플리케이션 전체에 걸쳐 사용하는 store의 고유 ID
- state
  - 반응형 상태 (데이터)
  - `ref() === state`
- getters
  - 계산된 값
  - `computed() === getters`
- actions
  - 메서드
  - `function() === actions`
- plugin
  - 애플리케이션의 상태 관리에 필요한 추가 기능을 제공하거나 확장하는 도구나 모듈
  - 애플리케이션의 상태 관리를 더욱 간편하고 유연하게 만들어주며 패키지 매니저로 설치 이후 별도 설정을 통해 추가

> Pinia의 상태들을 사용하려면 반드시 반환해야 한다!

### Pinia 구성 요소 활용
- State
  - 각 컴포넌트 깊이에 관계 없이 인스턴스로 state에 접근
  - 직접 읽고 쓸 수 있음
  - state가 정의되지 않으면 컴포넌트에서 새로 추가할 수 없음
- Getters
  - 직접 접근 가능
- Actions
  - 직접 접근 및 호출 가능
  - getters와 달리 state 조작, 비동기, API 호출이나 다른 로직 수행 가능


## Pinia 실습
### Read
- store에 임시 todos 목록 state 정의
```javascript
export const useCounterStore = defineStore('counter', () => {
  let id = 0
  const todos = ref([
    { id: id++, text: '할 일 1', isDone: false },
    { id: id++, text: '할 일 2', isDone: false }
  ])
  return { todos }
})
```
- store의 todos state를 참조
```javascript
import { useCounterStore } from '@/stores/counter'

const store = useCounterStore()
```
- 하위 컴포넌트인 TodoListItem을 반복하면서 개별 todo를 props로 전달
```vue
<div>
  <TodoListItem 
    v-for="todo in store.todos"
    :key="todo.id"
    :todo="todo"
  />
</div>
```
- TodoListItem에서 props 정의
```vue
<template>
  <div>
    {{ todo.text }}
  </div>
</template>

<script setup>
defineProps({
  todo: Object
})
</script>
```

### Create
- todos 목록에 todo를 생성 및 추가하는 addTodo 액션 정의
```javascript
// useCounterStore 내부
const addTodo = function (todoText) {
  todos.value.push({
    id: id++,
    text: todoText,
    isDone: false
  })
}

return { 
  todos,
  addTodo
}
```
- TodoForm에서 데이터를 양방향 바인딩하여 반응형 변수로 할당
- submit 이벤트 발생 시, 사용자 입력 텍스트를 인자로 전달하여 addTodo 메서드 호출
```vue
<template>
  <div>
    <form @submit.prevent="createTodo(todoText)" ref="formErase">
      <!-- fromErase는 input 초기화 용도 -->
      <input type="text" v-model="todoText">
      <input type="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useCounterStore } from '@/stores/counter'

const todoText = ref('')
const formErase = ref(null)
const store = useCounterStore()

const createTodo = function (todoText) {
  store.addTodo(todoText)
  formErase.value.reset() // input 초기화
}
</script>
```

### Delete
- todo 목록에서 특정 todo를 삭제하는 deleteTodo 액션 정의
```javascript
const deleteTodo = function (todoId) {
  const index = todos.value.findIndex((todo) => todo.id === todoId)
  todos.value.splice(index, 1)
}

return { 
  todos,
  addTodo,
  deleteTodo
}
```
- 각 todo에 삭제버튼 추가 후 클릭 이벤트 설정
```vue
<template>
  <div>
    <span>{{ todo.text }}</span>
    <button @click="store.deleteTodo(todo.id)">Del</button>
  </div>
</template>
```

### Update
- todo의 isDone 속성을 변경하는 액션 메서드 작성
```javascript
const updateTodo = function (todoId) {
  todos.value = todos.value.map((todo) => {
    if (todo.id === todoId) {
      todo.isDone = !todo.isDone
    }
    return todo
  })
}

return { 
  todos,
  addTodo,
  deleteTodo,
  updateTodo
}
```

### Counting
- 완료한 todos 배열의 깅이 값을 반환하는 함수 countingTodo 작성
- computed 방식인 getters 사용
```javascript
const countingTodo = computed(() => {
  const doneTodos = Todos.value.filter((todo) => todo.isDone)
  return doneTodos.length
})
```
- TodoList에 출력
```vue
<div>
  <p>완료 : {{ store.countingTodo }}개</p>
  <TodoListItem 
    v-for="todo in store.todos"
    :key="todo.id"
    :todo="todo"
  />
</div>
```

### Local Storage
- 브라우저 내에 key-value 쌍을 저장하는 웹 스토리지 객체
  - 페이지 새로 고침 시 데이터가 유지
  - 네트워크 요청 시 서버로 전송되지 않음
  - 여러 탭이나 창 간에 데이터 공유 가능

#### pinia-plugin-persistedstate
- state를 브라우저의 local storage나 session storage에 영구적으로 저장하고 복원하는 기능 제공

#### 설치
- npm 설치
`npm i pinia-plugin-persistedstate`

- 등록
```javascript
// main.js

import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)

app.use(pinia)
```
- store에 추가
  - `defineStore()`의 세번째 인자로 추가
