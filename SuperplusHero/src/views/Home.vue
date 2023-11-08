<style scoped>

.coolbox {
    display: flex;
    align-items: center;
    justify-content: center;
    /* height: 100vh; */
}
.box {
    flex: 1;
    display: flex;
    flex-direction: column; 
    justify-content: center;
    align-items: center;
    text-align: center;
}

.type, .type1 {
    overflow: hidden;
    white-space: nowrap;
    border-right: .15em solid black;
    max-width: 100%;
    width: 0ch;
    font-size: 3vw; /* Responsive text size */
    animation-name: typing, blink-caret;
    animation-duration: 3.5s, 3.5s;
    animation-fill-mode: forwards;
}
.type[data-text="Welcome to SurplusHero!"] {
    animation-duration: 3s, 3s;
}
.type1[data-text="Your go-to for cheap groceries"] {
    animation-duration: 4s, 4s;
}

/* The typing effect */
@keyframes typing {
    from { width: 0ch; }
    to { width: 27ch; }
}

/* The typewriter cursor effect */
@keyframes blink-caret {
    0%, 100% {
        border-color: transparent;
    }
    50% {
        border-color: black;
    }
    100% {
        border-width: 0;
    }
}



#homeImg{
    max-width: 100%; /* This makes the image responsive */
    align-self: center; /* This centers the image in the div */
}


.carousel-item .card {
    height: 100%;
}

button.carousel-control-prev,
button.carousel-control-next {
    width: 9%;
} 

.card button {
    outline: 0;
    padding: 12px;
    /* color: white; */
    /* background-color: #000000; */
    text-align: center;
    cursor: pointer;
    width: 100%;
    font-size: 18px;
}

.repBtn{
    width:fit-content;
}

.content{
    margin-top: 100px;
}

.card-img-top {
    width: 100%;
    height: 100%;
    object-fit: cover;
}


</style>


<template>


        <div class="content container coolbox">
    <div class="box">
        <img src="../assets/appLogo.png" alt="Logo of SurplusHero" id="homeImg"/>
    </div>
    <div class="box typewriter">
        <h2 class="type" data-text="Welcome to SurplusHero!">Welcome to SurplusHero!</h2>
        <h2 class="type1" data-text="Your go-to for cheap groceries"> Your go-to for <span class="text-success">cheap groceries</span></h2>
    </div>
</div>
<!-- Maybe money saved can be a pie chart or dashboard showing how much money saved so far and what type of good it was spent on -->
        <!-- <div class="container">
            <div class="row row-cols-1 row-cols-md-3 g-4">
                <div class="col mt-5">
                    <div class="card h-100">
                    <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" class="card-img-top" alt="...">
                        <div class="card-body">
                            <h5 class="card-title">Money Saved</h5>
                            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                        </div>
                    </div>
                </div> -->
                <!-- <div class="col">
                    <div class="card h-100">
                        <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                        <div class="card-body">
                            <h5 class="card-title">Viewed Recipes</h5>
                            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                        </div>
                    </div>
                </div> -->

                <!-- <div class="col mt-5">
                    <div class="card mb-3">
                        <div class="row g-0">
                            <div class="col-md-4">
                            <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" class="img-fluid rounded-start" style="">
                            </div>
                            <div class="col-md-6">
                                <div class="card-body">
                                    <h5 class="card-title">Viewed Recipes</h5>
                                    <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                                </div>
                            </div>
                        </div>
                    </div>

                </div> -->

                <!-- <div class="col">
                    <div class="card h-100">
                    <img src="..." class="card-img-top" alt="...">
                        <div class="card-body">
                            <h5 class="card-title">Notifications</h5>
                            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content.</p>
                        </div>
                    </div>
                </div> -->
<!--                 
            </div>
        </div> -->



    <!-- BS carousel: start -->
    <!-- Carousel title Produce -->
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-1"></div>
            <div class="col-md-2"><h2>Deals of the day!</h2></div>
            </div>
    </div>

        <div id="surplusCaro" class="carousel carousel-dark slide" >
                <div class="carousel-inner">
    
                    <div class="carousel-item active">
                        <div class="container-fluid">
    
                            <div class="row">
                                
                                <div class="col-md-1"></div>
                                    <div class="col-md-2 mb-3" v-for="(item, index) in items" :key="index">
                                            <div class="card">
                                                <img :src="item.ImageURL" class="card-img-top" alt="Surplus Listing"  style="width:100%">
                                                <h1>{{item.IngredientName}}</h1>
                                                <p class="price"> <s>{{ item.OriginalPrice }}</s><strong class="ms-2 text-danger">{{ item.SalePrice }}</strong></p>
                                                <!-- <p>Some text about the product</p> -->
                                                <p><button type="button" class="btn btn-primary" @click="addtoCart(item)">Add to Cart</button></p>    
                                            </div>
                                    </div>
                                <!-- <div class="ignore">
                                    
                                <div class="col-md-2 mb-3">
                                        <div class="card">
                                            <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                            <h1>Lettuce</h1>
                                            <p class="price"> <s>$61.99</s><strong class="ms-2 text-danger">$50.99</strong></p>
                                            <p>Some text about the product</p>
                                            <p><button type="button" class="btn btn-primary">Add to Cart</button></p>    
                                        </div>
                                </div>
                                <div class="col-md-2 mb-3">
                                        <div class="card">
                                            <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                            <h1>Lettuce</h1>
                                            <p class="price"> <s>$61.99</s><strong class="ms-2 text-danger">$50.99</strong></p>
                                            <p>Some text about the product</p>
                                            <p><button type="button" class="btn btn-primary">Add to Cart</button></p>    
                                        </div>
                                </div>
                                <div class="col-md-2 mb-3">
                                        <div class="card">
                                            <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                            <h1>Lettuce</h1>
                                            <p class="price"> <s>$61.99</s><strong class="ms-2 text-danger">$50.99</strong></p>
                                            <p>Some text about the product</p>
                                            <p><button type="button" class="btn btn-primary">Add to Cart</button></p>    
                                        </div>
                                </div>
                                <div class="col-md-2 mb-3">
                                        <div class="card">
                                            <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                            <h1>Lettuce</h1>
                                            <p class="price"> <s>$61.99</s><strong class="ms-2 text-danger">$50.99</strong></p>
                                            <p>Some text about the product</p>
                                            <p><button type="button" class="btn btn-primary">Add to Cart</button></p>    
                                        </div>
                                </div>
                                </div> -->
                                    
                                <div class="col-md-1"></div>
                            </div>
    
                        </div>
                    </div>
                    <!-- Next carousel item -->
                    <div class="carousel-item">
                        <div class="container-fluid">
    
                            <div class="row">
                                
                                <div class="col-md-1"></div>
                                <div class="col-md-2 mb-3" v-for="(item, index) in items" :key="index">
                                        <div class="card">
                                            <img :src="item.ImageURL" class="card-img-top" alt="Recipe" style="width:100%">
                                            <h1>{{item.IngredientName}}</h1>
                                            <p class="price"> <s>{{ item.OriginalPrice }}</s><strong class="ms-2 text-danger">{{ item.SalePrice }}</strong></p>
                                            <!-- <p>Some text about the product</p> -->
                                            <p><button type="button" class="btn btn-primary" @click="addtoCart(item)">Add to Cart</button></p>    
                                        </div>
                                </div>
                                <!-- <div class="ignore">
                                    
                                <div class="col-md-2 mb-3">
                                        <div class="card">
                                            <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                            <h1>Lettuce</h1>
                                            <p class="price"> <s>$61.99</s><strong class="ms-2 text-danger">$50.99</strong></p>
                                            <p>Some text about the product</p>
                                            <p><button type="button" class="btn btn-primary">Add to Cart</button></p>    
                                        </div>
                                </div>
                                <div class="col-md-2 mb-3">
                                        <div class="card">
                                            <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                            <h1>Lettuce</h1>
                                            <p class="price"> <s>$61.99</s><strong class="ms-2 text-danger">$50.99</strong></p>
                                            <p>Some text about the product</p>
                                            <p><button type="button" class="btn btn-primary">Add to Cart</button></p>    
                                        </div>
                                </div>
                                <div class="col-md-2 mb-3">
                                        <div class="card">
                                            <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                            <h1>Lettuce</h1>
                                            <p class="price"> <s>$61.99</s><strong class="ms-2 text-danger">$50.99</strong></p>
                                            <p>Some text about the product</p>
                                            <p><button type="button" class="btn btn-primary">Add to Cart</button></p>    
                                        </div>
                                </div>
                                <div class="col-md-2 mb-3">
                                        <div class="card">
                                            <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                            <h1>Lettuce</h1>
                                            <p class="price"> <s>$61.99</s><strong class="ms-2 text-danger">$50.99</strong></p>
                                            <p>Some text about the product</p>
                                            <p><button type="button" class="btn btn-primary">Add to Cart</button></p>    
                                        </div>
                                </div>
                                </div> -->
                                    
                                <div class="col-md-1"></div>
                            </div>
    
    
                        </div>
                    </div>
                </div>
                <!-- <a class="left carousel-control" href="#surplusCaro" role="button" data-slide="prev">
                    <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                    <span class="sr-only">Previous</span>
                </a>
                <a class="right carousel-control" href="#surplusCaro" role="button" data-slide="next">
                    <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                    <span class="sr-only">Next</span>
                </a> -->
    
                <button class="carousel-control-prev" type="button" data-bs-target="#surplusCaro" data-bs-slide="prev" >
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Previous</span>
                </button>
                <button class="carousel-control-next" type="button" data-bs-target="#surplusCaro" data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Next</span>
                </button>
        </div>


    <!-- Carousel title Recipe -->
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-1"></div>
            <div class="col-md-4"><h2>Check these recipes out!</h2></div>
            </div>
    </div>


        <div id="recipeCaro" class="carousel carousel-dark slide">
            <div class="carousel-inner">
                <div class="carousel-item active">
                    <div class="container-fluid">
    
                        <div class="row">
                            
                            <div class="col-md-1"></div>
                            <!-- <div class="col-md-2 mb-3">
                                    <div class="card">
                                        <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                        <h1>Chicken Rice</h1>
                                        <p>Some text about the recipe</p>
                                        <p><button type="button" class="btn btn-dark">Make!</button></p>    
                                    </div>
                            </div> -->
                            <div class="card text-center col-md-2 mb-3" data-bs-toggle="modal" data-bs-target="#repModal" role="button" tabindex="0" aria-label="Open information in a popup modal">
                                <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" class="card-img-top" alt="Card image cap">
                                    <div class="card-body">
                                        <h1 class="card-title">Chicken Rice</h1>
                                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                                    </div>
                                <p><button type="button" class="btn btn-dark">Click for more!</button></p>   
                            </div>

                            <div class="modal fade" id="repModal" tabindex="-1" aria-labelledby="myModalLabel" role="dialog">
                                    <div class="modal-dialog">
                                        <div class="modal-content">
                                            <div class="modal-header">
                                                <h5 class="modal-title fs-5" id="myModalLabel">Modal title</h5>
                                                <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close">
                                                </button>
                                            </div>
                                            <div class="modal-body">
                                                <p>Modal body text goes here.</p>
                                            </div>
                                            <div class="modal-footer">
                                                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                            </div>
                                        </div>
                                    </div>
                            </div>
                            
                            <div class="col-md-2 mb-3">
                                    <div class="card">
                                        <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                        <h1>Chicken Rice</h1>
                                        <p>Some text about the recipe</p>
                                        <p><button type="button" class="btn btn-dark">Make!</button></p>   
                                    </div>
                            </div>
                            <div class="col-md-2 mb-3">
                                    <div class="card">
                                        <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                        <h1>Chicken Rice</h1>
                                        <p>Some text about the recipe</p>
                                        <p><button type="button" class="btn btn-dark">Make!</button></p>    
                                    </div>
                            </div>
                            <div class="col-md-2 mb-3">
                                    <div class="card">
                                        <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                        <h1>Chicken Rice</h1>
                                        <p>Some text about the recipe</p>
                                        <p><button type="button" class="btn btn-dark">Make!</button></p>    
                                    </div>
                            </div>
                            <div class="col-md-2 mb-3">
                                    <div class="card">
                                        <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                        <h1>Chicken Rice</h1>
                                        <p>Some text about the recipe</p>
                                        <p><button type="button" class="btn btn-dark">Make!</button></p>    
                                    </div>
                            </div>
                            <div class="col-md-1"></div>
                        </div>
    
                    </div>
                </div>
                <!-- Next carousel item -->
                <div class="carousel-item">
                    <div class="container-fluid">
    
                        <div class="row">
                            <div class="col-md-1"></div>
                            <div class="col-md-2 mb-3">
                                    <div class="card">
                                        <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                        <h1>Chicken Rice</h1>
                                        <p>Some text about the recipe</p>
                                        <p><button type="button" class="btn btn-dark">Make!</button></p>    
                                    </div>
                            </div>
                            <div class="col-md-2 mb-3">
                                    <div class="card">
                                        <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                        <h1>Chicken Rice</h1>
                                        <p>Some text about the recipe</p>
                                        <p><button type="button" class="btn btn-dark">Make!</button></p>    
                                    </div>
                            </div>
                            <div class="col-md-2 mb-3">
                                    <div class="card">
                                        <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                        <h1>Chicken Rice</h1>
                                        <p>Some text about the recipe</p>
                                        <p><button type="button" class="btn btn-dark">Make!</button></p>    
                                    </div>
                            </div>
                            <div class="col-md-2 mb-3">
                                    <div class="card">
                                        <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                        <h1>Chicken Rice</h1>
                                        <p>Some text about the recipe</p>
                                        <p><button type="button" class="btn btn-dark">Make!</button></p> 
                                    </div>
                            </div>
                            <div class="col-md-2 mb-3">
                                    <div class="card">
                                        <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                        <h1>Chicken Rice</h1>
                                        <p>Some text about the recipe</p>
                                        <p><button type="button" class="btn btn-dark">Make!</button></p> 
                                    </div>
                            </div>
                            <div class="col-md-1"></div>
                        </div>
    
                    </div>
                </div>
            </div>
            <!-- <a class="left carousel-control" href="#surplusCaro" role="button" data-slide="prev">
                <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                <span class="sr-only">Previous</span>
            </a>
            <a class="right carousel-control" href="#surplusCaro" role="button" data-slide="next">
                <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                <span class="sr-only">Next</span>
            </a> -->
    
            <button class="carousel-control-prev" type="button" data-bs-target="#recipeCaro" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#recipeCaro" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
            </button>

        </div>
    <!-- BS carousel: end -->
    
</template>

<script>
import axios from 'axios';

import Cookies from 'js-cookie';
export default {
  data() {
    return {
      showNavBar: true, // Default to show the navigation bar
      notificationCount: 0,
      newNotifications: false,
      postalCode: "",
      location:"",
      
      items: [],
      cart: [],
      cartLength:0


    };
  },
  async created() {
        try {
            const response = await axios.get(`http://127.0.0.1:5000/listings`);
            this.items = response.data;    
            // console.log('All cookies:', Cookies.get());
        } catch(error) {
            console.error(error);
        }
    },

    methods: {
        addtoCart(item) {
            if (Cookies.get("cart")){
                this.cart = JSON.parse(Cookies.get("cart"));
                if (!this.checkDup(item)){
                    this.cart.push(item);
                    Cookies.set('cart',JSON.stringify(this.cart));
                    // console.log(JSON.parse(Cookies.get('cart')));
                    this.desiredQuantity[item.id] = 1;
                    Cookies.set('desiredQuantity', JSON.stringify(this.desiredQuantity));
                    this.cartLength++;
                }
            }

            
        },
        checkDup(item){
            if (this.cart.includes(item,0) ){
                console.log("Dup check");
                return true
            }else{
                return false;
            }
        }
        // getListings(){
        //     axios.get(`http://127.0.0.1:5000/listings`)
        //         .then(response => {
        //             console.log(response.data); // Handle success response
        //             this.ImageURL = response.data[2].ImageURL
        //             this.IngredientName = response.data[2].IngredientName
        //             this.OriginalPrice = response.data[2].OriginalPrice
        //             this.Quantity = response.data[2].Quantity
        //             this.SalePrice = response.data[2].SalePrice
        //         })
        //         .catch(error => {
        //             console.error('Error updating data:', error); // Handle error
        //         });
        // },
        // initAutocomplete() {
        //     let input = document.getElementById("autocomplete");
        //     let autocomplete = new google.maps.places.Autocomplete(input);
        //     this.location=autocomplete
        // },
        // useCurrentLocation() {
        //     if (!navigator.geolocation) {
        //     return;
        //     }

        //     navigator.geolocation.getCurrentPosition((position) => {
        //     const lat = position.coords.latitude;
        //     const lng = position.coords.longitude;
        //     console.log(lat);
        //     console.log(lng);
        //     const radius = '5000';
        //     const keyword = encodeURIComponent('NTUC');
        //     const key = "AIzaSyBiF8eEDh6HtoLGPrLnbNBfZQGbBNzNBN4";  
        //     console.log("working")   
        //     // axios.get(`https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=${lat},${lng}&radius=${radius}&type=${type}&key=${key}`)
        //     axios.get(`/api?location=${lat},${lng}&radius=${radius}&keyword=${keyword}&key=${key}`)
        //         .then(res => {
        //         if (res.data.results && res.data.results.length > 0) {
        //             this.location = res.data.results[0].vicinity;
                    
        //             }
        //         })
        //         .catch(err => {
        //             // console.error(err);
        //             console.error(err.message, err.response);
        //         });
        //     });
        // }, 
    },
}
</script>