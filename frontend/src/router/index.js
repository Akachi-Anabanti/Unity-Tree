import { createRouter, createMemoryHistory} from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createMemoryHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/profile',
      name: 'profile',
      component : () => import('../views/UserView.vue')
    },
    {
      path: '/landing',
      name: 'landing',
      component: () => import ('../views/landingView.vue')
    }
  ]
})

export default router
