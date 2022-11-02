<template>
  <div class="border">
    <h1>내가 만든 컴포넌트다! 실시간으로 바뀌는</h1>
    <MyComponentItem/>
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
}
</script>

<style>
  .border {
    border: solid 1px black;
  }
</style>