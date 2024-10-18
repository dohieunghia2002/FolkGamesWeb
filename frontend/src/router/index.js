import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Recognition from '../views/Recognition.vue'
import Detail from '../views/Detail.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/recognition',
      name: 'recognition',
      component: Recognition
    },
    {
      path: '/detail/:id',
      name: 'detail',
      component: Detail
    }
  ]
})

export default router
