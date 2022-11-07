import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    todos: [],
  },
  getters: {
    todoLength(state) {
      return state.todos.length
    },
    completedTodos(state) {
      return state.todos.filter((val) => {
        return val.isCompleted
      }).length
    },
    unCompletedTodos(state, getters) {
      return getters.todoLength - getters.completedTodos
    }
  },
  mutations: {
    ADD_TODO(state, obj) {
      state.todos.push(obj)
    },
    DELETE_TODO(state, arr) {
      state.todos = arr
      // arr 대신 todoItem 자체를 받아서 지워줄 수도 있다.
      // const idx = state.todos.indexOf(todoItem)
      // state.todos.splice(index, 1)
    },
    UPDATE_TODO(state, item) {
      // state.todos[idx].isCompleted = !state.todos[idx].isCompleted
      item.isCompleted = !item.isCompleted
    },
    // 라이브러리 vuex-persistedStorage 안쓰고 로드하기
    // LOAD_TODOS(state) {
    //   const localTodos = localStorage.getItem('todos')
    //   const parsedTodos = JSON.parse(localTodos)
    //   state.todos = parsedTodos
    //   state.todos = JSON.parse(localStorage.getItem('todos'))
    // }
  },
  actions: {
    addTodo(context, todoTitle) {
      const todoItem = {
        title: todoTitle,
        isCompleted: false
      }
      context.commit('ADD_TODO', todoItem)
      // context.dispatch('saveTodosToLocalStorage')
    },
    deleteTodo(context, idx) {
      let req = context.state.todos.filter((val, i) => {
        if (i === idx) {return false} else {return true}
      })
      context.commit('DELETE_TODO', req)
      // context.dispatch('saveTodosToLocalStorage')
    },
    updateTodoStatus(context, idx) {
      let reqItem = context.state.todos[idx]
      context.commit('UPDATE_TODO', reqItem)
      // context.dispatch('saveTodosToLocalStorage')
    },
    // 라이브러리 vuex-persistedStorage 안쓰고 세이브/로드하기
    
    // saveTodosToLocalStorage(context) {
    //   const jsonTodos = JSON.stringify(context.state.todos)
    //   localStorage.setItem('todos', jsonTodos) // 키 이름으로 가져올 것이다.
    // },
    // loadTodos(context) {
    //   context.commit('LOAD_TODOS')
    // }
  },
  modules: {
  }
})
