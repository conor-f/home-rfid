import { createRouter, createWebHistory } from 'vue-router'

import Cards from '../views/Cards.vue'

const routes = [
  {
    path: '/',
    name: 'DefaultCards',
    component: Cards
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
