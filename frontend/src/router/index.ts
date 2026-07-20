import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'login',
      component: () => import('../app/views/LoginView.vue'),
    },
    {
      path: '/admin-dashboard',
      name: 'admin-dashboard',
      component: () => import('../app/views/AdminDashboardView.vue'),
    },
    {
      path: '/employee-dashboard',
      name: 'employee-dashboard',
      component: () => import('../app/views/EmployeeDashboardView.vue'),
    }
  ],
})

export default router
