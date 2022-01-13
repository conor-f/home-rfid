import { createRouter, createWebHistory } from 'vue-router'

import Cards from '../views/Cards.vue'
import Actions from '../views/Actions.vue'

const routes = [
  {
    path: '/',
    name: 'DefaultCards',
    component: Cards
  },
  {
    path: '/cards',
    name: 'Cards',
    component: Cards
  },
  {
    path: '/actions',
    name: 'Actions',
    component: Actions
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
