<template>
    <div class="content">
      <div class="container-fluid mt-3">
        <!-- Recipe List: Start -->
        <h2>All Recipes</h2>
        <div class="row">
          <div v-for="recipe in recipes.results" :key="recipe.id" class="col-md-4">
            <div class="card m-2 pt-2" style="width: 18rem">
              <img :src="recipe.image" class="card-img-top" :alt="recipe.title">
              <div class="card-body">
                <h5 class="card-title">{{ recipe.title }}</h5>
                <p class="card-text">{{ recipe.description }}</p>
                <button @click="selectRecipe(recipe)" class="btn btn-outline-success">Read more</button>
              </div>
            </div>
          </div>
        </div>
        <!-- Recipe List: End -->
  
        <!-- Recipe Details: Start -->
        <div v-if="selectedRecipe" class="mt-4 p-4 bg-light text-black rounded">
          <div class="row">
            <div class="col-md-4">
              <div>
                <img :src="selectedRecipe.image" style="width: 30vw; height: auto; border-radius: 5%;" :alt="selectedRecipe.title">
              </div>
            </div>
            <div class="col-md-8">
              <h2>{{ selectedRecipe.title }} Preparation</h2>
              <ol>
                <li v-for="step in selectedRecipe.analyzedInstructions[0]?.steps" :key="step.number">{{ step.step }}</li>
              </ol>
              <div style="text-align: right;">
                <button class="btn btn-success">Start Cooking</button>
              </div>
            </div>
          </div>
        </div>
        <!-- Recipe Details: End -->
  
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
  import recipeData from '../../../backend/spoonacular/allCuisine.json'
  
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

  console.log(recipeData)
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
  