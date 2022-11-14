<template>
  <div>
    <h5>{{ article.id }}</h5>
    <p>{{ article.title }}</p>
    <p>작성자 : {{ article.username }}</p>
    <router-link
      :to="{
        name: 'DetailView',
        params: { id: article.id },
      }"
      >[DETAIL]</router-link
    >
    <hr />
  </div>
</template>

<script>
export default {
  name: "ArticleListItem",
  props: {
    article: Object,
  },
}
</script>

<style></style>
