import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    msg: "나는 긴 변수를 쓰기 싫다.",
  },
  getters: {
    msgLen(state) {
      return state.msg.length
    },
    doubLen(state, getters) {
      return getters.msgLen * 2
    }
  },
  mutations: {
    CHANGE_MESSAGE(state, req) {
      state.msg = req
    },
  },
  actions: {
    cm (context, req) {
      // console.log(context)
      // console.log(req)
      context.commit('CHANGE_MESSAGE', req)
    },
  },
  modules: {

  }
})
