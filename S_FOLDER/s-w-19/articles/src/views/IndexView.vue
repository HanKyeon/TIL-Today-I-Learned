<template>
  <div>
    <h1>인덱스</h1>
    <router-link :to="{ name: 'create' }">글 쓰기</router-link>
    <article-item
      v-for="(article, idx) in articles"
      :key="`article-${idx}`"
      :article="article"
      :idx="idx"
    ></article-item>
  </div>
</template>

<script>
import ArticleItem from "@/components/ArticleItem"

export default {
  name: "IndexView",
  components: {
    ArticleItem,
  },
  computed: {
    articles() {
      return this.$store.state.articles
    },
  },
}
</script>

<style></style>
