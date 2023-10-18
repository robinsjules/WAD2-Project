<template>
  <div>
    <router-link :to="{ name: 'Register' }">Register</router-link> |
    <router-link :to="{ name: 'Home' }">Home</router-link> |
    <router-link :to="{ name: 'Profile' }">Profile</router-link> |
    <router-link :to="{ name: 'Login' }">Login</router-link>
  </div>

  <p>
  <button @click="$router.go(-1)">Go back 1 step</button>
  <button @click="$router.go(1)" >Go forward 1 step</button>
  </p>

  <router-view/>
</template>