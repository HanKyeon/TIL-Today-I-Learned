<template>
  <div>
    <h2>투두리스트</h2>
    All Todos: {{allTodos}}<br>
    Completed Todo: {{completedTodos}}<br>
    Uncompleted Todo: {{unCompletedTodos}}<br>
    <todo-list-item
      v-for="todo, idx in todos"
      :key="`todo-${idx}`"
      :todo="todo"
      :idx="idx"
    />
  </div>
</template>

<script>
import TodoListItem from '@/components/TodoList/TodoListItem'
export default {
  name: "TodoList",
  components: {
    TodoListItem,
  },
  computed: {
    todos() {
      return this.$store.state.todos
    },
    allTodos() {
      return this.$store.getters.todoLength
    },
      completedTodos() {
        return this.$store.getters.completedTodos
      },
    unCompletedTodos() {
      return this.$store.getters.unCompletedTodos
    },
  },
  props: {
    
  },
}
</script>

<style>

</style>