<template>
    <div>
      <h1>Data from JSON</h1>
      <ul>
        <li v-for="recipe in recipes.results">
          {{ recipe.title }}
          <img :src="recipe.image" alt="">
          <ol>
            <li v-for="step in recipe.analyzedInstructions[0]?.steps" :key="step.number">
              {{ step.step }}
              <h3>Ingredients:</h3>
              <ul>
                <li v-for="ingredient in step.ingredients" :key="ingredient.id">
                  {{ ingredient.name }}
                </li>
              </ul>
            </li>
          </ol>
        </li>
      </ul>
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