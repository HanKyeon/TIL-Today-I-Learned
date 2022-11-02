<template>
  <div id="app">
    <TodoList
      :todos-list="todos"
      @delete-plz="okdk"
    />
    <TodoForm
      @save-request="createTodo"
    />
  </div>
</template>

<script>
import TodoForm from '@/components/Todo/TodoForm'
import TodoList from '@/components/Todo/TodoList'

export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList,
  },
  data() {
    return {
      todos: []
    }
  },
  methods: {
    createTodo(inputData) {
      this.todos.push(inputData)
    },
    okdk(itemData) {
      let a = this.todos.indexOf(itemData) // 삭제 할 아이템 인덱스 찾고
      this.todos.splice(a, 1) // 삭제한걸 새로 반환한다.
    }
  }
}
</script>

<style>
/* #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
} */
</style>
