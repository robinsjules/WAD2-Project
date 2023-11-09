<template>
  
  <div class="background">
    <!-- <div class="container-fluid"> -->
      <!-- Start of Hero Image -->
      <div class="row" style="margin-top: 85px; border-bottom: 1px solid; background-color: white; ">
        <div class="col-lg-6 col-12 centered-content" >
          <p class="surplus-hero">SurplusHero</p>
          <h1 class="recipe-title">{{ matchingRecipe.title }}</h1>
          <p style="font-size: 1rem;">Suitable for {{ matchingRecipe.diets.join(', ') }}</p>

          <p style="font-weight: bold;">______________________</p>

            <h6>Made for {{ matchingRecipe.servings }} pax</h6>
          <button class="btn" @click="showRemainingSteps = true">
            <h6 class="hover-effect" style="margin-bottom: 0px;">Ready In {{ matchingRecipe.readyInMinutes }} minutes</h6>
          </button>
          <div>
            
            <i class="click-me fa-solid fa-sort-up fa-flip-vertical" style="height: 20px;"></i>

            

          </div>
        </div>

        <div class="col-lg-6 col-12 d-flex justify-content-center justify-content-md-end">
          <img :src="matchingRecipe.image" alt="Recipe Image" style="width: 100%; height: 100%;" class="img-fluid custom-image" >
        </div>
      </div>
    <!-- End of Hero Image -->
    <!-- </div> -->
<div class="container-fluid">
    <div class="row main-content">
        <div class="col-8" style="border-top: 1px solid; margin-right: 5%; padding-top: 5%;">
            <h2>About {{ matchingRecipe.title }} (Serving Size: {{ matchingRecipe.servings }})</h2><br>
            <p>{{ matchingRecipe.summary }}</p>
        </div>
        
        <div class="col-3 card">
            <h3>Ingredients:</h3>
            <p></p>
            <ul>
                <li v-for="ingredient in matchingRecipe.extendedIngredients">
                    {{ ingredient.original }}
                </li>
            </ul>

            <div style="text-align: right;">
                <button class="btn moving-item hover-effect" @click="showRemainingSteps = true">
                    Let's Get Started <i class="fa-solid fa-angle-right"></i>
                </button>
            </div>
        </div>
    </div>
</div>

  </div>
    
    

    <div class="reference">
    <div>
    
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
    <div class="container">
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
    beforeRouteLeave(to, from, next) {
    // Scroll to the top before leaving the current route
    window.scrollTo(0, 0);

    // Continue with the route navigation
    next();
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
  font-family: 'Montserrat';
  overflow: hidden
}


.reference{
  margin-top: 1000px
}

.custom-image {
  max-width: 100%;
  max-height: 80vh;
}

@media (max-width: 992px) {
  .custom-image {
    max-height: 60vh;
  }
}

.main-content {
  padding-top: 20px;
  margin: 5%;
}

.card{
  max-height: fit-content; 
  padding: 20px;
  border-radius: 0px;
  background-color: transparent;
  border: 0px;
  border-top: 3px solid;
  border-bottom: 3px solid;
}

.centered-content {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 5%;
}

.surplus-hero {
  background-color: green;
  color: white;
  width: fit-content;
  padding: 10px;
}

.recipe-title {
  margin-top: 5%;
  margin-bottom: 5%;
  font-weight: bold;
  font-size: 3rem;
}

.section-divider {
  margin-left: 30%;
  margin-right: 30%;
}

.hover-effect {
  transition: color 0.3s, text-decoration 0.3s;
}

.hover-effect:hover {
  color: green;
  text-decoration: underline;
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
  color: rgb(0, 0, 0);
  padding: 10px;
  border-radius: 5px;
}

.green-box {
  background-color: rgb(226, 246, 244);
}

.red-box {
  background-color: rgb(246, 226, 226);
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
  padding: 30px;
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

/* Click Me */
.click-me {
  font-size: 36px;
  padding: 10px 20px;
  margin-top: 10px;
  color: black;
  border: none;
  /* cursor: pointer; */
  transition: background-color 0.3s;
  animation: moveUpDown 2s linear infinite; /* Add this line */
}

.moving-item {
            position: relative;
            animation: moveLeftRight 2s linear infinite;
        }

/* Define the animation */
@keyframes moveUpDown {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-20px);
  }
}

@keyframes moveLeftRight {
  0% {
                right: 0px;
            }
            50% {
                right: 25px; /* Move to the right */
            }
            100% {
                right: 0; /* Move back to the left */
            }
}
</style>
