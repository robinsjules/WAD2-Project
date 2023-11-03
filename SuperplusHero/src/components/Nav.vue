<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');

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
            <!-- Modal trigger -->
            <a 
            class="nav-link" 
            href="#"
            data-bs-toggle="modal"
            data-bs-target="#locationModal"
          >
            <img src="../assets/locationWhite.png" alt="Location Pin" width="50" height="50">
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


        </li>

        <li class="nav-item">
          <router-link to="/community"> <!-- Edit to Community Page, also apply to index.js router -->
            <a class="nav-link" href="#"><img src="../assets/communityWhite.png" alt="Community" width="50" height="50"></a>
          </router-link>
        </li>

        <li class="nav-item">
          <router-link to="/"> <!-- Edit to Cart Page, also apply to index.js router -->
            <a class="nav-link" href="#"><img src="../assets/cartWhite.png" alt="Cart" width="50" height="50"></a>
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/fridge"> <!-- Edit to Fridge Page, also apply to index.js router -->
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
      notificationCount: 0,
      newNotifications: false,
      postalCode: "",
      location:"",
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
  // initAutocomplete() {
  //       let input = document.getElementById("autocomplete");
  //       let autocomplete = new google.maps.places.Autocomplete(input);
  //       },
  //       useCurrentLocation() {
  //           if (!navigator.geolocation) {
  //           return;
  //           }

  //           navigator.geolocation.getCurrentPosition((position) => {
  //           const lat = position.coords.latitude;
  //           const lng = position.coords.longitude;
  //           const radius = '1000';
  //           const type = encodeURIComponent('NTUC');
  //           const key = "YOUR_GOOGLE_API_KEY";
            
  //           axios.get(`https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=${lat},${lng}&radius=${radius}&type=${type}&key=${key}`)
  //               .then(res => {
  //               if (res.data.results && res.data.results.length > 0) {
  //                   this.location = res.data.results[0].name;
  //               }
  //               })
  //               .catch(err => {
  //               console.error(err);
  //               });
  //           });
// },
  watch: {
    $route(to) {
      // Check the route and conditionally hide the navigation bar on specific routes
      this.showNavBar = !['/login', '/register', '/register2'].includes(to.path);
    },
  },
};

</script>