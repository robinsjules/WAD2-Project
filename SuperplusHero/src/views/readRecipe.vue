<template>
  <div class="content">
    <div>
      <h3>Recipe Title: {{ recipeTitle }}</h3>

      <div v-for="recipe in recipes.results" :key="recipe.id" class="recipe-card">
        <p v-if="recipeTitle == recipe.title">

          <div class="recipe-image">
            <img :src="recipe.image" :alt="recipe.title" />
          </div>
          <div class="recipe-details">
            
            <h3>Instructions:</h3>
            <ol>
              <li v-for="step in recipe.analyzedInstructions[0]?.steps" :key="step.number">
                {{ step.step }}
              </li>
            </ol>
          </div>

          <div class="recipe-ingredients">
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
          </div>

        <!-- Recipe Details: Start -->
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
        <!-- Recipe Details: End -->
              
            
          
          
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import recipeData from '../../../backend/spoonacular/allCuisine.json';
import Cookies from 'js-cookie';

export default {
  data() {
    return {
      recipeTitle: '', // Initialize the recipeTitle data property
      recipes: recipeData,
    };
  },
  created() {
    // Retrieve the recipe title from the cookie when the component is created
    this.recipeTitle = Cookies.get('recipeTitle');
  },
};
</script>

<style scoped>
.content {
  margin-top: 100px;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.recipe-card {
  margin: 1rem;
  display: flex;
  align-items: center;
}

.recipe-details {
  flex: 2;
}

.recipe-image {
  flex: 1;
  margin-left: 1rem;
}

.recipe-image img {
  max-width: 100%;
}

.recipe-ingredients {
  margin-top: 1rem;
}

.recipe-ingredients h3 {
  font-size: 1.2rem;
}

.recipe-ingredients ul {
  list-style-type: disc;
  padding-left: 2rem;
}

.recipe-ingredients li {
  font-size: 1rem;
  margin-bottom: 0.25rem;
}
</style>
