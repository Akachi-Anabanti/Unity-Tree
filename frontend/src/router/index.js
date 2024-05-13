import { useAlertStore } from '@/stores/alert';
import { useAuthStore } from '@/stores/auth';
import { createRouter, createWebHistory} from 'vue-router'
import accountRoute from './account';
import HomeView from '@/views/main/HomeView.vue';


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  linkActiveClass:'active',
  routes: [
    {
      path: '',
      name: 'home',
      component: ()=> import('@/views/main/MainView.vue'),
      children:[
        {
          path:"",
          name:"main",
          component: HomeView
        },
        {
          path:"/tree/:familyId",
          name:"tree",
          component: () => import("@/views/main/TreeView.vue"),
          props:true
        },
        {
          path: "/profile/:userId",
          name: "profile",
          redirect: "view",
          children:[
            {
              path:"/view",
              name: "view",
              component: () =>  import("@/views/main/profile/UserProfileView.vue"),
              props:true
            },
            {
              path:"/edit",
              name:"edit",
              component: () => import("@/views/main/profile/UserProfileEditView.vue"),
              props:true
            }
          ],
          props:true
        }
      ]
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
    
      authStore.setReturnUrl(to.fullPath)
      return '/account/login';
  }
})


export default router
