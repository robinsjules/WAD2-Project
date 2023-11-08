<template>
  <div class="background">
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
              <div class="input-group me-8">
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
      <div class="container">
        <div class="row">
          <div v-for="recipe in paginatedRecipes" :key="recipe.title" class="card mx-2 my-2" @mouseenter="isHovered = true" @mouseleave="isHovered = false">
              <!-- Your card content here -->
              <div class="card-image">
                <img :src="recipe.image" class="card-img" :alt="recipe.title">
                <div class="card-overlay">
                  <button class="read-more-button" @click="readRecipe(recipe)" v-show="isHovered">Read More</button>
                </div>
              </div>
              <div class="card-body">
                <span style="color: green; font-size: smaller;">RECIPE</span><br>
                <span class="card-title">{{ recipe.title }}</span>
                <p class="card-text">{{ recipe.description }}</p>
                <p style="position: absolute; bottom: 0px; left: 15px; font-size: smaller;">Ready In {{ recipe.readyInMinutes }} Minutes </p>
                <i class="fas fa-heart" style="position: absolute; bottom: 20px; right: 30px; color: red;"><span style="color: grey;">&nbsp;{{ recipe.aggregateLikes }}</span></i>
                </div>
              <!-- <div class="card-footer d-flex flex-column">
                <router-link @click="setRecipeTitleCookie(recipe.title)" :to="{ name: 'readRecipe', params: { id: recipe.title } }">
                  <button type="button" class="btn btn-outline-success mt-auto w-100">Read more</button>
                </router-link>
              </div> -->
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

import recipeData from '../../../backend/spoonacular/allCuisineNew.json'
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
      isHovered: false,
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
    mainContentStyle() {
    return {
      marginLeft: this.isCollapsed ? '100px' : '300px',
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
      Cookies.set("recipeTitle", this.recipeTitle);
    },
    // setRecipeTitleCookie(title) {
    //   // Set a cookie with the recipe title
    //   Cookies.set('recipeTitle', title);
    // },
    goToPage(page) {
      this.currentPage = page;
      this.scrollToTop();
    },
    nextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage += 1;
        this.scrollToTop();
      }
    },
    prevPage() {
      if (this.currentPage > 1) {
        this.currentPage -= 1;
        this.scrollToTop();
      }
    },
    resetPage() {
      this.currentPage = 1;
    },
    scrollToTop() {
      // Scroll smoothly to the top of the page
      window.scrollTo({
        top: 0,
        behavior: 'smooth',
      });
    },
  },
    watch: {
    searchQuery: 'resetPage', // Reset the page when searchQuery changes
    selectedCuisine: 'resetPage', // Reset the page when selectedCuisine changes
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
  margin-left: 300px; /* Adjust the margin to match the sidebar's width */
  padding: 20px; /* Add some padding to separate content from sidebar */
  margin-right: 50px;
}

.card {
  position: relative;
  background-color: white;
  height: 350px;
  width: 300px;
  padding: 0;
  border-radius: 0;
  overflow: hidden;
  transition: opacity 0.2s;
}

.read-more-button {
  background-color: green;
  color: white;
  border: none;
  border-radius: 0; /* Remove border radius */
  padding: 5px 10px;
  cursor: pointer;
  margin-top: 100px; /* Add margin of 50px */
  width: 150px;
  height: 50px;
}

.card:hover::before {
  content: ''; /* Create a pseudo-element */
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border: 5px solid transparent; /* Initially transparent border */
  box-sizing: border-box; /* Include border in the element's dimensions */
  transition: border-color 0.2s; /* Transition for border-color only */
}

.card:hover {
  z-index: 1;
  transition: opacity 0.2s;
  opacity: 100%;
 
  }

  .card:hover::before {
  border-color: rgb(0, 220, 0); /* Border color on hover (adjust to your preference) */
}

.card:hover .card-overlay {
  opacity: 1; /* Make the overlay visible on hover */
}

.card-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.2);
  opacity: 0;
  transition: opacity 0.2s;
  display: flex;
  justify-content: center;
  align-items: flex-start; /* Align items to the top */;
}



.card-image img {
  width: 300px;
  height: 200px;
  border-radius: 0;
}

.card-title {
  font-size: 1rem;
  font-weight: bold;
}

.card-text {
  color: #666;
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
  font-size: 16px; /* Default font size for large screens */
}

.toggle-button {
  position: absolute;
  right: 0; /* Position the button on the right side */
  top: 50%; /* Center the button vertically */
  transform: translateY(-50%); /* Adjust for vertical centering */
  background-color: green;
  color: white;
  width: 30px; /* Adjust the width of the rectangle */
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