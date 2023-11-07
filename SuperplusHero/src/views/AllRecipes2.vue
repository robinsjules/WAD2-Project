<style scoped>
.content {
  margin-top: 80px;
}
</style>


<template>
<div class="content">
  <div class="container-fluid">
  <div class="row">
    <div class="">

    </div>
  </div>
</div></div>


































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
    // Automatically close the sidebar for small screens
    if (window.innerWidth <= 768) {
      this.isCollapsed = true;
    }
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
  