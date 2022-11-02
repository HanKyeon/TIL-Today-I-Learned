<template>
  <div>
    <h2>
      마이 컴포넌트 아이템
    </h2>
    <p>{{staticProps}}</p>
    <p>{{dynamicProps}}</p>
    <button @click="childToParent">
      클릭
    </button>
    <input 
      type="text" 
      v-model="childInputData"
      @keyup.enter="childInput"
    >
  </div>
</template>

<script>
export default {
  name: 'MyComponentItem',
  props: {
    staticProps: String,
    dynamicProps: String,
  },
  methods: {
    childToParent() {
      this.$emit('show-me-the-money', this.$data)
      this.childInputData=null
    },
    childInput() {
      this.$emit('child-input', this.$data)
      this.childInputData=null
    },
  },
  data() {
    return {
      childInputData: null,
      normallySend: "그냥 보냄",
    }
  }
}
</script>

<style>

</style>