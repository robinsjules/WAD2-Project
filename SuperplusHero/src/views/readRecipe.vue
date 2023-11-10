<template>
<body>
  <div class="background">
    <!-- <div class="container-fluid"> -->
      <!-- Start of Hero Image -->
      <div class="row" style="margin-top: 85px; border-bottom: 1px solid; background-color: white; ">
        <div class="col-lg-6 col-12 centered-content">
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
          <img :src="matchingRecipe.image" alt="Recipe Image" style="width: 100%; height: 100%;">
        </div>
      </div>
    <!-- End of Hero Image -->
    <!-- </div> -->
<div class="container-fluid">
    <div class="row main-content">
        <div class="col-lg-8 col-12" style=" margin-right: 20px; padding-top: 20px; margin-bottom: 5%;">
            <h2>About {{ matchingRecipe.title }} (Serving Size: {{ matchingRecipe.servings }})</h2><br>
            <p>{{ matchingRecipe.summary }}</p>
        </div>
        
        <div class="col-lg-3 col-12 card">
            <h3>Ingredients:</h3>
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




      <div class="col-md-12">

          <!-- Recipe Details: Start -->
          <div class="bg-light text-black rounded-3" style="margin-top: 5%;">
            <div class="row main-content">
              <div class="col-md-4">
                <div>
                  <img :src="matchingRecipe.image" style="width: 100%;" :alt="matchingRecipe.title">
                </div>
              </div>

              <div class="col-md-8">
                <h2>{{ matchingRecipe.title }}</h2>
                <ol>
                  <li v-for="(step, index) in matchingRecipe.analyzedInstructions[0]?.steps.slice(0, 4)" :key="index">{{ step.step }}</li>
                  <p v-if="matchingRecipe.analyzedInstructions[0]?.steps.length > 4">. . . . .</p>
                </ol>
                <div>
                  <span style="color: rgb(10, 160, 10); font-weight: bold;">Cooking Time:</span> {{matchingRecipe.readyInMinutes }} Minutes <br>
                  <span style="color: rgb(10, 160, 10); font-weight: bold;">Serving Size:</span> {{matchingRecipe.servings }} Pax
                </div>  
                <div style="text-align: right;">
                  <button class="btn btn-success" style="background-color: rgb(10, 160, 10)" @click="showRemainingSteps = true">Start Cooking</button>
                </div>
              </div>
          </div>
          <!-- Recipe Details: End -->
        </div>
    </div>
  </div>

      <div class="content-seperator">
        <p style="text-align: center;"><hr>
          <div>
            <h3><strong>Before We Begin</strong></h3>
          <!-- <i class="fa-solid fa-rotate-right" style="font-size: 30px;"></i> -->
          <!-- <p>Checking your fridge . . .</p> -->
          <a @click="toggleContent">
            <p class="btn surplus-hero2">{{ isContentVisible ? "Check your ingredients" : "Click me to check your ingredients!" }}</p>
          </a>

          </div>
        </p><hr>
        <p style="text-align: center; font-weight: bold;">________</p>
      </div>

      <!-- Hidden Content -->
      <div v-if="isContentVisible">

      
      <div class="container">
      <div  style="margin-bottom: 5%;">
        <!-- Green Box -->
        <div>
          <div class="common-box">
            <h3>Ingredients for Recipe:</h3>
            <div v-if="matchingRecipe">
              <div class="recipe-ingredients">
                <p v-for="step in matchingRecipe.analyzedInstructions[0]?.steps" :key="step.number">
                  <p>
                    <p v-for="(ingredient, index) in step.ingredients.slice(0, 5)" :key="ingredient.id">
                      <!-- Check if ingredient name is not empty before rendering -->
                      <div v-if="ingredient.name.trim() !== ''" class="ingredient-card">
                        <label :for="`ingredient-${ingredient.id}`">{{ ingredient.name }}</label>
                        <div>
                        </div>
                        <!-- Use a method to determine the checked state dynamically -->
                        <input type="checkbox" :id="`ingredient-${ingredient.id}`" :checked="isChecked(index)" />
                      </div>
                    </p>
                  </p>
                </p>
              </div>
            </div>
          </div>
          <div>
          </div>
        </div>

        <!-- Red Box -->
        <!-- <div class="col-md-6">
          <div class="common-box red-box">
            <h3>Missing Ingredients</h3>
            <div v-if="matchingRecipe">
              <div class="recipe-ingredients">
                <p v-for="step in matchingRecipe.analyzedInstructions[0]?.steps" :key="step.number">
                  <p>
                    <p v-for="ingredient in step.ingredients" :key="ingredient.id">

                      <div v-if="ingredient.name.trim() !== ''" class="ingredient-card">
                        <label for="ingredient-{{ ingredient.id }}">{{ ingredient.name }}</label>
                        <input type="checkbox" id="ingredient-{{ ingredient.id }}" />
                      </div>
                    </p>
                  </p>
                </p>
              </div>
            </div>
          </div>
        </div> -->

      </div>
    </div>
  </div>
        <!-- Hidden Content -->
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
  </body>
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
      isContentVisible: false,
      checkedIngredients: [],
      items: [],
      checkedIngredients: Array(3).fill(true),
    };
  },

  async created() {
        try {
            console.log('All cookies:', Cookies.get());
            const response = await axios.get(`http://127.0.0.1:5000/listings`);
            this.items = response.data;
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
  methods: {
    toggleContent() {
      this.isContentVisible = !this.isContentVisible;
    },
    isChecked(index) {
      // Use the checkedIngredients array to determine the checked state
      return this.checkedIngredients[index];
    // to get fridge
    },
    async fetchFridgeFromServer() {
            try {
                const fridgeuser = 'julesrobins';
                const response = await axios.get(`http://127.0.0.1:5000/fridge/${fridgeuser}`);
                console.log('Fetched Fridge Data:', response.data); // Log the fetched data
                this.data = response.data;
                this.items = this.data[0].Fridge;

                this.checkedIngredients = serverData.map(item => item.toLowerCase());

            } catch (error) {
                console.error('Error fetching items:', error);
            }
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
body {
  background-color: rgb(237, 243, 235); 
}
div {
  font-family: 'Montserrat';
  overflow: hidden;
  line-height: 1.5;
}


.reference{
  margin-top: 1000px
}

.col-12 {
  max-width: 100%;
  overflow: hidden;
  /* height: 400px !important; */
}


.col-lg-6 {
  max-width: 100%;
  overflow: hidden;
  height: 90vh !important; 
}

.main-content {
  margin: 5%;
}

.card{
  padding-top: 20px;
  padding-bottom: 20px;
  max-height: fit-content; 
  margin: 30px;
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
  background-color: rgb(10, 160, 10);
  color: white;
  width: fit-content;
  padding: 10px;
  margin: auto;
}

.surplus-hero2 {
  border: 2px solid;
  color: rgb(10, 160, 10);
  width: fit-content;
  padding: 5px;
  margin: auto;
  font-size: 16px;
}
.surplus-hero2:hover {
  border: 2px solid;
  background-color: rgb(10, 160, 10);
  color: white;
  width: fit-content;
  padding: 5px;
  margin: auto;
  font-size: 16px;
}

.recipe-title {
  margin-top: 5%;
  margin-bottom: 5%;
  font-weight: bold;
  font-size: 3rem;
}


.hover-effect {
  transition: color 0.3s, text-decoration 0.3s;
}

.hover-effect:hover {
  color: rgb(10, 160, 10);
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
  margin: 0px; 
  width: 100%;
  display: flex;
  justify-content: space-between; /* Align label and checkbox to opposite ends */
  align-items: center; /* Vertically center the content */
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
  width: 100%;
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

.content-seperator{
  margin: 5%;
  /* border-top: 1px solid;
  border-bottom: 1px solid; */
  padding: 20px
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
.click-me-text {
  animation: moveUpDown2 2s linear alternate;
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

@keyframes moveUpDown2 {
  0% {
    transform: translateY(0);
  }
  100% {
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
