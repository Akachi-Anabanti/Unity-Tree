// import { useAlertStore } from '@/stores/alert';
import { useAuthStore } from '@/stores/auth'
import { createRouter, createWebHistory } from 'vue-router'
import accountRoute from './account'
import HomeView from '@/views/main/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  linkActiveClass: 'active',
  routes: [
    {
      path: '',
      name: 'home',
      component: () => import('@/views/main/MainView.vue'),
      children: [
        {
          path: '',
          name: 'main',
          component: HomeView
        },
        {
          path: '/tree/:familyId',
          name: 'tree',
          component: () => import('@/views/main/TreeView.vue'),
          props: true
        },
        {
          path: '/family',
          name: 'family',
          component: () => import('@/views/main/family/familyViewLayout.vue'),
          children: [
            {
              path: 'create',
              name: 'create-family',
              component: () => import('@/views/main/family/createFamilyView.vue')
            },
            {
              path: 'view/:familyId',
              name: 'view-family',
              component: () => import('@/views/main/family/familyProfileView.vue'),
              props: true
            },
            {
              path: 'edit/:familyId',
              name: 'edit-family',
              component: () => import('@/views/main/family/editFamilyProfileView.vue'),
              props: true
            }
          ]
        },
        {
          path: '/profile',
          name: 'profile',
          component: () => import('@/views/main/profile/ProfileViewLayout.vue'),
          children: [
            {
              path: 'view/:_Id',
              name: 'view',
              component: () => import('@/views/main/profile/UserProfileView.vue'),
              props: true
            },
            {
              path: 'edit/:_Id',
              name: 'edit',
              component: () => import('@/views/main/profile/UserProfileEditView.vue'),
              props: true
            }
          ]
        },
        {
          path: '/discover',
          name: 'discover',
          component: () => import('@/views/main/ExploreView.vue')
        }
      ]
    },
    // Accounts route set up
    { ...accountRoute },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    { path: '/:pathMatch(.*)*', redirect: '/' }
  ]
})
router.beforeEach((to, from, next) => {
  // Store the user's last route path
  localStorage.setItem('lastRoute', to.fullPath)
  next()
})

router.beforeEach(async (to) => {
  //clear alerts on route change
  // useAlertStore().$reset()

  const publicPages = ['/account/login', '/account/register', '/about']
  const authRequired = !publicPages.includes(to.path)

  const authStore = useAuthStore()
  if (authRequired && !authStore.isAuthenticated) {
    authStore.setReturnUrl(to.fullPath)
    return '/account/login'
  }
  // If the user is authenticated and there's a last route in the localStorage,
  // navigate to it instead
  // const lastRoute = localStorage.getItem('lastRoute');
  // if (authStore.isAuthenticated && lastRoute) {
  //   next(lastRoute);
  // } else {
  //   next();
  // }
})

export default router
