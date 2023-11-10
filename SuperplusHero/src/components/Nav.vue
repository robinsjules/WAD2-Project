<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');

.navbar-nav{
    margin-left: auto;
}

.template{
  font-family: 'Montserrat', sans-serif;
}

.navbar-dark.navcolor {
  /* background-color: black;  */
  position: fixed;
  width: 100%;
  z-index: 1000;
  top: 0;
  left: 0;
  right: 0;
  height: 85px;
}

.navbar-brand img {
  margin-left: 10px;
}

.nav-link img {
    margin-left: 20px;
}

</style>

<style scoped>

.cart-item {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
  flex: 1; 
}

.cartThumbnail {
  margin-right: 10px;
  width: 20%;
  height: 20%;
}

/* .cart-item-details {
  display: flex;
  flex-direction: column;
  align-items: start;
} */



.checkout {
  text-align: right;
}

.remove{
  justify-content: right;
  align-items: center;
  margin-left: auto;
}

.itemCost{
  margin-left:auto;
}



.cartItemActions {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.color-coord{
  background-color: rgb(10, 160, 10);
}

</style>

<template>
<nav v-if="showNavBar" class="navbar navbar-expand-md navbar-dark bg-dark navcolor">
    <router-link to="/home">
        <a class="navbar-brand" href="#"><img src="../assets/appLogoForNav.png" alt="Logo" height="60"></a>
    </router-link>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
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
            data-bs-target="#locationModal"
          >
            <img src="../assets/locationWhite.png" alt="Location Pin" width="40" height="40">
          </a>
            

        </li>

                <li class="nav-item">
                  <router-link to="/products"> <!-- Edit to Community Page, also apply to index.js router -->
            <a class="nav-link" href="#">
            <img src="../assets/broccoli.png" alt="products" width="40" height="40">
          </a>
          </router-link>
            

        </li>

        <li class="nav-item">
          <router-link to="/community"> <!-- Edit to Community Page, also apply to index.js router -->
            <a class="nav-link" href="#">
            
            <img src="../assets/communityWhite.png" alt="Community" width="40" height="40">
          
          </a>

          </router-link>
        </li>

        <li class="nav-item">
          <router-link to="/"> <!-- Edit to Cart Page, also apply to index.js router -->
            <a class="nav-link" href="#"
            data-bs-toggle="modal"
            data-bs-target="#cartModal"
            @click="checkCart()"
            >


            
            
            <img src="../assets/cartWhite.png" alt="Cart" width="35" height="35">
            <span class="badge bg-danger" v-if="cartLength > 0 " role="alert">{{ cartLength }}</span>
            <i class="bi bi-bell"></i>
          
          </a>
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/fridge"> <!-- Edit to Fridge Page, also apply to index.js router -->
            <a class="nav-link" href="#"><img src="../assets/fridgeWhite.png" alt="Fridge" width="35" height="35"></a>
          </router-link>
        </li>
        <li class="nav-item">
          <router-link to="/profile">
            <a class="nav-link" href="#"><img src="../assets/profileWhite.png" alt="Profile" width="35" height="35"></a>
          </router-link>
        </li>
      </ul>
      </div>
  </nav>
  <div class="modal fade" id="locationModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title" id="exampleModalLabel">Enter desired NTUC</h5>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                  <input 
                    id="autocomplete" 
                    class="form-control" 
                    type="text" 
                    placeholder="Enter a location" 
                    v-model="location"
                  >
                  <p class="text-help mt-2">- OR -</p>
                  <button 
                    class="btn mt-2 btn-success color-coord" 
                    @click="useCurrentLocation"
                  >
                    Get the closest NTUC
                  </button>
                </div>
              </div>
            </div>
          </div>


          <div class="modal fade" id="cartModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
              <div class="modal-content">
                <div class="modal-header">
                  <h5 class="modal-title" id="exampleModalLabel">Shopping Cart</h5>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                  <span v-if="checkCart() == []">There's nothing in your cart!</span>
                  <div v-for="(item, idx) in cart" :key="idx" class="cart-item">
                    <img :src="item.ImageURL" alt="Surplus Listing" class="cartThumbnail">
                    <div class="cart-item-details">
                        <h3 class="cartItemName">{{item.IngredientName}}</h3>
                        <span class="price"> Price: $<s>{{ item.OriginalPrice }}</s><strong class="ms-2 text-danger"> ${{ item.SalePrice }}</strong></span>
    
                          <div class="cartItemQuantity">
                            Quantity: 
                              <button class="btn btn-success color-coord" @click="decreaseQuantity(item)"  :disabled="desiredQuantity[item.id] <= 1" >-</button>
                              {{desiredQuantity[item.id] || 1}} 
                              <!-- If item id exists in desiered quantity object set value to 1 if not go next -->
                              <button class="btn btn-success color-coord" @click="increaseQuantity(item)" :disabled="desiredQuantity[item.id] >= item.Quantity">+</button>
                              
                              
                              <div class="cartItemStock">
                                Stock Available: {{ item.Quantity }}
                                Item Cost: ${{ itemTotalPrice[item.id] }}
                              </div>
                              

                          </div>

                          
                          
                        </div>
                        <button class="btn btn-success color-coord remove" @click="removeFromCart(item)">X</button>
                        
                      <hr>
                    </div>
                    <div class="test" v-if="totalPrice > 0">

                      <div class="totalPrice" >
                        Total Cost: ${{ totalPrice }}
                      </div>
                      <router-link to="/checkout">
                        <button class="btn btn-success color-coord checkout" data-bs-dismiss="modal">Checkout</button>
                      </router-link>

                    </div>
                </div>
              </div>
            </div>
          </div>
  



</template>

<script>
import axios from 'axios';
import Cookies from 'js-cookie';
export default {
  data() {
    return {
      showNavBar: true, // Default to show the navigation bar
      // notificationCount: 0,
      // newNotifications: false,
      postalCode: "",
      location:"",
      desiredQuantity: {},
      itemTotalPrice: {},
      totalPrice:0.0,
      cart:[],
      newCartItem: false,
      cartLength: 0,
      showCheckoutAlert: false,
    };
  },
  async created() {
      this.checkCookies();
      this.checkCart();
      this.checkCartLength(); 
      if (Cookies.get('desiredQuantity')) {
        this.desiredQuantity = JSON.parse(Cookies.get('desiredQuantity'));
      }
      this.newCartItem = false;
      this.cartLength = setInterval(() => {
        this.checkCartLength();
      }, 500);
      // this.totalPrice = this.desiredQuantity.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
      this.totalPrice = this.calcTotal(this.itemTotalPrice);

      this.showCheckoutAlert = setInterval(() => {
        this.checkedOut();
      },500);



      

    },

    computed: { 
      // cartLength() {
      //   return this.cart.length;
      // }
    },
  methods: {

    checkedOut(){
        this.showCheckoutAlert = Cookies.get("showCheckoutAlert")
        if (this.showCheckoutAlert == "true" ){
          // console.log(this.showCheckoutAlert);
          // console.log(this.totalPrice);
          this.totalPrice = 0;
          Cookies.remove("totalPrice");
          Cookies.set("showCheckoutAlert", false);
        }
    },
    calcTotal(obj){
      let sum = Object.values(obj).reduce((a, b) => parseFloat(a) + parseFloat(b), 0);
      return parseFloat(sum.toFixed(2)); 
    },
    removeFromCart(item) {
      
      const index = this.cart.findIndex(cartItem => cartItem.id === item.id); // Calls the findIndex method on every item (we call cartItem) Check if the item in cart matches the item being sent from remove item
      if (index !== -1) {
        this.cart.splice(index, 1);
        Cookies.set('cart', JSON.stringify(this.cart));
        if (this.desiredQuantity[item.id]) {
          delete this.desiredQuantity[item.id];
          delete this.itemTotalPrice[item.id];  
          Cookies.set('desiredQuantity', JSON.stringify(this.desiredQuantity)); // Update cookies
      }

      if (Cookies.get("itemTotalPrice")){
        // this.calcTotal(Cookies.get("itemTotalPrice"));
        this.totalPrice = this.calcTotal(Cookies.get("itemTotalPrice"));
        // console.log(this.totalPrice);
      }else{
        this.totalPrice = 0.0;
      }
    }
  },
    checkCartLength(){
      if (Cookies.get("cartLength")){
        // console.log(Cookies.get('cartLength'));
        this.cartLength = Cookies.get('cartLength');
      }else{
        this.cartLength=0;
      }
    },
    checkCookies(){
      if (Cookies.get('location')){
        this.location = Cookies.get("location");
      }else{
        this.location = "";
      }
      if (Cookies.get("totalPrice")){
        this.totalPrice=Cookies.get("totalPrice");
      }else{

      }
    },
    checkCart(){
      if (Cookies.get("cart")){
          this.cart = JSON.parse(Cookies.get("cart"));
          // console.log("not checkcartnav");
          if(Cookies.get('desiredQuantity')){
            this.desiredQuantity = JSON.parse(Cookies.get('desiredQuantity'));
          }

          for (let item of this.cart) {
            if(this.desiredQuantity[item.id] === undefined){
              this.desiredQuantity[item.id] = 1;
            }
            this.calculateItemTotal(item);
          }
          this.totalPrice = this.calcTotal(this.itemTotalPrice);  
          Cookies.set("totalPrice", this.totalPrice);
          this.showCheckoutAlert = Cookies.get("showCheckoutAlert")
          if (this.showCheckoutAlert == "true" ){
            // console.log('WORKING');
            this.totalPrice=this.calc(this.itemTotalPrice);
            Cookies.set("totalPrice",0);
          }


      }else{
        this.cart = [];
      }
    },
    increaseQuantity(item) {
      if (!this.desiredQuantity[item.id]) {
        this.desiredQuantity[item.id] = 1;
      } else {
        if(item.Quantity > this.desiredQuantity[item.id]){
          this.desiredQuantity[item.id]++;
        }
      }
      Cookies.set('desiredQuantity', JSON.stringify(this.desiredQuantity));
      this.calculateItemTotal(item);
      this.totalPrice = this.calcTotal(this.itemTotalPrice);
      Cookies.set("itemTotalPrice", this.itemTotalPrice);
      Cookies.set("totalPrice", this.totalprice);
    },
    decreaseQuantity(item) {
      if (!this.desiredQuantity[item.id] || this.desiredQuantity[item.id] <= 1) {
        this.desiredQuantity[item.id] = 1;
      } else {
        this.desiredQuantity[item.id]--;
      }
      Cookies.set('desiredQuantity', JSON.stringify(this.desiredQuantity));
      this.calculateItemTotal(item);
      this.totalPrice = this.calcTotal(this.itemTotalPrice);
      Cookies.set("itemTotalPrice", this.itemTotalPrice);
      Cookies.set("totalPrice", this.totalprice);

      
    },
    calculateItemTotal(item){
      let calc = this.desiredQuantity[item.id] * item.SalePrice
      this.itemTotalPrice[item.id] = parseFloat(calc.toFixed(2)); 
    },
    setLocationCookie() { 
      Cookies.set('location', this.location);
    },
      useCurrentLocation() {
          if (!navigator.geolocation) {
            return;
          }

          navigator.geolocation.getCurrentPosition((position) => {
          var lat = position.coords.latitude;
          var lng = position.coords.longitude;
          // console.log(lat);
          // console.log(lng);
          const radius = '5000';
          const keyword = encodeURIComponent('NTUC');
          const key = "AIzaSyBiF8eEDh6HtoLGPrLnbNBfZQGbBNzNBN4";  
          // console.log("working")   
          // axios.get(`https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=${lat},${lng}&radius=${radius}&type=${type}&key=${key}`)
          axios.get(`/api?location=${lat},${lng}&radius=${radius}&keyword=${keyword}&key=${key}`)
              .then(res => {
              if (res.data.results && res.data.results.length > 0) {
                  // this.location = res.data.results[0].vicinity;
                  lat = res.data.results[0].geometry.location.lat
                  lng = res.data.results[0].geometry.location.lng
                  // this.setLocationCookie();
                  Cookies.set('location', this.location);
                  }

                  axios.get(`https://maps.googleapis.com/maps/api/geocode/json?latlng=${lat},${lng}&key=${key}`)
                    .then(res => {
                    if (res.data.results && res.data.results.length > 0) {
                      for (let i = 0; i < res.data.results[0].address_components.length; i++) {
                        if (res.data.results[0].address_components[i].types.indexOf('postal_code') !== -1) {
                          this.location = res.data.results[0].address_components[i].short_name;
                          break;
                        }
                      }
                      // this.location = postalCode;
                      Cookies.set('location', this.location);
                    }
                    })
                    .catch(err => {
                        console.error(err.message, err.response);
                    });

              })
              .catch(err => {
                  // console.error(err);
                  console.error(err.message, err.response);
              });

          });
      }, 
  },
  watch: {
    $route(to) {
      // Check the route and conditionally hide the navigation bar on specific routes
      this.showNavBar = !['/login', '/', '/register2'].includes(to.path);
    },
    location(newLocation) { 
      // Set the cookie when location gets updated
      this.setLocationCookie();
    },
    cart: function (newVal, oldVal) {
      this.cartLength = newVal.length;
      Cookies.set('cartLength', JSON.stringify(this.cartLength));
    },
  },
};

</script>