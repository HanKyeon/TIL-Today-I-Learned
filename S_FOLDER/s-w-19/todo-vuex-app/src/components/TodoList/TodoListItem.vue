<template>
  <li>
    <span
      @click="updateTodoStatus"
      :class="todo.isCompleted? ['is-completed', 'hello'] : ''"
      style="display: inline;"
    >
      {{ todo.title }}
    </span>
      <button
        @click="deleteTodo"
      >
        삭제
      </button>
  </li>
</template>

<script>
//:class="{'hi': true, 'hello': true}"
//:class="{['is-completed', 'hello'] : todo.isCompleted}"
export default {
  name: "TodoListItem",
  props: {
    todo: Object,
    idx:Number,
  },
  data() {
    return {
    }
  },
  methods: {
    deleteTodo(event) {
      event.preventDefault()
      this.$store.dispatch('deleteTodo', this.idx)
    },
    updateTodoStatus() {
      this.$store.dispatch('updateTodoStatus', this.idx)
    },
  },
}
</script>

<style>
.is-completed {
  text-decoration: line-through;
}
</style>