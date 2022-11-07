<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- <HelloWorld msg="Welcome to Your Vue.js App"/> -->
    <h1>{{ msg }}</h1>
    <input
      type="text"
      @keyup.enter="cm"
      v-model="t"
    >
    <h2>입력된 문자의 길이는 {{msgLen}}</h2>
    <h3>길이 두배는 {{dLen}}</h3>
  </div>
</template>

<script>
// import axios from 'axios'
// import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  data() {
    return {
      t:null,
    }
  },
  components: {
    // HelloWorld
  },
  computed: {
    msg() {return this.$store.state.msg},
    msgLen() {
      return this.$store.getters.msgLen
    },
    dLen() {
      return this.$store.getters.doubLen
    }
  },
  methods: {
    cm() {
      const txtInput = this.t
      // this.$store.dispatch("cm", txtInput)
      this.$store.commit("CHANGE_MESSAGE", txtInput)
      this.t = null
    }
  },
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
