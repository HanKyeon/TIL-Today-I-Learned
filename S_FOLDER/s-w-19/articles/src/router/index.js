import Vue from "vue"
import VueRouter from "vue-router"
import IndexView from "../views/IndexView.vue"

Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    name: "index",
    component: IndexView,
  },
  {
    path: "/create",
    name: "create",
    component: () =>
      import(/* webpackChunkName: "create" */ "../views/CreateView.vue"),
  },
  {
    path: "/404-not-found",
    name: "NotFound404",
    component: () =>
      import(/* webpackChunkName: "404" */ "../views/NotFound404"),
  },
  {
    path: "/:id",
    name: "detail",
    component: () =>
      import(/* webpackChunkName: "detail" */ "../views/DetailView.vue"),
  },
  {
    path: "*",
    redirect: "/404-not-found",
  },
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
})

export default router
