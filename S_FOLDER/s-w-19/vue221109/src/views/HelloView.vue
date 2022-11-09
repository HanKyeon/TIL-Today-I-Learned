<template>
  <div>
    <h1>Hello, {{ userName }}</h1>
    <!-- <h1>ㅎ {{ this.$router }}</h1> -->
  </div>
</template>

<script>
export default {
  name: "HelloView",
  data() {
    return {
      userName: this.$route.params?.userName,
    }
  },
  created() {
    this.userName = this.$route.params?.userName
  },
  beforeRouteUpdate(to, from, next) {
    this.userName = to.params.userName
    next()
  },
}
</script>
