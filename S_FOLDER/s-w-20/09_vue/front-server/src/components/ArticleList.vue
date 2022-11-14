<template>
  <div class="article-list">
    <h3>Article List</h3>
    <article-list-item
      v-for="(article, idx) in articles"
      :key="`article-${idx}`"
      :article="article"
    />
  </div>
</template>

<script>
import ArticleListItem from "@/components/ArticleListItem.vue"

export default {
  name: "ArticleList",
  components: {
    ArticleListItem,
  },
  computed: {
    articles() {
      return this.$store.state.articles
    },
  },
}
</script>

<style>
.article-list {
  text-align: start;
}
</style>
