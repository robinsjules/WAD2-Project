<style scoped>

    body{
        background-color: rgb(237,243,235);
        font-family: 'Montserrat';
        min-height: 100vh;
    }
    .content {
        padding-top: 125px;

    }

    .test{
        margin:auto;
    }

    .payment {
        position: relative;
    }   

    .paymentCard{
        position: sticky;
        top:125px;
    }
    .moneyStuff {
        font-weight: bold;
    }
    .list-group-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .nestedFlex, .nestedFlex2 {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        width: 30%; 
    }
    
    .cartItemDetails {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        width: 100%;
    }

    .cartItemQuantity{
        text-align: center;
    }

    .card{
        margin-bottom: 20px;
    }

    
    .checkoutBtn {
    position: sticky;
    top: 269px; /* 125px for the navbar + 144px for the size of the list group and margin */
    
}

.checkoutBtn .btn {
    width: 100%;
}

.card-img-top {
    max-width: 100%;
    /* width: 20%;        
    height: auto;       */
        width: 150px;   /* This can be adjusted as per requirement */
    height: 150px;  /* This can be adjusted as per requirement */
    object-fit: cover; 
}

</style>

<template>

    <body>


    <div class="content">
        <div class="container-fluid row test">
            <div class="col-lg-1"></div>
            <div class="cart col-lg-5">

                <div class="order">
                    <div class="card">
                        
                        <ul class="list-group list-group-flush">
                            <div v-for="(item,index) in cart"  :key="index">
                                <li class="list-group-item">
                                    <img :src="item.ImageURL" class="card-img-top img-fluid" alt="Recipe">
                                    
                                    <div class="nestedFlex">
                                        <div>
                                            {{item.IngredientName}}
                                        </div>
    
                                        <div class="cartItemQuantity">
                                            <b>Stock Available:</b> {{  item.Quantity }}
                                            <br>
                                            <b>Quantity:</b> 
                                        </div>

                                        <div>
                                            <button class="btn btn-success" @click="decreaseQuantity(item)" :disabled="desiredQuantity[item.id] <= 1">-</button>
                                            {{desiredQuantity[item.id] || 1}} 
                                            <!-- If item id exists in desiered quantity object set value to 1 if not go next -->
                                            <button class="btn btn-success" @click="increaseQuantity(item)" :disabled="desiredQuantity[item.id] >= item.Quantity">+</button>
                                        </div>

                                    </div>
                                    
                                    <div class="nestedFlex2">
                                        <button class="btn btn-secondary remove" @click="removeFromCart(item)">X</button>
                                        <p class="price text-danger"> <s>${{ item.OriginalPrice }}</s><strong class="ms-2" style="color:black;">${{ item.SalePrice }}</strong></p>
                                    </div>
                                    
                                </li>
                            </div>
                        </ul>
                        <!-- <img src="https://wallpapercave.com/wp/wp4489833.jpg"> -->
                    </div>
                </div>
            </div>

            <div class="payment col-lg-5  ">

                <div class="card paymentCard">

                    <ul class="list-group list-group-flush">
                        <li class="list-group-item">Normal Price: <span class='moneyStuff text-danger'>${{ normalTotalPrice }}</span></li>
                        <li class="list-group-item">Savings: <span class='moneyStuff'>${{ savedTotal }}</span></li>
                        <li class="list-group-item">Total: <span class='moneyStuff text-success'>${{ totalPrice }}</span></li>
                    </ul>

                </div>
                
                <div class="checkoutBtn">
                    <router-link to="/home">
                        <button class="btn btn-success checkout" @click="checkout">Checkout</button>
                    </router-link>
                </div>


            </div>
        </div>

        <div class="col-lg-1"></div>

    </div>
</body>
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
            items:[],
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
        this.savedTotal = (this.normalTotalPrice - this.totalPrice).toFixed(2);
            
        },
    methods: {
        checkout() {
            Cookies.set('showCheckoutAlert', true);
            this.$router.push('/home');

            Cookies.remove('desiredQuantity');
            Cookies.remove('itemTotalPrice');
            Cookies.remove('itemNormalTotal');
            Cookies.remove('cart');
            Cookies.remove("cartLength");
            this.totalPrice = 0;
            Cookies.remove('totalPrice');

            axios.post('http://127.0.0.1:5000/send_email/robinsjules2019@gmail.com')
        },
        calcTotal(obj){
            let sum = Object.values(obj).reduce((a, b) => parseFloat(a) + parseFloat(b), 0);
            return parseFloat(sum.toFixed(2)); 
        },
        reCalcAfterRemoval(){
            this.cart = Cookies.get("cart");

            this.calculateItemTotal(item);  // Calculate new Total Sale Price
            this.calculateItemNormalTotal(item) // Calculate new Total Normal Price
        },
        removeFromCart(item) {
            const index = this.cart.findIndex(cartItem => cartItem.id === item.id); 
            if (index !== -1) {
                this.cart.splice(index, 1);
                Cookies.set('cart', JSON.stringify(this.cart));
                // Additional section for normal price adjustment
                if (this.itemNormalTotal[item.id]) {
                    delete this.itemNormalTotal[item.id];
                    Cookies.set('itemNormalTotal', JSON.stringify(this.itemNormalTotal)); 
                }
                if (this.desiredQuantity[item.id]) {
                    delete this.desiredQuantity[item.id];
                    delete this.itemTotalPrice[item.id]; 
                    Cookies.set('desiredQuantity', JSON.stringify(this.desiredQuantity));
                }
            }
            this.totalPrice = this.calcTotal(this.itemTotalPrice);
            Cookies.set("totalPrice", this.totalPrice);
            console.log(Cookies.get('totalPrice'));
            this.normalTotalPrice = this.calcTotal(this.itemNormalTotal);
            this.savedTotal = (this.normalTotalPrice - this.totalPrice).toFixed(2);
            
            this.cartLength = this.checkCartLength();

            Cookies.set('cartLength', this.checkCartLength);
            

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
                
                if (Cookies.get('totalPrice')){
                    this.totalPrice = Cookies.get('totalPrice');
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
            this.calculateItemTotal(item);  // Calculate new Total Sale Price
            this.calculateItemNormalTotal(item) // Calculate new Total Normal Price
            this.totalPrice = this.calcTotal(this.itemTotalPrice);
            this.normalTotalPrice = this.calcTotal(this.itemNormalTotal)
            this.savedTotal = (this.normalTotalPrice - this.totalPrice).toFixed(2);
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
            this.calculateItemTotal(item);  // Calculate new Total Sale Price
            this.calculateItemNormalTotal(item) // Calculate new Total Normal Price
            this.totalPrice = this.calcTotal(this.itemTotalPrice);
            this.normalTotalPrice = this.calcTotal(this.itemNormalTotal)
            this.savedTotal = (this.normalTotalPrice - this.totalPrice).toFixed(2);
            Cookies.set("itemTotalPrice", this.itemTotalPrice);
            Cookies.set("totalPrice", this.totalprice);
        },
        calculateItemTotal(item){
            let calc = this.desiredQuantity[item.id] * item.SalePrice;
            this.itemTotalPrice[item.id] = parseFloat(calc.toFixed(2)); 
            Cookies.set('itemTotalPrice', JSON.stringify(this.itemTotalPrice));
        },
        calculateItemNormalTotal(item){
            let calc = this.desiredQuantity[item.id] * item.OriginalPrice;
            this.itemNormalTotal[item.id] = parseFloat(calc.toFixed(2)); 
            Cookies.set('itemNormalTotal', JSON.stringify(this.itemNormalTotal));
        }
    }
};

</script>