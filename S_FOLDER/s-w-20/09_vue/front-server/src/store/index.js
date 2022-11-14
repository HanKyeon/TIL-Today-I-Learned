import Vue from "vue"
import Vuex from "vuex"
import axios from "axios"
import createPersistedState from "vuex-persistedstate"
import router from "../router"

const API_URL = "http://127.0.0.1:8000"

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    articles: [],
    token: null,
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    },
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles = articles
    },
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: "ArticleView" })
    },
  },
  actions: {
    getArticles(context) {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/articles/`,
        headers: { Authorization: `Token ${context.state.token}` },
      })
        .then((res) => {
          context.commit("GET_ARTICLES", res.data)
        })
        .catch((err) => {
          console.error(err)
        })
    },
    signUp(context, payload) {
      axios({
        method: "post",
        url: `${API_URL}/accounts/signup/`,
        data: {
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
        },
      })
        .then((res) => {
          context.commit("SAVE_TOKEN", res.data.key)
        })
        .catch((err) => {
          console.error(err)
        })
    },
    logIn(context, payload) {
      axios({
        method: "post",
        url: `${API_URL}/accounts/login/`,
        data: {
          username: payload.username,
          password: payload.password,
        },
      }).then((res) => {
        context.commit("SAVE_TOKEN", res.data.key)
      })
    },
  },
  modules: {},
})
