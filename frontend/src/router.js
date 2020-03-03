import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

const MainPageMain = () => import('components/MainPageMain')
const ComputerStructure = () => import('components/ComputerStructure')

const routes = [{
    path: '/',
    redirect: '/home'
  },
  {
    path: '/home',
    component: MainPageMain
  },
  {
    path: '/course',
    component: ComputerStructure
  }
]

export default new Router({
  mode: 'history',
  routes: routes
})