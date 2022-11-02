<template>
  <div class="border">
    <h1>내가 만든 컴포넌트다! 실시간으로 바뀌는</h1>
    <MyComponentItem
      static-props="123"
      :dynamic-props="dynamicProps"
      @show-me-the-money="pge"
      @child-input="pge"
    />
  </div>
</template>

<script>
import MyComponentItem from '@/components/MyComponents/MyComponentItem'
// import MyComponentItem from '@/Mycomponents/MyComponentItem'

export default {
  name: 'MyComponent',
  components: {
    MyComponentItem,
  },
  data: function () {
    return {
      dynamicProps: '쿠쿠루삥뽕',
    }
  },
  methods: {
    pge(param) {
      console.log("My Component", param.childInputData)
      console.log("My Component", param.normallySend)
      let a = {
        a:"gg dynamic data"
        }
      this.$emit('my-component-shout-out', a)
    }
  }
}
</script>

<style>
  .border {
    border: solid 1px black;
  }
</style>