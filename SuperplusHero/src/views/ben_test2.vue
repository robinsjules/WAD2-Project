<template>
  <!-- Recipe Cards -->
  <section>
          <div class="container-fluid">
            <div class="row justify-content-center">
              <div v-for="recipe in filteredRecipes" :key="recipe.id" class="card m-2" style="width: 18rem;">
                <div class="card-image">
                  <img :src="recipe.image" class="card-img-top" :alt="recipe.title">
                </div>
                <div class="card-body">
                  <h5 class="card-title">{{ recipe.title }}</h5>
                  <p class="card-text">{{ recipe.description }}</p>
                </div>
                <div class="card-footer">
                  <button type="button" class="btn btn-outline-success btn-read-more" @click="readRecipe(recipe)">Read more</button>
                </div>
              </div>
            </div>
          </div>
        </section>
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
            <li v-for="step in recipe.analyzedInstructions[0].steps" :key="step.number">
              <span v-for="ingredient in step.ingredients" :key="ingredient.id">
                {{ ingredient.name }}
              </span>
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
  