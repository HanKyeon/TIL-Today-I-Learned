import Vue from "vue"
import VueRouter from "vue-router"
import HomeView from "../views/HomeView.vue"
// import HelloView from "../views/HelloView.vue"
import LoginView from "../views/LoginView.vue"

Vue.use(VueRouter)
const a = true // 라우터 가드 때매
const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
  {
    path: "/hello/:userName?",
    name: "hello",
    component: () =>
      import(/* webpackChunkName: "hello" */ "../views/HelloView.vue"), // 레이지 로딩 방식.
    // component: HelloView,
  },
  {
    path: "/login",
    name: "login",
    // component: () => import(/* webpackChunkName: "login" */ "../views/LoginView.vue"), // 레이지 로딩 방식.
    component: LoginView,
    beforeEnter(to, from, next) {
      if (true == a) {
        console.log("이미 로그인 상태")
        next({ name: "home" })
      } else {
        next()
      }
    },
  },
  {
    path: "/404",
    name: "NotFound404",
    component: () =>
      import(/* webpackChunkName: "NotFound404" */ "../views/NotFound404.vue"), // 레이지 로딩 방식.
    // component: LoginView,
  },
  {
    path: "/dog/:breed?",
    name: "dog",
    component: () =>
      import(/* webpackChunkName: "dog" */ "../views/DogView.vue"), //
  },
  {
    path: "*",
    redirect: "/404",
  },
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
})

// // 전역 가드
// router.beforeEach(function (to, from, next) {
//   console.log(from)
//   const isLogedIn = true

//   const authPages = ["hello", "home", "about"]

//   const isAuthRequired = authPages.includes(to.name)
//   if (isAuthRequired && !isLogedIn) {
//     next({ name: "login" })
//   } else {
//     next()
//   }
// })

export default router
