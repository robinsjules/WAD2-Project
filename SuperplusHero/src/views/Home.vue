<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap');
    body{
        background-color: rgb(237,243,235);
        font-family: 'Montserrat';
        min-height: 10vh;
    }
.text-custom {
    font-family: "Montserrat";
    }
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
    font-size: 3vw;
    animation-name: typing, blink-caret;
    animation-duration: 3.5s, 3.5s;
    animation-fill-mode: forwards;
    padding-bottom: 10px;
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
    padding: 5px;
    text-align: center;
    width: 90%;
    margin: 8px;
    font-size: 18px;
    background-color: rgb(10, 160, 10);
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
    border-radius: 20px;
    padding: 10px;
}


@media (min-width: 768px) {
    .btn-edit {
    padding: 16px 48px;
  }
}

.card-edit{
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    border: 2px solid #3F8256;
    background-color: rgb(237, 243, 235);
}

.shadow-text {
    color: #3498db;
    text-shadow: 2px 2px 7px rgba(0, 0, 0, 0.5);
}


.alert {
    text-align: center;

}

.overflow-text {
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        width: 100%;
        display: inline-block;
    }

.custom-link{
    color:rgb(10, 160, 10);
}
</style>


<template>

        <div class="content ">

            <div class="alert alert-success alert-dismissible fade show" role="alert" v-if="showCheckoutAlert == 'true'">
                <strong>You have successfully checked out!</strong>
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close" @click="reset()"></button>
            </div>

            <div class="container coolbox">

                <div class="box">
                    <img src="../assets/appLogo.png" alt="Logo of SurplusHero" id="homeImg"/>
                </div>
    
                <div class="box typewriter">
                    <h2 class="type" data-text="Welcome to SurplusHero!">Welcome to SurplusHero!</h2>
                    <h2 class="type1" data-text="Your go-to for cheap groceries"> Your go-to for <span class="text-success">cheap groceries</span></h2>
                </div>

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
            <div class="col-md-4"><h2 style="font-family:Montserrat">Deals of the day!</h2></div>
            </div>
    </div>

        <div id="surplusCaro" class="carousel carousel-dark slide" >
                <div class="carousel-inner">
    
                    <div class="carousel-item active">
                        <div class="container-fluid">
    
                            <div class="row">
                                
                                <div class="col-md-1"></div>
                                    <div class="col-md-2 mb-3" v-for="(item, index) in items.slice(0,5)" :key="index">
                                            <div class="card card-edit">
                                                <img :src="item.ImageURL" class="card-img-top" alt="Surplus Listing"  style="width:100%">
                                                <h3 style="font-family:Montserrat">&nbsp;{{item.IngredientName}}</h3>
                                                <p class="price">&nbsp; 
                                                    <s>${{ item.OriginalPrice }}</s>
                                                    <strong class="ms-2 text-danger shadow-text">${{ item.SalePrice }}</strong>
                                                </p>
                                                <!-- <p>Some text about the product</p> -->
                                                <p><button type="button" style="font-family:Montserrat;" class="btn btn-success" @click="addtoCart(item)">Add to Cart</button></p>    
                                            </div>
                                    </div>
                                    <div class="col-md-11"><h5 style="font-family:Montserrat; text-align:right;">Click <router-link :to="{ name: 'products' }" class="custom-link">here</router-link> for more deals!</h5></div>
                                <div class="col-md-1"></div>
                            </div>
    
                        </div>
                    </div>
                    <!-- Next carousel item -->
                    <div class="carousel-item">
                        <div class="container-fluid">
    
                            <div class="row">
                                
                                <div class="col-md-1"></div>
                                <div class="col-md-2 mb-3" v-for="(item, index) in items.slice(5,10)" :key="index">
                                        <div class="card card-edit">
                                            <img :src="item.ImageURL" class="card-img-top" alt="Recipe" style="width:100%">
                                            <h3 style="font-family:Montserrat">&nbsp;{{item.IngredientName}}</h3>
                                            <p class="price">&nbsp; 
                                                    <s>${{ item.OriginalPrice }}</s>
                                                    <strong class="ms-2 text-danger shadow-text">${{ item.SalePrice }}</strong>
                                            </p>
                                            <!-- <p>Some text about the product</p> -->
                                            <p><button type="button" style="font-family:Montserrat;" class="btn btn-success" @click="addtoCart(item)">Add to Cart</button></p>    
                                        </div>
                                </div>
                                    
                                <div class="col-md-1"></div>
                            </div>
    
    
                        </div>
                    </div>
                </div>
    
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
                <div class="col-md-5"><h2 style="font-family:Montserrat">Check these recipes out!</h2></div>
            </div>
    </div>


        <div id="recipeCaro" class="carousel carousel-dark slide">
            <div class="carousel-inner">
                <div class="carousel-item active">
                    <div class="container-fluid">
    
                        <div class="row">
                            
                            <div class="col-md-1"></div>
                            <div class="col-md-2 mb-3">
                                    <div class="card card-edit">
                                        <img src="https://spoonacular.com/recipeImages/646512-312x231.jpg   " alt="Recipe" style="width:100%">
                                        <h1>Salmon Caesar Salad</h1>
                                        <p class="overflow-text">The recipe Salmon Caesar Salad could satisfy your American craving in roughly 45 minutes. One portion of this dish contains around 27g of protein, 29g of fat, and a total of 393 calories. 
                                            For $3.01 per serving, you get a main course that serves 2. It is brought to you by Foodista. 12 people were glad they tried this recipe. Head to the store and pick up parmesan cheese, lemon juice, paprika, and a few other things to make it today. It is a good option if you're following a gluten free, primal, pescatarian, and ketogenic diet.</p>
                                            <button type="button" class="btn btn-success"  @click="gotoRec()">Find out More!</button>    
                                    </div>
                            </div>
                            <!-- <div class="card card-edit text-center col-md-2 mb-3" data-bs-toggle="modal" data-bs-target="#repModal" role="button" tabindex="0" aria-label="Open information in a popup modal">
                                <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" class="card-img-top" alt="Card image cap">
                                    <div class="card-body">
                                        <h2 class="card-title">Chicken Rice</h2>
                                        <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                                    </div>
                                <p><button type="button" class="btn btn-success">Click for more!</button></p>   
                            </div> -->

                            <!-- <div class="modal fade" id="repModal" tabindex="-1" aria-labelledby="myModalLabel" role="dialog">
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
                            </div> -->
                            
                            <div class="col-md-2 mb-3">
                                <div class="card card-edit">
                                        <img src="https://spoonacular.com/recipeImages/918033-312x231.jpg" alt="Recipe" style="width:100%">
                                        <h1>Chicken Spring Rolls</h1>
                                        <p class="overflow-text">Need a gluten free and dairy free hor d'oeuvre? 
                                            Chicken Spring Rolls could be an outstanding recipe to try. One serving contains 337 calories, 28g of protein, and 11g of fat. 
                                            This recipe serves 4. For $2.08 per serving, this recipe covers 23% of your daily requirements of vitamins and minerals. 
                                            If you have rice paper wrappers, garlic clove, rice wine vinegar, and a few other ingredients on hand, you can make it. 
                                            1 person were impressed by this recipe. From preparation to the plate, this recipe takes about 45 minutes. </p>
                                        
                                            <p>
                                                <button type="button" class="btn btn-success" @click="gotoRec()">Find out More!</button>
                                            </p>    
                                </div>
                            </div>
                            <div class="col-md-2 mb-3">
                                <div class="card card-edit">
                                        <img src="https://spoonacular.com/recipeImages/715567-312x231.jpg" alt="Recipe" style="width:100%">
                                        <h2>Beef Fajita Marinade</h2>
                                        <p class="overflow-text">Beef Fajita Marinade takes about 45 minutes from beginning to end. 
                                            This gluten free, dairy free, paleolithic, and primal recipe serves 2 and costs $8.91 per serving. 
                                            One serving contains 677 calories, 75g of protein, and 40g of fat. This recipe from Pink When has 21 fans. 
                                            It works well as a marinade. Head to the store and pick up cilantro, lime zest, lime juice, and a few other things to make it today. </p>
                                        <br/>
                                            <p>
                                                <button type="button" class="btn btn-success" @click="gotoRec()">Find out More!</button>
                                            </p>    
                                </div>
                            </div>
                            <div class="col-md-2 mb-3">
                                <div class="card card-edit">
                                        <img src="https://spoonacular.com/recipeImages/715438-312x231.jpg" alt="Recipe" style="width:100%">
                                        <h1>Mexican Casserole</h1>
                                        <p class="overflow-text">The recipe Mexican Casserole could satisfy your Mexican craving in about 1 hour and 5 minutes. 
                                            This main course has 581 calories, 48g of protein, and 21g of fat per serving. 
                                            This recipe serves 6 and costs $2.63 per serving. It is brought to you by Pink When. 503 people were impressed by this recipe.
                                             It will be a hit at your Autumn event. A mixture of cheddar cheese, monterrey jack, salsa, and a handful of other ingredients are all it takes to make this recipe so scrumptious. It is a good option if you're following a gluten free diet </p>
                                        
                                            <p>
                                                <button type="button" class="btn btn-success" @click="gotoRec()">Find out More!</button>
                                            </p>    
                                </div>
                            </div>
                            <div class="col-md-2 mb-3">
                                <div class="card card-edit">
                                        <img src="https://spoonacular.com/recipeImages/664828-312x231.jpg" alt="Recipe" style="width:100%">
                                        <h1>Vietnamese Banh Mi</h1>
                                        <p class="overflow-text">Vietnamese Banh Mi is a dairy free recipe with 6 servings. 
                                            One portion of this dish contains around 24g of protein, 21g of fat, and a total of 477 calories. For $1.86 per serving, this recipe covers 17% of your daily 
                                            requirements of vitamins and minerals. 3 people found this recipe to be delicious and satisfying. t is a rather inexpensive recipe for fans of Vietnamese food. 
                                            From preparation to the plate, this recipe takes around 45 minutes. </p>
                                            <p>
                                                <button type="button" class="btn btn-success" @click="gotoRec()">Find out More!</button>
                                            </p>    
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
                                    <div class="card card-edit">
                                        <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                        <h1>Chicken Rice</h1>
                                        <p>Some text about the recipe</p>
                                        <p><button type="button" class="btn btn-success">Make!</button></p>    
                                    </div>
                            </div>
                            <div class="col-md-2 mb-3">
                                    <div class="card card-edit">
                                        <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                        <h1>Chicken Rice</h1>
                                        <p>Some text about the recipe</p>
                                        <p><button type="button" class="btn btn-success">Make!</button></p>    
                                    </div>
                            </div>
                            <div class="col-md-2 mb-3">
                                    <div class="card card-edit">
                                        <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                        <h1>Chicken Rice</h1>
                                        <p>Some text about the recipe</p>
                                        <p><button type="button" class="btn btn-success">Make!</button></p>    
                                    </div>
                            </div>
                            <div class="col-md-2 mb-3">
                                    <div class="card card-edit">
                                        <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                        <h1>Chicken Rice</h1>
                                        <p>Some text about the recipe</p>
                                        <p><button type="button" class="btn btn-success">Make!</button></p> 
                                    </div>
                            </div>
                            <div class="col-md-2 mb-3">
                                    <div class="card card-edit">
                                        <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                        <h1>Chicken Rice</h1>
                                        <p>Some text about the recipe</p>
                                        <p><button type="button" class="btn btn-success">Make!</button></p> 
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
        desiredQuantity: {},
        items: [],
        cart: [],
        cartLength:0,
        showCheckoutAlert: false,
        modal: null


    };
  },
  async created() {
        try {
            const response = await axios.get(`http://127.0.0.1:5000/listings`);
            this.items = response.data;    
            // console.log('All cookies:', Cookies.get());
            if (Cookies.get("showCheckoutAlert")){
                this.showCheckoutAlert = Cookies.get('showCheckoutAlert');
                // console.log(this.showCheckoutAlert);
                if (this.showCheckoutAlert) {
                    
                    Cookies.remove("totalPrice");
                    Cookies.set('showCheckoutAlert', false);
                }
            }

            if (Cookies.get("cart")){
                this.cart = JSON.parse(Cookies.get("cart"));
            }

            if (Cookies.get("cartLength")){
                this.cartLength = Cookies.get("cartLength");
            }else{
                this.cartLength=0;
            }
        } catch(error) {
            console.error(error);
        }
    },

    methods: {
        gotoRec() {
            this.$router.push({ name: 'readRecipe', params: { id: "Salmon Caesar Salad" } });
        },
        reset() {
            this.showCheckoutAlert = false;
            console.log(this.showCheckoutAlert);
        },
        addtoCart(item) {
            if (Cookies.get("cart")){
                this.cart = JSON.parse(Cookies.get("cart"));
                this.cartLength = Cookies.get("cartLength");
                if (!this.checkDup(item)){
                    
                    this.cart.push(item);
                    Cookies.set('cart',JSON.stringify(this.cart));
                    // console.log(JSON.parse(Cookies.get('cart')));
                    this.desiredQuantity[item.id] = 1;
                    Cookies.set('desiredQuantity', JSON.stringify(this.desiredQuantity));
                    this.cartLength++;
                    Cookies.set('cartLength', this.cartLength);
                    // console.log("notaddcart");
                }
            }else{
                if (!this.checkDup(item)){
                    this.cart.push(item);
                    Cookies.set('cart',JSON.stringify(this.cart));
                    // console.log(JSON.parse(Cookies.get('cart')));
                    this.desiredQuantity[item.id] = 1;
                    Cookies.set('desiredQuantity', JSON.stringify(this.desiredQuantity));
                    this.cartLength++;
                    Cookies.set('cartLength', this.cartLength);
                    // console.log("notaddcart");
                }
            }

            
        },
        checkDup(item){
  // Check if the `cart` array has an object with the same `id` as `item`
            if (this.cart.some(cartItem => cartItem.id === item.id)){
                // console.log("Dup check");
                return true
            }else{
                // console.log("not dup");
                return false;
            }
        },

    },

}





</script>