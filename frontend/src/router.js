import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const MainPageMain = () => import('components/MainPageMain')

const routes = [
  {
    path: '/',
    redirect: '/home'
  },
  {
    path:'/home',
    component: MainPageMain
  }
]

export default new Router({
  mode: 'history',
  routes: routes
})
