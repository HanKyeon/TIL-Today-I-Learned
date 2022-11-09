import Vue from "vue"
import Vuex from "vuex"

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    articleId: 3,
    articles: [
      {
        id: 1,
        title: "First Article",
        content: "First Article Content",
        createdAt: new Date().getTime(),
      },
      {
        id: 2,
        title: "Second Article",
        content: "Second Article Content",
        createdAt: new Date().getTime(),
      },
    ],
  },
  getters: {},
  mutations: {
    CREATE_ARTICLE(state, article) {
      state.articles.push(article)
      state.articleId += 1
    },
    DELETE_ARTICLE(state, id) {
      state.articles = state.articles.filter((val) => {
        return val.id !== id
      })
    },
  },
  actions: {
    createArticle(context, payload) {
      const article = {
        id: context.state.articleId,
        title: payload.title,
        content: payload.content,
        createdAt: new Date().getTime(),
      }
      context.commit("CREATE_ARTICLE", article)
    },
    deleteArticle(context, id) {
      context.commit("DELETE_ARTICLE", id)
    },
  },
  modules: {},
})
