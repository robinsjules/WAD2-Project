<template>
    <div class="content">
      <h1 class="text-success" style="font-weight: bold;">All Recipes</h1>
  
      <!-- Search Bar -->
      <form @submit.prevent="searchRecipes">
        <div class="container-fluid">
          <div class="form-group">
            <div class="row justify-content-center">
              <div class="col-md">
                <div class="input-group">
                  <input v-model="searchQuery" type="text" class="form-control" placeholder="Search Recipe..">
                  <div class="input-group-append">
                    <button class="btn btn-success" type="submit">Search</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </form>
  
      <!-- Filter Dropdown -->
      <div class="col-4 btn-group mt-2">
        <select v-model="selectedCuisine" class="form-select" aria-label="Default select example">
          <option value="" selected>Filter by cuisine</option>
          <option value="local">Local (Singapore)</option>
          <option value="western">Western</option>
          <option value="chinese">Chinese</option>
          <option value="indian">Indian</option>
          <option value="malay">Malay</option>
          <option value="japanese">Japanese</option>
          <option value="korean">Korean</option>
          <option value="thai">Thai</option>
          <option value="french">French</option>
        </select>
      </div>
  
      <!-- Recipe Cards -->
      <section>
        <div class="container-fluid">
          <div class="row justify-content-center">
            <div v-for="recipe in filteredRecipes" :key="recipe.id" class="card m-2 pt-2" style="width: 18rem">
              <img :src="recipe.image" class="card-img-top" :alt="recipe.title">
              <div class="card-body" style="display: flex; flex-direction: column; justify-content: space-between;">
                <h5 class="card-title">{{ recipe.title }}</h5>
                <p class="card-text">{{ recipe.description }}</p>
                <button type="button" class="btn btn-outline-success" style="align-self: flex-end;" @click='readRecipe'>Read more</button>
              </div>
            </div>
          </div>
        </div>
      </section>
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
      };
    },
    computed: {
      filteredRecipes() {
        return this.recipes.results.filter((recipe) => {
          const searchMatch = this.searchQuery === "" || recipe.title.toLowerCase().includes(this.searchQuery.toLowerCase());
          const cuisineMatch = this.selectedCuisine === "" || recipe.cuisine === this.selectedCuisine;
          return searchMatch && cuisineMatch;
        });
      },
    },
    methods: {
      searchRecipes() {
        // Perform a search action if needed
        // For now, we just update the filteredRecipes computed property
      },
      readRecipe() {
        this.$router.push({name: 'readRecipe'})
      }
    },
  };
  </script>
  