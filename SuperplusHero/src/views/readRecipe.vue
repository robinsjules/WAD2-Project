<template>
  <div class="recipe-details">
    <div class="recipe-image">
      <img :src="recipe.image" alt="Recipe" />
    </div>
    <div class="recipe-instructions">
      <h2>Instructions</h2>
      <ol>
        <li v-for="step in recipe.analyzedInstructions[0].steps" :key="step.number">
          {{ step.step }}
        </li>
      </ol>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      recipe: {
        image: '',
        analyzedInstructions: [
          {
            steps: [],
          },
        ],
      },
    };
  },
  created() {
    // Fetch recipe details based on the recipeId parameter passed from the route
    const recipeId = this.$route.params.recipeId;
    // You should implement logic to fetch the specific recipe data based on recipeId
    // and populate the 'recipe' data property.
    // For this example, let's assume you have a function to fetch the recipe data.
    this.fetchRecipeDetails(recipeId);
  },
  methods: {
    // Implement a method to fetch recipe details based on recipeId
    fetchRecipeDetails(recipeId) {
      // Make an API call or fetch data from your data source here and set it to this.recipe
    },
  },
};
</script>

<style scoped>
.recipe-details {
  display: flex;
  align-items: center;
}

.recipe-image {
  flex: 1;
  margin: 1rem;
}

.recipe-image img {
  max-width: 100%;
}

.recipe-instructions {
  flex: 2;
  margin: 1rem;
}

.recipe-instructions h2 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.recipe-instructions ol {
  list-style-type: decimal;
  padding-left: 1rem;
}

.recipe-instructions li {
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
}
</style>
