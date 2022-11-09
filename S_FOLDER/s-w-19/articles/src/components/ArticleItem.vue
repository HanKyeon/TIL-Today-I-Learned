<template>
  <div @click="goDetail(article.id)">
    <h3>아이템</h3>
    <p>{{ article.id }}</p>
    <p>{{ article.title }}</p>
    <p>{{ article.content }}</p>
    <hr />
  </div>
</template>

<script>
export default {
  name: "ArticleItem",
  props: {
    article: Object,
  },
  methods: {
    goDetail(id) {
      this.$router.push({ name: "detail", params: { id: id } })
    },
  },
}
</script>

<style></style>
