<style scoped>



</style>

<template>
  <nav v-if="showNavBar" class="navbar navbar-expand-md navbar-success bg-success">
    <router-link to="/">
      <a class="navbar-brand" href="#"><img src="../assets/appLogo.png" alt="Logo" width="50" height="50"></a>
    </router-link>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">

        <li class="nav-item">
            <!-- Modal trigger -->
            <a 
            class="nav-link" 
            href="#"
            data-bs-toggle="modal"
            data-bs-target="#postalCodeModal"
          >
            <img src="../assets/location.png" alt="Location Pin" width="50" height="50">
          </a>

        </li>

        <li class="nav-item">
          <button 
              type="button"
              class="btn btn-link" 
              data-bs-toggle="modal" 
              data-bs-target="#notificationModal"
              @click="openNoti"
              aria-label="Show notifications"
            ><img src="../assets/noti.png" width="50" height="50">
          <span class="badge bg-danger" v-if="newNotifications" role="alert">{{notificationCount}}</span>
          <i class="bi bi-bell"></i>
    </button>

            <div 
              class="modal" 
              tabindex="-1" 
              role="dialog" 
              id="notificationModal" 
              aria-labelledby="notificationModalLabel" 
              aria-hidden="true">
              <div class="modal-dialog">
                  <div class="modal-content">
                      <div class="modal-header">
                          <h5 class="modal-title" id="notificationModalLabel">Notifications</h5>
                          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                      </div>
                      <div class="modal-body">
                          You have {{notificationCount}} new notifications.
                          <!-- REPLACE WITH THE EXPIRING NOTIFICATIONS FROM SUPABASE  -->
                      </div>
                  </div>
              </div>
          </div>

        </li>

        <li class="nav-item">
          <router-link to="/"> <!-- Edit to Community Page, also apply to index.js router -->
            <a class="nav-link" href="#"><img src="../assets/comm.png" alt="Community" width="50" height="50"></a>
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/"> <!-- Edit to Cart Page, also apply to index.js router -->
            <a class="nav-link" href="#"><img src="../assets/cart.png" alt="Cart" width="50" height="50"></a>
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/"> <!-- Edit to Fridge Page, also apply to index.js router -->
            <a class="nav-link" href="#"><img src="../assets/fridge.png" alt="Fridge" width="50" height="50"></a>
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/profile">
            <a class="nav-link" href="#"><img src="../assets/profile.png" alt="Profile" width="50" height="50"></a>
          </router-link>
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
      notificationCount: 0,
      newNotifications: false
    };
  },
  methods: {
    openNoti() {
      // reset notification count 
      this.notificationCount = 0;
      this.newNotifications = false;
    }
  },
  created(){
    setInterval(() => {
      this.notificationCount++;
      this.newNotifications = true;
    }, 30000); // simulate notification every 30 seconds
  },
  watch: {
    $route(to) {
      // Check the route and conditionally hide the navigation bar on specific routes
      this.showNavBar = !['/login', '/register', '/register2'].includes(to.path);
    },
  }
};



// JavaScript with Google Maps API integration
function openModal() {
  document.getElementById('myModal').style.display = "block";
  document.body.classList.add('modal-open');
  document.getElementById('postalInput').focus(); // Auto-focus on input field
}

function closeModal() {
  document.getElementById('myModal').style.display = "none";
  document.body.classList.remove('modal-open');
  document.getElementById('modalOpenBtn').focus(); // Move focus back to the button
}

function getFromAPI() {
  var postalCode = document.getElementById('postalInput').value;
  // Google Maps Postal code lookup api request here Eg:
  // var apiRequest = 'http://maps.googleapis.com/maps/api/geocode/json?address='+postalCode+'&sensor=true';
  closeModal(); // Close modal after API call
}




</script>