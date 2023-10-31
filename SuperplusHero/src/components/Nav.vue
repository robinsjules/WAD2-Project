<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap');

.navbar-nav{
    margin-left: auto;
}

.navbar-success.navcolor {
  background-color: black; 
  position: fixed;
  width: 100%;
  z-index: 1000;
  top: 0;
  left: 0;
  right: 0;
}

.navbar-brand img {
  margin-left: 10px;
}

.nav-link img {
    margin-left: 20px;
}

</style>

<template>
  <nav v-if="showNavBar" class="navbar navbar-expand-md navbar-success navcolor">
    <router-link to="/">
      <a class="navbar-brand" href="#"><img src="../assets/appLogoForNav.png" alt="Logo" height="70"></a>
    </router-link>
      <ul class="navbar-nav">
        <li class="nav-item">
          <router-link to="/"> <!-- Edit to Community Page, also apply to index.js router -->
            <a class="nav-link" href="#"><img src="../assets/communityWhite.png" alt="Community" width="50" height="50"></a>
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/"> <!-- Edit to Cart Page, also apply to index.js router -->
            <a class="nav-link" href="#"><img src="../assets/cartWhite.png" alt="Cart" width="50" height="50"></a>
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/"> <!-- Edit to Fridge Page, also apply to index.js router -->
            <a class="nav-link" href="#"><img src="../assets/fridgeWhite.png" alt="Fridge" width="50" height="50"></a>
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/profile">
            <a class="nav-link" href="#"><img src="../assets/profileWhite.png" alt="Profile" width="50" height="50"></a>
          </router-link>
        </li>
      </ul>
  </nav>
</template>

<script>
export default {
  data() {
    return {
      showNavBar: true, // Default to show the navigation bar
    };
  },
  watch: {
    $route(to) {
      // Check the route and conditionally hide the navigation bar on specific routes
      this.showNavBar = !['/login', '/register', '/register2'].includes(to.path);
    },
  },
};
</script>