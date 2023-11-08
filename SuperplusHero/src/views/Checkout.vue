<style scoped>
    .content {
        margin-top: 125px;

    }

    .test{
        margin:auto;
    }


    .paymentCard{
        position: sticky;
        top:125px;
    }
</style>

<template>
    <div class="content">
        <div class="container-fluid row test">

            <div class="cart col-lg-6">

                <div class="order">
                    <div class="card">
                        
                        <ul class="list-group list-group-flush">
                            <div v-for="(item,index) in items"  :key="index">
                                <li class="list-group-item">
                                    <img :src="item.ImageURL" class="card-img-top" alt="Recipe" style="width:100%">
                                    <h1>{{item.IngredientName}}</h1>
                                    <p class="price"> <s>{{ item.OriginalPrice }}</s><strong class="ms-2 text-danger">{{ item.SalePrice }}</strong></p>

                                </li>
                            </div>
                        </ul>
                        <!-- <div class="col-md-2 mb-3" v-for="(item, index) in items" :key="index">
                            <div class="card">
                                <img :src="item.ImageURL" class="card-img-top" alt="Recipe" style="width:100%">
                                <h1>{{item.IngredientName}}</h1>
                                <p class="price"> <s>{{ item.OriginalPrice }}</s><strong class="ms-2 text-danger">{{ item.SalePrice }}</strong></p>
                                
                                <p><button type="button" class="btn btn-primary" @click="addtoCart(item)">Add to Cart</button></p>    
                            </div>
                        </div> -->
                        <img src="https://wallpapercave.com/wp/wp4489833.jpg">
                    </div>
                </div>
            </div>

            <div class="payment col-lg-6  ">

                <div class="card paymentCard">

                    <ul class="list-group list-group-flush">
                        <li class="list-group-item">Normal Price: ${{ normalTotalPrice }}</li>
                        <li class="list-group-item">Savings: ${{ savedTotal }}</li>
                        <li class="list-group-item">Total: ${{ totalPrice }}</li>
                    </ul>

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
            itemNormalTotal:{},
            normalTotalPrice:0.0,
            totalPrice:0.0,
            savedTotal:0.0,
            cart:[],
            newCartItem: false,
            cartLength: 0,
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
        this.normalTotalPrice = this.calcTotal(this.itemNormalTotal);
        this.savedTotal = this.normalTotalPrice - this.totalPrice;
            
        },
    methods: {
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
                Cookies.set('desiredQuantity', JSON.stringify(this.desiredQuantity)); // Update cookies
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
                    this.calculateItemNormalTotal(item);
                    
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
            this.normalTotalPrice = this.calcTotal(this.itemNormalTotal)
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
            this.normalTotalPrice = this.calcTotal(this.itemNormalTotal)
        },
        calculateItemTotal(item){
            let calc = this.desiredQuantity[item.id] * item.SalePrice
            this.itemTotalPrice[item.id] = parseFloat(calc.toFixed(2)); 
        },
        calculateItemNormalTotal(item){
            let calc = this.desiredQuantity[item.id] * item.OriginalPrice
            this.itemNormalTotal[item.id] = parseFloat(calc.toFixed(2)); 
        }
    }
};

</script>