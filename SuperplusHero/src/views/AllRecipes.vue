<template>
  <div>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">

    

    <!-- Sidebar -->
    <div class="sidebar" :class="{ collapsed: isCollapsed }">
      <div class="nav" v-if="!isCollapsed">
        
        <ul>
          <li @click="selectedCuisine = ''" :class="{ active: selectedCuisine === '' }">
            <a href="#">Show All</a>
          </li>
          <li
            v-for="cuisine in uniqueCuisines"
            :key="cuisine"
            @click="selectedCuisine = cuisine"
            :class="{ active: selectedCuisine === cuisine }"
          >
            <a href="#">{{ cuisine }}</a>
          </li>
        </ul>
      </div>

      <!-- Collapse Button -->
      <div class="toggle-button" @click="toggleSidebar">
        <i :class="isCollapsed ? 'fas fa-chevron-right' : 'fas fa-chevron-left'"></i>
      </div>
      <!-- Additional sidebar content if needed -->
    </div>


    <!-- Main Content -->
    <div class="content" :style="mainContentStyle">
      <h2 style="color: rgb(10, 160, 10); margin-left:15px;">Recipe Book</h2>
      <!-- Search Bar -->
      <div class="container-fluid">
        <div class="form-group">
          <div class="row justify-content-center">
            <div class="col-md">
              <div class="input-group">
                <input v-model="searchQuery" type="text" class="form-control" placeholder="Search Recipe..">
                <div class="input-group-append">
                  <button class="btn btn-success" type="button" @click="searchRecipes">Search</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>


      <!-- Number of recipes to display per page -->

    <div class="form-group m-3">
      <label for="recipesPerPage">Recipes per Page: &nbsp;</label>
      <select id="recipesPerPage" v-model="recipesPerPage">
        <option value="10">10</option>
        <option value="20">20</option>
        <option value="30">30</option>
        <option value="40">40</option>
        <option value="50">50</option>
      </select>
    </div>

<!-- Recipe Cards -->
    <section>
      <br>
      <div class="container-fluid">
        <div class="row justify-content-left">
          <div v-for="recipe in paginatedRecipes" :key="recipe.title" class="card mx-2 my-3" style="width: 13rem; height: auto;">
              <!-- Your card content here -->
              <div class="card-image">
                <img :src="recipe.image" class="card-img-top" :alt="recipe.title">
              </div>
              <div class="card-body">
                <h5 class="card-title">{{ recipe.title }}</h5>
                <p class="card-text">{{ recipe.description }}</p>
              </div>
              <div class="card-footer d-flex flex-column">
                <router-link @click="setRecipeTitleCookie(recipe.title)" :to="{ name: 'readRecipe', params: { id: recipe.title } }">
                  <button type="button" class="btn btn-outline-success mt-auto w-100">Read more</button>
                </router-link>
              </div>
            </div>
          </div>
        </div>
      </section>
    

      <!-- Pagination Controls -->
    <div class="pagination">
      <button @click="goToPage(1)" :disabled="currentPage === 1">First</button>
      <button @click="prevPage" :disabled="currentPage === 1">Previous</button>
      <span>Page {{ currentPage }} of {{ totalPages }}</span>
      <button @click="nextPage" :disabled="currentPage === totalPages">Next</button>
      <button @click="goToPage(totalPages)" :disabled="currentPage === totalPages">Last</button>
    </div>

    <!-- Total Results -->
    <div>Total Results: {{ filteredRecipes.length }}</div>
  </div>
</div>
</template>

<script>

import recipeData from '../../../backend/spoonacular/allCuisine.json'
import Cookies from 'js-cookie';


export default {
  data() {
    return {
      selectedCuisine: '', // Selected cuisine for filtering
      recipes: { results: [] }, // Initialize with an empty results array
      searchQuery: '',
      isCollapsed: false,
      recipesPerPage: 20, // Default number of recipes per page
      currentPage: 1, // Current page number
    };
  },
  computed: {
    uniqueCuisines() {
      // Extract unique cuisines from the recipe data
      const cuisines = new Set();
      if (this.recipes.results) {
        this.recipes.results.forEach((recipe) => {
          recipe.cuisines.forEach((cuisine) => {
            cuisines.add(cuisine);
          });
        });
      }
      return Array.from(cuisines);
    },
    filteredRecipes() {
      // Filter recipes based on selected cuisine and searchQuery
      return this.recipes.results
        .filter((recipe) => {
          // Check for unique recipes based on title
          return !this.isDuplicateRecipe(recipe);
        })
        .filter((recipe) => {
          const cuisineMatch = this.selectedCuisine === '' || recipe.cuisines.includes(this.selectedCuisine);
          const searchMatch = this.searchQuery === '' || recipe.title.toLowerCase().includes(this.searchQuery.toLowerCase());
          return cuisineMatch && searchMatch;
        });
    },
    paginatedRecipes() {
      const startIndex = (this.currentPage - 1) * this.recipesPerPage;
      const endIndex = this.currentPage * this.recipesPerPage;
      return this.filteredRecipes.slice(startIndex, endIndex);
    },
    totalPages() {
      return Math.ceil(this.filteredRecipes.length / this.recipesPerPage);
    },
    watch: {
    selectedCuisine: 'resetPage',
    searchQuery: 'resetPage',
    filterRecipes: 'resetPage'
    },
    mainContentStyle() {
    return {
      marginLeft: this.isCollapsed ? '50px' : '250px',
      transition: 'margin-left 0.3s ease' // Adjust the duration and easing as needed
    };
  },

  },
  mounted() {
    // Load recipe data from the JSON file when the component is mounted
    this.recipes = recipeData;
  },
  methods: {

    filterRecipes() {
      // Handle filtering recipes based on selected cuisine
    },
    searchRecipes() {
      // The filtering is done through the computed property
    },
    isDuplicateRecipe(recipe) {
      // Function to check if a recipe is a duplicate based on title
      const titles = this.recipes.results.map((r) => r.title);
      const index = titles.indexOf(recipe.title);
      return index !== -1 && index !== titles.lastIndexOf(recipe.title);
    },
    toggleSidebar() {
      this.isCollapsed = !this.isCollapsed;
    },
    // Navigate to the ReadRecipe component
    readRecipe(recipe) {
      this.recipeTitle = recipe.title; // Set the recipeTitle here
      this.$router.push({ name: 'readRecipe', params: { id: recipe.title } });
    },
    setRecipeTitleCookie(title) {
      // Set a cookie with the recipe title
      Cookies.set('recipeTitle', title);
    },
    goToPage(page) {
      this.currentPage = page;
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage += 1;
      }
    },
    prevPage() {
      if (this.currentPage > 1) {
        this.currentPage -= 1;
      }
    },
    resetPage() {
      this.currentPage = 1;
    },
  },
};
</script>
  
<style scoped>
.content {
  margin-top: 80px;
  margin-left: 250px; /* Adjust the margin to match the sidebar's width */
  padding: 20px; /* Add some padding to separate content from sidebar */
  background-color: rgb(237, 243, 235);
}


.card {
  border: 1px solid #ccc;
  border-radius: 10px;
  transition: transform 0.2s;
  background-color: white
}

.card:hover {
  transform: scale(1.1);
  }

.card-image img {
  margin-top: 10px;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
}

.card-title {
  font-size: 1.25rem;
  font-weight: bold;
}

.card-text {
  color: #666;
}

.btn-read-more {
  align-self: flex-end;
}

.sidebar {
  position: fixed; /* Fix the sidebar in place */
  top: 0; /* Position it at the top */
  left: 0; /* Position it at the left */
  width: 250px;
  padding: 20px;
  background-color: #333;
  color: #fff;
  font-size: 16px;
  height: 100vh;
  overflow-y: auto;
  margin-top: 85px;
  transition: width 0.3s;
}

.toggle-button {
  position: absolute;
  right: 0; /* Position the button on the right side */
  top: 50%; /* Center the button vertically */
  transform: translateY(-50%); /* Adjust for vertical centering */
  background-color: green;
  color: white;
  width: 50px; /* Adjust the width of the rectangle */
  height: 20%; /* Full height of the sidebar */
  border-top-left-radius: 10px; /* Rounded top-left corner */
  border-bottom-left-radius: 10px; /* Rounded bottom-left corner */
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  z-index: 2;
}

/* Additional styles for the button icon */
.toggle-button i {
  font-size: 20px;
}

.sidebar.collapsed {
  width: 50px; /* Adjust the width of the collapsed sidebar as needed */
}

.sidebar ul {
  list-style: none;
  padding: 0;
}

.sidebar ul li {
  margin-bottom: 10px;
}

.sidebar ul li a {
  text-decoration: none;
  color: #fff;
  display: block;
  padding: 5px 10px;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.sidebar ul li a:hover {
  background-color: #555; /* Change the background color on hover */
}

.sidebar ul li.active a {
  background-color: green; /* Highlight the active cuisine */
}

/* Additional styling for active link */
.sidebar ul li.active a:hover {
  background-color: #0056b3; /* Highlight the active cuisine on hover */
}
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 10px 0;
}

.pagination button {
  margin: 0 5px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 8px 16px;
  cursor: pointer;
}

.pagination button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}

.pagination select {
  margin: 0 10px;
  padding: 5px;
}


</style>