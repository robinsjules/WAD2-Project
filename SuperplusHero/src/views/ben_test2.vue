<template>
    <div>
      <h1>Data from JSON</h1>
      <ul>
        <p v-for="recipe in recipes.results">
          <h2>{{ recipe.title }}</h2>
          <img :src="recipe.image" alt="">
          <ol>
            <li v-for="step in recipe.analyzedInstructions[0]?.steps" :key="step.number">
              {{ step.step }}
            </li>
          </ol>
          <h3>Ingredients:</h3>
          <ul>
            <p v-for="step in recipe.analyzedInstructions[0]?.steps" :key="step.number">
              <ul>
                <li v-for="ingredient in step.ingredients" :key="ingredient.id">
                  {{ ingredient.name }}
                </li>
              </ul>
            </p>
          </ul>
          <h3>Equipment:</h3>
          <ul>
            <li v-for="step in recipe.analyzedInstructions[0]?.steps" :key="step.number">
              <ul>
                <li v-for="equip in step.equipment" :key="equip.id">
                  {{ equip.name }}
                </li>
              </ul>
            </li>
          </ul>
        </p>
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