<template>
  <div>
    <router-link :to="{ name: 'Register' }">Register</router-link> |
    <router-link :to="{ name: 'Login' }">LogIn</router-link> |
    <router-link :to="{ name: 'Home' }">Home</router-link> |
    <router-link :to="{ name: 'Profile' }">Profile</router-link>
  </div>
  <router-view/>
</template>