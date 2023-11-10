<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');

.navbar-nav {
    margin-left: auto;

}


* {
    font-family: 'Montserrat', sans-serif;
}
</style>

<template>
    <body>
        <!-- Header-->
        <header class="bg-dark py-5">
            <div class="container px-4 px-lg-5 my-5">
                <div class="text-center text-white">
                    <h1 class="display-4 fw-bolder">Surplus Products</h1>
                    <p class="lead fw-normal text-white-50 mb-0">Purchase them at discounted prices!</p>
                </div>
            </div>
        </header>
        <!-- Section-->
        <br>
        <div class="container-fluid">
            <div class="form-group">
                <div class="row justify-content-center">
                    <div class="col-md">
                        <div class="input-group me-8">
                            <input v-model="searchQuery" type="text" class="form-control" placeholder="Search Product..">
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <section class="py-5">
            <div class="container px-4 px-lg-5 mt-5">
                <div class="row gx-4 gx-lg-5 row-cols-2 row-cols-md-3 row-cols-xl-4 justify-content-center">
                    <div class="col mb-5" v-for="(item, index) in items" :key="index">
                        <div class="card h-100">
                            <!-- Product image-->
                            <img class="card-img-top" :src="item.ImageURL" style="width: 100%;" alt="..." />
                            <!-- Product details-->
                            <div class="card-body p-4">
                                <div class="text-center">
                                    <!-- Product name-->
                                    <h5 class="fw-bolder">{{ item.IngredientName }}</h5>
                                    <!-- Product price-->
                                    <span class="text-decoration-line-through" style="color: red;">${{ item.OriginalPrice
                                    }}</span>
                                    ${{ item.SalePrice }}
                                </div>
                            </div>
                            <!-- Product actions-->
                            <div class="card-footer p-4 pt-0 border-top-0 bg-transparent">
                                <div class="text-center">
                                    <p><button type="button" style="font-family:Montserrat;" class="btn btn-success"
                                            @click="addtoCart(item)">Add to Cart</button></p>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>
        </section>
    </body>
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
            searchQuery: '',
            products: { results: [] },
            product: '',
        };
    },
    async created() {
        try {
            const response = await axios.get(`http://127.0.0.1:5000/listings`);
            this.items = response.data;
            // console.log('All cookies:', Cookies.get());
            console.log(this.itemss);
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
        } catch (error) {
            console.error(error);
        }
    },
    computed: {
        filteredProducts() {
            // Filter recipes based on selected cuisine and searchQuery
            return this.products.results
                .filter((product) => {
                    // Check for unique recipes based on title
                    return !this.isDuplicateRecipe(recipe);
                })
                .filter((product) => {
                    const cuisineMatch = this.selectedCuisine === '' || recipe.cuisines.includes(this.selectedCuisine);
                    const searchMatch = this.searchQuery === '' || recipe.title.toLowerCase().includes(this.searchQuery.toLowerCase());
                    return cuisineMatch && searchMatch;
                });
        },
    },
    methods: {
        searchProducts() {
            this.products.results = this.items.filter((product) => {
                const searchMatch = this.searchQuery === '' || product.IngredientName.toLowerCase().includes(this.searchQuery.toLowerCase());
                return searchMatch;
            });
            // The filtering is done through the computed property
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
    }
}
</script>