<template>
  <div id="app">
    <h1>ㅎㅇ 세상</h1>
    <todo-list/>
    <todo-form/>
    <button @click="loadTodos">Todos 불러오기</button>
  </div>
</template>

<script>
import TodoForm from '@/components/TodoForm/TodoForm'
import TodoList from '@/components/TodoList/TodoList'

export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList
  },
  methods: {
    // 라이브러리 vuex-persistedStorage 안쓰고 로드하기
    // loadTodos() {
    //   this.$store.dispatch('loadTodos')
    // }
  },
  // 라이브러리 vuex-persistedStorage 안쓰고 로드하기
  // created() {
  //   this.$store.dispatch('loadTodos')
  // },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
