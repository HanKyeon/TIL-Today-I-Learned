<template>
  <div>
    <h1>디테일</h1>
    <p>글 번호 : {{ article?.id }}</p>
    <p>제목 : {{ article?.title }}</p>
    <p>내용 : {{ article?.content }}</p>
    <p>작성 시간 : {{ createdAt }}</p>
    <router-link :to="{ name: 'index' }">뒤로 가기</router-link>
    <br />
    <button @click="deleteArticle">삭제하기</button>
  </div>
</template>

<script>
export default {
  name: "DetailView",
  data() {
    return {
      article: null,
    }
  },
  computed: {
    articles() {
      return this.$store.state.articles
    },
    createdAt() {
      const createdAt = new Date(this.article?.createdAt).toLocaleString()
      return createdAt
    },
  },
  methods: {
    getArticle(id) {
      // const id = this.$route.params.id
      for (const article of this.articles) {
        if (article.id === Number(id)) {
          this.article = article
          break
        }
      }
      if (!this.article) {
        this.$router.push({ name: "NotFound404" })
      }
    },
    deleteArticle(event) {
      event.preventDefault()
      this.$store.dispatch("deleteArticle", this.article.id)
      this.$router.push({ name: "index" })
    },
  },
  created() {
    this.getArticle(this.$route.params.id)
  },
}
</script>

<style></style>
