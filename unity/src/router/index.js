import { createWebHistory, createRouter } from 'vue-router'

import AboutViewVue from '@/views/AboutView.vue'
import HomeViewVue from '@/views/HomeView.vue'

const routes = [
  { path: '/about', component: AboutViewVue },
  { path: '/home', component: HomeViewVue }
]
const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
