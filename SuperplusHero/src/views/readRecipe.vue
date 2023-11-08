<template>
  
  <div class="background">
  <div class="content">
    <div>
    <span class="hero-shot"><img :src="matchingRecipe.image" alt="Recipe Image" style="height: 90vh; width: 50vw;"></span>
    <h1>{{ matchingRecipe.title }}</h1>
    <p><strong>Summary:</strong> {{ matchingRecipe.summary }}</p>
    <p><strong>Cuisines:</strong> {{ matchingRecipe.cuisines.join(', ') }}</p>
    <p><strong>Dish Types:</strong> {{ matchingRecipe.dishTypes.join(', ') }}</p>
    <p><strong>Diets:</strong> {{ matchingRecipe.diets.join(', ') }}</p>
    <p><strong>Occasions:</strong> {{ matchingRecipe.occasions.join(', ') }}</p>
    <p><strong>Servings:</strong> {{ matchingRecipe.servings }}</p>
    <p><strong>Ready In:</strong> {{ matchingRecipe.readyInMinutes }} minutes</p>
    <p><strong>Health Score:</strong> {{ matchingRecipe.healthScore }}</p>
    <p><strong>Price Per Serving:</strong> ${{ matchingRecipe.pricePerServing }}</p>
    <p><strong>Source:</strong> <a :href="matchingRecipe.sourceUrl">{{ matchingRecipe.sourceName }}</a></p>

    <h2>Ingredients:</h2>
    <ul>
      <li v-for="ingredient in matchingRecipe.extendedIngredients">
        {{ ingredient.original }}
      </li>
    </ul>

    <h2>Instructions:</h2>
    <ol>
      <li v-for="step in matchingRecipe.analyzedInstructions[0].steps">
        {{ step.step }}
      </li>
    </ol>
  </div>

    <div class="row">
      <div class="col-md-12">
        <div class="recipe-card" v-if="matchingRecipe">
          <!-- Recipe Details: Start -->
          <div class="m-4 p-4 bg-light text-black rounded-3">
            <div class="row">
              <div class="col-md-4">
                <div>
                  <img :src="matchingRecipe.image" style="width: 100%;" :alt="matchingRecipe.title">
                </div>
              </div>

              <div class="col-md-8">
                <h2>{{ matchingRecipe.title }} Preparation</h2>
                <ol>
                  <li v-for="(step, index) in matchingRecipe.analyzedInstructions[0]?.steps.slice(0, 4)" :key="index">{{ step.step }}</li>
                  <p v-if="matchingRecipe.analyzedInstructions[0]?.steps.length > 4">. . . . .</p>
                </ol>
                <div>
                  <span style="color: green; font-weight: bold;">Cooking Time:</span> {{matchingRecipe.readyInMinutes }} Minutes <br>
                  <span style="color: green; font-weight: bold;">Serving Size:</span> {{matchingRecipe.servings }} Pax
                </div>  
                <div style="text-align: right;">
                  <button class="btn btn-success" @click="showRemainingSteps = true">Start Cooking</button>
                </div>
              </div>
            </div>
          </div>
          <!-- Recipe Details: End -->


        </div>
      </div>
    </div>

    <div class="row">
      <!-- Green Box -->
      <div class="col-md-6">
          <div class="common-box green-box">
            <h3>Available Ingredients</h3>
            <div v-if="matchingRecipe">
              <div class="recipe-ingredients">
                
                  <p v-for="step in matchingRecipe.analyzedInstructions[0]?.steps" :key="step.number">
                    <ul>
                      <li v-for="ingredient in step.ingredients" :key="ingredient.id">
                        <!-- Check if ingredient name is not empty before rendering -->
                        <div v-if="ingredient.name.trim() !== ''" class="ingredient-card">
                          <label for="ingredient-{{ ingredient.id }}">{{ ingredient.name }}</label>
                          <input type="checkbox" id="ingredient-{{ ingredient.id }}" />
                        </div>
                      </li>
                    </ul>
                  </p>
                
              </div>
            </div>
          </div>
        </div>

      <!-- Red Box -->
      <div class="col-md-6">
          <div class="common-box red-box">
            <h3>Missing Ingredients</h3>
            <div v-if="matchingRecipe" class="recipe-ingredients">
              
                <p v-for="step in matchingRecipe.analyzedInstructions[0]?.steps" :key="step.number">
                  <ul>
                    <li v-for="ingredient in step.ingredients" :key="ingredient.id">
                      <!-- Check if ingredient name is not empty before rendering -->
                      <div v-if="ingredient.name.trim() !== ''" class="ingredient-card">
                        <label for="ingredient-{{ ingredient.id }}">{{ ingredient.name }}</label>
                        <input type="checkbox" id="ingredient-{{ ingredient.id }}" checked/>
                      </div>
                    </li>
                  </ul>
                </p>
              
            </div>
          </div>
        </div>
      </div>

    <!-- Popup for Remaining Steps: Start -->
    <div class="popup" v-if="showRemainingSteps">
      <div class="popup-content">
        <span class="close" @click="showRemainingSteps = false">&times;</span>
        <div class="image-container">
          <img :src="matchingRecipe.image" alt="matchingRecipe.title" class="professional-image">
        </div>
        <h3>{{ matchingRecipe.title }}</h3>
        <ol>
          <li v-for="(step, index) in matchingRecipe.analyzedInstructions[0]?.steps.slice()" :key="index">{{ step.step }}</li>
        </ol>
      </div>
    </div>
    <!-- Popup for Remaining Steps: End -->
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
      showRemainingSteps: false, // Track whether to show the remaining steps popup
    };
  },
  async created() {
        try {
            console.log('All cookies:', Cookies.get());
        } catch(error) {
            console.error(error);
        }
    },
  computed: {
    matchingRecipe() {
      return this.recipes.results.find(recipe => recipe.title === this.recipeTitle);
    },
  },
  created() {
    // Retrieve the recipe title from the cookie when the component is created
    this.recipeTitle = Cookies.get('recipeTitle');
    console.log('Recipe Title:', this.recipeTitle);
  },
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap');
.background{
  background-color: rgb(237, 243, 235); 
  height: 100%;
}
div {
  font-family: 'Montserrat'
}

.content {
  margin-top: 80px;
  align-items: center;
  background-color: rgb(237, 243, 235);
  height: 100%;
  margin-left: 5%; 
  margin-right: 5%;
}

.hero-shot{
  margin-right: 0px !important ;
}

.ingredients {
  margin-top: 20px;
  padding: 10px;
}

/* Style for the checkbox input */
.recipe-ingredients input[type="checkbox"] {
  margin-right: 5px; /* Add some space between the checkbox and the label */
}

/* Style for the ingredient card */
.ingredient-card {
  border: 1px solid #ccc; /* Add a border around the card */
  padding: 10px;
  display: flex;
  justify-content: space-between; /* Align label and checkbox to opposite ends */
  align-items: center; /* Vertically center the content */
  margin-bottom: 5px; /* Add some space between cards */
}


/* Style for the label text (ingredient name) */
.recipe-ingredients label {
  display: inline-block;
  cursor: pointer; /* Change the cursor to a pointer on hover */
}

.recipe-card {
  align-items: center;
  width: 100%
}

.common-box {
  margin: 24px;
  color: black;
  padding: 10px;
  border-radius: 5px;
}

.green-box {
  background-color: rgb(226, 246, 244);
  margin-right: 12px;
}

.red-box {
  background-color: rgb(246, 226, 226);
  margin-left: 12px;
}

.popup {
  position: fixed;
  margin-top: 40px;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.7);
  z-index: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.popup-content {
  /* Add or modify these styles */
  background-color: #f7f7f7;
  padding: 20px;
  border: 1px solid #888;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  width: 80%; /* Increase the width if necessary */
  max-height: 80%; /* Limit the height to a percentage of the screen */
  overflow-y: auto; /* Add vertical scroll if content exceeds the height */
  border-radius: 5px;
  
  text-align: left; /* Adjust text alignment as needed */
  position: relative;
}

.image-container {
  text-align: center;
}

.professional-image {
  max-width: 100%;
  height: auto;
  display: block;
  margin: 0 auto; /* Center the image horizontally */
  border: 3px solid #ccc; /* Add a border */
  border-radius: 5px; /* Add rounded corners */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2); /* Add a subtle shadow */
}

.image-container img {
  margin: 0 auto; /* Center the image horizontally */
}

.close {
  color: #ff0000;
  font-size: 40px;
  font-weight: bold;
  cursor: pointer;
  position: absolute;
  top: 10px; 
  right: 30px; /* Adjust the value to control the distance from the right edge */
}

.close:hover,
.close:focus {
  color: #000;
}

.popup-content h3 {
  margin-top: 0;
}
</style>
