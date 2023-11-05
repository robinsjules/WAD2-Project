<template>
  <div class="content">
  <h2>Recipe Title: {{ recipeTitle }}</h2>
  <!-- <div class="recipe-details">
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
  </div> -->
</div>
</template>

<script>
export default {
  data() {
    return {
      recipeTitle: '', // Initialize the recipe title
      // recipe: {
      //   image: '',
      //   analyzedInstructions: [
      //     {
      //       steps: [],
      //     },
      //   ],
      // },
    };
  },
  created() {
    // Access the route parameter and assign it to the data property
    this.recipeTitle = this.$route.params.title;
    // Fetch recipe details based on the recipeId parameter passed from the route
  },
  methods: {
  },
};
</script>

<style scoped>
.content {
  margin-top: 500px;
}
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
