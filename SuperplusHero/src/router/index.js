import { createRouter, createWebHistory } from 'vue-router'

import TestingPage from '@/views/TestingPage.vue'
import Home from '@/views/Home.vue'
import Login from '@/views/Login.vue'
import Profile from '@/views/Profile.vue'
import Register from '@/views/Register.vue'
import AllRecipes from '@/views/AllRecipes.vue'
import readRecipe from '@/views/readRecipe.vue'
import AllIngredients from '@/views/AllIngredients.vue'
import Products from '@/views/Products.vue'
import UserRecipes from '@/views/UserRecipes.vue'
import Register2 from '@/views/Register2.vue'
import Community from '@/views/Community.vue'
import ben_test2 from '@/views/ben_test2.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/testing',
      name: TestingPage,
      component: TestingPage
    },
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
      path: '/readrecipe',
      name: 'readRecipe',
      component: readRecipe
    },
    {
      path: '/AllIngredients',
      name: 'AllIngredients',
      component: AllIngredients
    },
    {
      path: '/ben_test2',
      name: 'ben_test2',
      component: ben_test2
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
    },
    {
      path: '/community',
      name: 'Community',
      component: Community
    }
  ]
})

export default router

