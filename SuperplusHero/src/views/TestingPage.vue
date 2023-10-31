<style scoped>
.content{
    margin-top: 100px;
}
</style>
<template>
  <div class="content">
    <h2>Edit Profile</h2>
    <form @submit.prevent="updateProfile">
      <label for="Email">Email:</label>
      <input type="text" id="Email" v-model="email" />

      <label for="UserName">Username:</label>
      <input type="text" id="UserName" v-model="userName" />

      <label for="Password">Password:</label>
      <input type="password" id="Password" v-model="password" />

      <label for="PostalCode">Postal Code:</label>
      <input type="text" id="PostalCode" v-model="postalCode" />

      <label for="Halal">Halal:</label>
      <input type="checkbox" id="Halal" v-model="halal" />

      <label for="Fridge">Fridge:</label>
      <textarea id="Fridge" v-model="fridge"></textarea>

      <label for="Savings">Savings:</label>
      <input type="number" id="Savings" v-model="savings" />

      <label for="RecipesPosted">Recipes Posted:</label>
      <input type="number" id="RecipesPosted" v-model="recipesPosted" />

      <button type="submit">Save</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '', // Initialize with user's current email
      userName: '', // Initialize with user's current username
      password: '', // Initialize with user's current password
      postalCode: '', // Initialize with user's current postal code
      halal: false, // Initialize with user's current halal status
      fridge: '', // Initialize with user's current fridge content (as JSON string)
      savings: 0, // Initialize with user's current savings
      recipesPosted: 0 // Initialize with user's current number of recipes posted
    };
  },
  methods: {
    updateProfile() {
      // Construct the updated user data
      const updatedData = {
        userName: this.userName,
        password: this.password,
        postalCode: this.postalCode,
        halal: this.halal,
        fridge: JSON.parse(this.fridge), // Assuming you want to store the fridge data as JSON
        savings: this.savings,
        recipesPosted: this.recipesPosted
        // Add other fields to be updated
      };
      
      // Make an HTTP PUT request to update the profile data
      axios.put(`http://127.0.0.1:5000/update_profile/${this.userName}`, updatedData)
        .then(response => {
          console.log(response.data); // Handle success response
        })
        .catch(error => {
          console.error('Error updating data:', error); // Handle error
        });
    }
  }
};
</script>
