<template>
    <div>
      <h1>User List</h1>
      <ul>
        <li v-for="user in users" :key="user.email">{{ user.User_FName }}</li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        users: [],
      };
    },
    mounted() {
      // Make an HTTP GET request to your Flask API
      axios.get('http://127.0.0.1:5000/users') // Adjust the URL if needed
        .then((response) => {
          this.users = response.data;
          console.log(this.users);
        })
        .catch((error) => {
          console.error('Error fetching data:', error);
        });
    },
  };
  </script>
  