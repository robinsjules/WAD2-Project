import { createRouter, createWebHistory } from 'vue-router'

import Home from '@/views/Home.vue'
import Login from '@/views/Login.vue'
import Profile from '@/views/Profile.vue'
import Register from '@/views/Register.vue'
import AllRecipes from '@/views/AllRecipes.vue'
import AllIngridients from '@/views/AllIngridients.vue'
import Products from '@/views/Products.vue'
import UserRecipes from '@/views/UserRecipes.vue'
import Register2 from '@/views/Register2.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/profile',
      name: 'Profile',
      component: Profile
    },
    {
      path: '/register',
      name: 'Register',
      component: Register
    },
    {
      path: '/allrecipes',
      name: 'AllRecipes',
      component: AllRecipes
    },
    {
      path: '/allingridients',
      name: 'AllIngridients',
      component: AllIngridients
    },
    {
      path: '/products',
      name: 'products',
      component: Products
    },
    {
      path: '/user/recipes', // once backend is clearer, make the user a variable/key
      name: 'UserRecipes',
      component: UserRecipes
    },
    {
      path: '/register2',
      name: 'Register2',
      component: Register2
    }
  ]
})

export default router