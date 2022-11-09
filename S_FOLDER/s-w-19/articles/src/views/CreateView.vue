<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
      <input type="text" v-model.trim="title" />
      <br />
      <textarea v-model="content"></textarea>
      <br />
      <input type="submit" />
    </form>
    <router-link :to="{ name: 'index' }">뒤로 가기</router-link>
  </div>
</template>

<script>
export default {
  name: "CreateView",
  data() {
    return {
      title: null,
      content: null,
    }
  },
  methods: {
    createArticle() {
      const payload = {
        title: this.title,
        content: this.content,
      }
      this.$store.dispatch("createArticle", payload)
      this.$router.push({ name: "index" })
    },
  },
}
</script>

<style></style>
