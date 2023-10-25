<template>
  <nav v-if="showNavBar" class="navbar navbar-expand-lg navbar-success bg-success">
    <a class="navbar-brand" href="#"><img src="" alt="Logo" width="80" height="30"></a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link" href="#"><img src="../assets/comm.png" alt="Community" width="50" height="50"></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#"><img src="../assets/cart.png" alt="Cart" width="50" height="50"></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#"><img src="../assets/fridge.png" alt="Fridge" width="50" height="50"></a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#"><img src="../assets/profile.png" alt="Profile" width="50" height="50"></a>
        </li>
      </ul>
    </div>
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
  