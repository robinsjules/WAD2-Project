<template>
    <div>
      <h1>Data from JSON</h1>
      <div v-for="recipe in recipes.results" :key="recipe.id" class="recipe-card">
        <!-- Recipe Image -->
        <img :src="recipe.image" class="recipe-image" :alt="recipe.title" />
  
        <!-- Recipe Details (Title, Instructions, and Ingredients) -->
        <div class="recipe-details">
          <h2>{{ recipe.title }}</h2>
          <h3>Instructions:</h3>
          <ol>
            <li v-for="step in recipe.analyzedInstructions[0]?.steps" :key="step.number">
              {{ step.step }}
            </li>
          </ol>
        </div>
  
        <!-- Ingredients -->
        <div class="recipe-ingredients">
          <h3>Ingredients:</h3>
          <ul>
            <li v-for="step in recipe.analyzedInstructions[0]?.steps" :key="step.number">
              <ul>
                <li v-for="ingredient in step.ingredients" :key="ingredient.id">
                  {{ ingredient.name }}
                </li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import recipeData from '../../../backend/spoonacular/americanCuisine.json'
  
  export default {
    data() {
      return {
        recipes: recipeData,
      };
    },
  };
  </script>
  
  <style scoped>
  .recipe-card {
    display: flex;
    margin: 20px;
    border: 1px solid #ccc;
    padding: 10px;
  }
  
  .recipe-image {
    max-width: 200px;
    max-height: 200px;
    object-fit: cover;
    margin-right: 20px;
  }
  
  .recipe-details {
    flex: 1;
  }
  
  .recipe-ingredients {
    flex: 1;
  }
  </style>
  