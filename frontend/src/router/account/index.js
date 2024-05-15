import Login from '@/views/account/LoginView.vue'
import Register from '@/views/account/RegisterView.vue'
import Layout from '@/views/account/AccountLayout.vue'

export default {
  path: '/account',
  component: Layout,
  children: [
    { path: '', redirect: 'login' },
    { path: 'login', component: Login },
    { path: 'register', component: Register }
  ]
}
