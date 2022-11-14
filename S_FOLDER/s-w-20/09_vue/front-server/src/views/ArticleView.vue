<template>
  <div>
    <h1>Article Page</h1>
    <router-link :to="{ name: 'CreateView' }">[CREATE]</router-link>
    <hr />
    <article-list />
  </div>
</template>

<script>
import ArticleList from "@/components/ArticleList.vue"
export default {
  name: "ArticleView",
  components: {
    ArticleList,
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    },
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      if (this.isLogin) {
        this.$store.dispatch("getArticles")
      } else {
        alert("로그인 필수")
        this.$router.push({ name: "LogInView" })
      }
    },
  },
}
</script>

<style></style>
