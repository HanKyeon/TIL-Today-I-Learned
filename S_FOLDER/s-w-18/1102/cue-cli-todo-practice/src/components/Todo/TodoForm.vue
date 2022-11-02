<template>
  <div>
    입력창
    <input
      type="text"
      v-model="inputData"
      @keyup.enter="saveContent"
    >
    <button @click="saveContent">저장 허/실?</button>
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data() {
    return {
      inputData: null,
    }
  },
  methods: {
    saveContent() {
      this.$emit('save-request', {content: this.inputData, isCompleted: false,})
      this.inputData = null
    },
  }
}
</script>

<style>

</style>