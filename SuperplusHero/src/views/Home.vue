<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap');

* {
    font-family: 'Montserrat';
}

body {
    background-color: rgb(237, 243, 235);
    font-family: 'Montserrat';
    min-height: 10vh;
}

h2 {
    font-weight: bold;

}

h5 {
    padding: 10px;
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

.type,
.type1 {
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
    from {
        width: 0ch;
    }

    to {
        width: 27ch;
    }
}

/* The typewriter cursor effect */
@keyframes blink-caret {

    0%,
    100% {
        border-color: transparent;
    }

    50% {
        border-color: black;
    }

    100% {
        border-width: 0;
    }
}



#homeImg {
    max-width: 100%;
    /* This makes the image responsive */
    align-self: center;
    /* This centers the image in the div */
}


.carousel-item .card {
    height: 100%;
}

button.carousel-control-prev,
button.carousel-control-next {
    width: 9%;
}

.card button {
    text-align: center;
    width: 90%;
    margin: 8px;
    /* font-size: 18px; */
    background-color: rgb(10, 160, 10);
}

.card button:hover {
    text-align: center;
    width: 90%;
    margin: 8px;
    /* font-size: 18px; */
    background-color: gray;
}

.repBtn {
    width: fit-content;
}

.content {
    margin-top: 100px;
}

/* .card-img-top {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 20px;
    padding: 10px;
} */


/* @media (min-width: 768px) {
    .btn-edit {
        padding: 16px 48px;
    }
} */

.card-edit {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    border: 1px solid #3F8256;
    background-color: rgb(237, 243, 235);
}

.shadow-text {
    color: #3498db;
    text-shadow: 2px 2px 7px rgba(0, 0, 0, 0.5);
}


.alert {
    text-align: center;

}

.custom-link {
    color: rgb(10, 160, 10);
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
                <img src="../assets/appLogo.png" alt="Logo of SurplusHero" id="homeImg" />
            </div>

            <div class="box typewriter">
                <h2 class="type" data-text="Welcome to SurplusHero!">Welcome to SurplusHero!</h2>
                <h2 class="type1" data-text="Your go-to for cheap groceries"> Your go-to for <span
                        style="color:rgb(10, 160, 10);">cheap groceries</span></h2>
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
                </div>
            </div>
        </div> -->



    <!-- Carousel title Recipe -->
    <div class="container-fluid">
        <div class="row" style="padding-top:30px;">
            <div class="col-md-1"></div>
            <div class="col-md-4">
                <h2>Explore recipes</h2>
            </div>
            <div class="col-md-6">
                <h5 style="padding:0px; text-align:right; transform:translateY(50%);"><router-link
                        :to="{ name: 'AllRecipes' }" class="custom-link">View all</router-link></h5>
            </div>
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
                                <img src="https://spoonacular.com/recipeImages/646512-312x231.jpg" alt="Recipe"
                                    style="width:100%; height:180px;">
                                <h5>Salmon Caesar Salad</h5>
                                <div class="mt-auto">
                                    <button type="button" class="btn btn-success" @click="gotoRec()">Read More</button>
                                </div>
                            </div>
                        </div>

                        <div class="col-md-2 mb-3">
                            <div class="card card-edit">
                                <img src="https://spoonacular.com/recipeImages/918033-312x231.jpg" alt="Recipe"
                                    style="width:100%; height:180px;">
                                <h5>Chicken Spring Rolls</h5>
                                <div class="mt-auto">
                                    <button type="button" class="btn btn-success" @click="gotoRec()">Read More</button>
                                </div>
                            </div>
                        </div>

                        <div class="col-md-2 mb-3">
                            <div class="card card-edit">
                                <img src="https://spoonacular.com/recipeImages/715567-312x231.jpg" alt="Recipe"
                                    style="width:100%; height:180px;">
                                <h5>Beef Fajita Marinade</h5>
                                <div class="mt-auto">
                                    <button type="button" class="btn btn-success" @click="gotoRec()">Read More</button>
                                </div>
                            </div>
                        </div>

                        <div class="col-md-2 mb-3">
                            <div class="card card-edit">
                                <img src="https://spoonacular.com/recipeImages/715438-312x231.jpg" alt="Recipe"
                                    style="width:100%; height:180px;">
                                <h5>Mexican Casserole</h5>

                                <div class="mt-auto">
                                    <button type="button" class="btn btn-success" @click="gotoRec()">Read More</button>
                                </div>
                            </div>
                        </div>

                        <div class="col-md-2 mb-3">
                            <div class="card card-edit">
                                <img src="https://spoonacular.com/recipeImages/664828-312x231.jpg" alt="Recipe"
                                    style="width:100%; height:180px;">
                                <h5>Vietnamese Banh Mi</h5>

                                <div class="mt-auto">
                                    <button type="button" class="btn btn-success" @click="gotoRec()">Read More</button>
                                </div>
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
                                <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg"
                                    alt="Recipe" style="width:100%">
                                <h1>Chicken Rice</h1>
                                <p>Some text about the recipe</p>
                                <p><button type="button" class="btn btn-success">Make!</button></p>
                            </div>
                        </div>
                        <div class="col-md-2 mb-3">
                            <div class="card card-edit">
                                <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg"
                                    alt="Recipe" style="width:100%">
                                <h1>Chicken Rice</h1>
                                <p>Some text about the recipe</p>
                                <p><button type="button" class="btn btn-success">Make!</button></p>
                            </div>
                        </div>
                        <div class="col-md-2 mb-3">
                            <div class="card card-edit">
                                <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg"
                                    alt="Recipe" style="width:100%">
                                <h1>Chicken Rice</h1>
                                <p>Some text about the recipe</p>
                                <p><button type="button" class="btn btn-success">Make!</button></p>
                            </div>
                        </div>
                        <div class="col-md-2 mb-3">
                            <div class="card card-edit">
                                <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg"
                                    alt="Recipe" style="width:100%">
                                <h1>Chicken Rice</h1>
                                <p>Some text about the recipe</p>
                                <p><button type="button" class="btn btn-success">Make!</button></p>
                            </div>
                        </div>
                        <div class="col-md-2 mb-3">
                            <div class="card card-edit">
                                <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg"
                                    alt="Recipe" style="width:100%">
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


        <button class="carousel-control-prev" type="button" data-bs-target="#recipeCaro" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#recipeCaro" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
        </button>

    </div>



    <!-- BS carousel: start -->
    <!-- Carousel title Produce -->
    <div class="container-fluid">
        <div class="row" style="padding-top:30px;">
            <div class="col-md-1"></div>
            <div class="col-md-4">
                <h2>Featured deals</h2>
            </div>
            <div class="col-md-6">
                <h5 style="transform:translateY(50%); padding:0px; text-align:right;"><router-link
                        :to="{ name: 'products' }" class="custom-link">View all</router-link></h5>
            </div>
        </div>
    </div>

    <div id="surplusCaro" class="carousel carousel-dark slide">
        <div class="carousel-inner">

            <div class="carousel-item active">
                <div class="container-fluid">

                    <div class="row">

                        <div class="col-md-1"></div>
                        <div class="col-md-2 mb-3" v-for="(item, index) in items.slice(0, 5)" :key="index">
                            <div class="card card-edit">
                                <img :src="item.ImageURL" class="card-img-top" alt="Surplus Listing"
                                    style="width:100%; height:180px;">
                                <h5>{{ item.IngredientName }}</h5>
                                <p class="price" style="padding-left:10px;">
                                    <s class="text-danger">${{ item.OriginalPrice }}</s>
                                    <strong class="ms-2 text-dark">${{ item.SalePrice }}</strong>
                                </p>
                                <!-- <p>Some text about the product</p> -->
                                <div class="mt-auto">
                                    <button type="button" style="font-family:Montserrat;" class="btn btn-success"
                                        @click="addtoCart(item)">Add to Cart</button>
                                </div>
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
                        <div class="col-md-2 mb-3" v-for="(item, index) in items.slice(5, 10)" :key="index">
                            <div class="card card-edit">
                                <img :src="item.ImageURL" class="card-img-top" alt="Recipe"
                                    style="width:100%; height:180px;">
                                <h5>{{ item.IngredientName }}</h5>
                                <p class="price" style="padding-left:10px;">
                                    <s class="text-danger">${{ item.OriginalPrice }}</s>
                                    <strong class="ms-2 text-dark">${{ item.SalePrice }}</strong>
                                </p>
                                <!-- <p>Some text about the product</p> -->
                                <div class="mt-auto">
                                    <button type="button" style="font-family:Montserrat;" class="btn btn-success"
                                        @click="addtoCart(item)">Add to Cart</button>
                                </div>
                            </div>
                        </div>

                        <div class="col-md-1"></div>
                    </div>


                </div>
            </div>
        </div>

        <button class="carousel-control-prev" type="button" data-bs-target="#surplusCaro" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
        </button>
        <button class="carousel-control-next" type="button" data-bs-target="#surplusCaro" data-bs-slide="next">
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
            location: "",
            desiredQuantity: {},
            items: [],
            cart: [],
            cartLength: 0,
            showCheckoutAlert: false,
            modal: null,
            totalPrice: 0.0,


        };
    },
    async created() {
        try {
            const response = await axios.get(`http://127.0.0.1:5000/listings`);
            this.items = response.data;
            // console.log('All cookies:', Cookies.get());
            if (Cookies.get("showCheckoutAlert")) {
                this.showCheckoutAlert = Cookies.get('showCheckoutAlert');
                // console.log(this.showCheckoutAlert);
                if (this.showCheckoutAlert) {

                    Cookies.remove("totalPrice");
                    Cookies.set('showCheckoutAlert', false);
                }
            }

            if (Cookies.get("cart")) {
                this.cart = JSON.parse(Cookies.get("cart"));
            }

            if (Cookies.get("cartLength")) {
                this.cartLength = Cookies.get("cartLength");
            } else {
                this.cartLength = 0;
            }

            if (Cookies.get("itemTotalPrice")) {
                // this.calcTotal(Cookies.get("itemTotalPrice"));
                this.totalPrice = this.calcTotal(Cookies.get("itemTotalPrice"));
                // console.log(this.totalPrice);
            } else {
                this.totalPrice = 0.0;
            }

        } catch (error) {
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
            if (Cookies.get("cart")) {
                this.cart = JSON.parse(Cookies.get("cart"));
                this.cartLength = Cookies.get("cartLength");
                if (!this.checkDup(item)) {

                    this.cart.push(item);
                    Cookies.set('cart', JSON.stringify(this.cart));
                    // console.log(JSON.parse(Cookies.get('cart')));
                    this.desiredQuantity[item.id] = 1;
                    Cookies.set('desiredQuantity', JSON.stringify(this.desiredQuantity));
                    this.cartLength++;
                    Cookies.set('cartLength', this.cartLength);
                    // console.log("notaddcart");


                }
            } else {
                if (!this.checkDup(item)) {
                    this.cart.push(item);
                    Cookies.set('cart', JSON.stringify(this.cart));
                    // console.log(JSON.parse(Cookies.get('cart')));
                    this.desiredQuantity[item.id] = 1;
                    Cookies.set('desiredQuantity', JSON.stringify(this.desiredQuantity));
                    this.cartLength++;
                    Cookies.set('cartLength', this.cartLength);
                    // console.log("notaddcart");
                }
            }


        },
        checkDup(item) {
            // Check if the `cart` array has an object with the same `id` as `item`
            if (this.cart.some(cartItem => cartItem.id === item.id)) {
                // console.log("Dup check");
                return true
            } else {
                // console.log("not dup");
                return false;
            }
        },
        calcTotal(obj) {
            let sum = Object.values(obj).reduce((a, b) => parseFloat(a) + parseFloat(b), 0);
            return parseFloat(sum.toFixed(2));
        },
        calculateItemTotal(item) {
            let calc = this.desiredQuantity[item.id] * item.SalePrice
            this.itemTotalPrice[item.id] = parseFloat(calc.toFixed(2));
        },

    },

}

</script>