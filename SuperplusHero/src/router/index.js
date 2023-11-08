import { createRouter, createWebHistory } from 'vue-router'

import TestingPage from '@/views/TestingPage.vue'
import Home from '@/views/Home.vue'
import Profile from '@/views/Profile.vue'
import Register from '@/views/Register.vue'
import AllRecipes from '@/views/AllRecipes.vue'
import AllRecipes2 from '@/views/AllRecipes2.vue'
import readRecipe from '@/views/readRecipe.vue'
import AllIngredients from '@/views/AllIngredients.vue'
import Products from '@/views/Products.vue'
import UserRecipes from '@/views/UserRecipes.vue'
import Community from '@/views/Community.vue'
import ben_test2 from '@/views/ben_test2.vue'
import Fridge from '@/views/Fridge.vue'
import Checkout from "@/views/Checkout.vue"
import { retrieveSession } from "@/router/retrievesession";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/testing',
      name: TestingPage,
      component: TestingPage
    },
    {
      path: '/home',
      name: 'Home',
      component: Home
    },
    {
      path: '/profile',
      name: 'Profile',
      component: Profile
    },
    {
      path: '/',
      name: 'Register',
      component: Register
    },
    {
      path: '/allrecipes',
      name: 'AllRecipes',
      component: AllRecipes
    },
    {
      path: '/allrecipes2',
      name: 'AllRecipes2',
      component: AllRecipes2
    },
    {
      path: '/readrecipe/:id',
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
      path: '/user/recipes',
      name: 'UserRecipes',
      component: UserRecipes
    },
    {
      path: '/community',
      name: 'Community',
      component: Community
    },
    {
      path: '/fridge',
      name: 'Fridge',
      component: Fridge
    },
    {
      path: '/checkout',
      name: "Checkout",
      component: Checkout
    },
  ]
})

router.beforeEach(async (to, from, next) => {
  const requiresAuth = to.matched.some(record => record.meta.requiresAuth);
  if (requiresAuth) {
    try {
      const userSession = await retrieveSession();
      if (!userSession) {
        next('/login'); // Redirect to login if not authenticated
      } else {
        next('/home');
      }
    } catch (error) {
      console.error('Error retrieving session:', error);
      next('/login'); // Redirect to login on error
    }
  } else {
    next(); // Continue for routes that don't require authentication
  }
});

export default router

