import { useAlertStore } from '@/stores/alert';
import { useAuthStore } from '@/stores/auth';
import { createRouter, createWebHistory} from 'vue-router'
import accountRoute from './account';


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  linkActiveClass:'active',
  routes: [
    {
      path: '/',
      name: 'home',
      component: ()=> import('../views/HomeView.vue')
    },
    // Accounts route set up
    { ...accountRoute},
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
    {path : '/:pathMatch(.*)*', redirect:'/'}

  ]
});

router.beforeEach(async(to) => {
  //clear alerts on route change
  useAlertStore().$reset

  const publicPages =['/account/login', '/account/register', '/about']
  const authRequired = !publicPages.includes(to.path);

  const authStore = useAuthStore();

  if (authRequired && !authStore.isAuthenticated) {
      authStore.returnUrl = to.fullPath;
      return '/account/login';
  }
})


export default router
