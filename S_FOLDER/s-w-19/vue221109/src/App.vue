<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'home' }">Home</router-link> |
      <router-link :to="{ name: 'about' }">About</router-link>
      |
      <router-link
        :to="
          userName
            ? { name: 'hello', params: { userName: userName } }
            : { name: 'hello' }
        "
        >Hello</router-link
      >
      |
      <router-link :to="{ name: 'login' }">Login</router-link>|
      <router-link :to="{ name: 'dog', params: { breed: 'husky' } }"
        >Dog</router-link
      >
    </nav>
    <router-view @to-hello="toHello" />
  </div>
</template>

<script>
//:to="{ name: 'hello', params: { userName: userName } }"
//@to-hello="toHello"
export default {
  name: "app",
  data() {
    return {
      userName: "",
    }
  },
  methods: {
    toHello(req) {
      this.userName = req
      console.log(req)
      this.$router.push({ name: "hello", params: { userName: req } })
    },
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
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
