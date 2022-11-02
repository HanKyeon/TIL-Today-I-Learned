<template>
  <div>
    Todo List
    <ul v-for="todoitem, idx in todosList" :key="`list-${idx}`">
      <TodoListItem
        :todo-item="todoitem"
        @item-shouting="goToApp"
      />
    </ul>
  </div>
</template>

<script>
import TodoListItem from '@/components/Todo/TodoListItem'

export default {
  name:'TodoList',
  components:{
    TodoListItem,
  },
  data() {
    return {
      
    }
  },
  props: {
    todosList: Array,
  },
  methods: {
    goToApp(wannaDelete) {
      this.$emit('delete-plz', wannaDelete)
    }
  }
}
</script>

<style>

</style>