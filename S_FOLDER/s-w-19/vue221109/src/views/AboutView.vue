<template>
  <div class="about">
    <h1>This is an about page</h1>
    <button @click="toHome">Go Home</button>
    <br />
    <input type="text" v-model="inputData" @keyup.enter="toHello" />
    <br />
    <router-link
      @click="toHello"
      :to="
        userName
          ? { name: 'hello', params: { userName: userName } }
          : { name: 'hello' }
      "
      >헬로!</router-link
    >
  </div>
</template>

<script>
export default {
  name: "aboutView",
  data() {
    return {
      inputData: "",
    }
  },
  methods: {
    toHome() {
      this.$router.push({ name: "home" })
    },
    toHello() {
      // this.$router.push({ name: "hello", params: { userName: this.inputData } })
      this.$emit("to-hello", this.inputData)
    },
  },
  computed: {
    userName() {
      return this.inputData
    },
  },
}
</script>
