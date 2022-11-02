<template>
  <li>
    {{todoItem.content}}
    <button @click="goToList">삭제 버튼</button>
  </li>
</template>

<script>
export default {
  name:'TodoListItem',
  data() {
    return {
      
    }
  },
  props: {
    todoItem: Object,
  },
  methods: {
    goToList() {
      this.$emit('item-shouting', this.todoItem)
    }
  }
}
</script>

<style>

</style>