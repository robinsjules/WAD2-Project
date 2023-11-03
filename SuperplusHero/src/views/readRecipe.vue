<template>
    <div class="content">
      <div class="container-fluid mt-3">
        <!-- Recipe Prep: Start -->
        <h2>Your Selected Recipe</h2>
        <div v-if="recipe" class="mt-4 p-4 bg-light text-black rounded">
          <div class="row">
            <div class="col-md-4">
              <div>
                <img :src="recipe.image" style="width: 30vw; height: auto; border-radius: 5%;" :alt="recipe.title">
              </div>
            </div>
            <div class="col-md-8">
              <h2>{{ recipe.title }} Preparation</h2>
              <ol>
                <li v-for="step in recipe.analyzedInstructions[0]?.steps" :key="step.number">{{ step.step }}</li>
              </ol>
              <div style="text-align: right;">
                <button class="btn btn-success">Start Cooking</button>
              </div>
            </div>
          </div>
        </div>
        <!-- Recipe Prep: End -->
  
        <h1>Required Ingredients (Serving Size: 4)</h1>
        <div v-if="recipe" class="row">
          <!-- Green Box -->
          <div class="col-md-6">
            <div class="mt-4 p-4 text-black rounded" style="background-color: rgb(226, 246, 244);">
              <h2>Available Ingredients:</h2>
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat..
              </p>
              <ul class="list-unstyled">
                <li class="fw-bold">Laksa Spice Base Paste</li>
                <li v-for="ingredient in recipe.ingredients" :key="ingredient.id">{{ ingredient.name }}</li>
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
  import recipeData from '../../../backend/spoonacular/americanCuisine.json'
  
  export default {
    data() {
      return {
        searchQuery: "",
        selectedCuisine: "",
        recipes: recipeData,
        recipe: null, // Initialize recipe as null
      };
    },
    methods: {
      // Update recipe when a recipe is selected
      selectRecipe(recipe) {
        this.recipe = recipe;
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
  