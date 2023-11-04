<template>
    <div class="content">
      <div class="container-fluid mt-3">
        <h1>Required Ingredients (Serving Size: 4)</h1>
      <div v-if="selectedRecipe" class="row">
        <!-- Green Box -->
        <div class="col-md-6">
          <div class="mt-4 p-4 text-black rounded" style="background-color: rgb(226, 246, 244);">
            <h2>Available Ingredients:</h2>
            <p>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat..
            </p>
            <ul class="list-unstyled">
              <li class="fw-bold">Laksa Spice Base Paste</li>
              <li v-for="ingredient in selectedRecipe.ingredients" :key="ingredient.id">{{ ingredient.name }}</li>
            </ul>
          </div>
        </div>
        <!-- Green Box -->

        <!-- Red Box -->
        <div class="col-md-6">
          <div class="mt-4 p-4 text-black rounded" style="background-color: rgb(246, 226, 226);">
            <h2>Missing Ingredients:</h2>
            <p>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat..
            </p>
            <!-- List missing ingredients here -->
          </div>
        </div>
        <!-- Red Box -->
      </div>
        </div>
    </div>
  </template>
  
<script>
import axios from 'axios'
import recipeData from '../../../backend/spoonacular/americanCuisine.json'

export default {
  data() {
    return {
      searchQuery: "",
      selectedCuisine: "",
      recipes: recipeData,
      selectedRecipe: null, // Initialize selectedRecipe as null
    };
  },
  methods: {
    // Select a recipe
    selectRecipe(recipe) {
      this.selectedRecipe = recipe;
    },
  },
};
</script>

<style scoped>
.content {
  margin-top: 100px;
}

.list-unstyled {
  list-style: none;
  padding: 0;
}



</style>

  