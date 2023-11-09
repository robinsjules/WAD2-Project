<style scoped>
#child {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -45%);
    width: 80%;
    height: 80%;
}

.fridge-container {
    display: flex;
    flex-direction: column;
    justify-content: end;
    text-align: center;
    max-width: 100%;
}

.fridge-img-closed {
    display: block;
}

.fridge-img-open {
    display: none;
}

.item-list {
    list-style: none;
    padding: 0;
}

.hidden {
    display: none;
}

.ingredient-card {
    border: 2px solid #FF6F61;
    padding: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-radius: 20px;
    background-color: #008080;
    color: white;
}

.fridge {
    border-radius: 30px;
}

.btn-custom {
    background-color: #c1c5c49d;
    color: #ff5748;
    border-radius: 20px;
    font-weight: bold;
}

.glowing-image {
    animation: glow 2s infinite;
}

@keyframes glow {
    0% {
        box-shadow: 0 0 20px rgba(255, 225, 0, 0.7);
    }

    50% {
        box-shadow: 0 0 40px rgba(255, 225, 0, 0.9);
    }

    100% {
        box-shadow: 0 0 20px rgba(255, 225, 0, 0.7);
    }
}
</style>
<template>
    <section>
        <!-- Jumbotron -->
        <div class="px-5 py-5 px-md-5 text-center text-lg-start"
            style="background-color: hsl(0, 0%, 96%); background-size: cover; height: 100vh; overflow:auto">
            <div class="container">
                <div class="row gx-lg-5">
                    <div class="col-lg-6 mb-5 mb-lg-0">
                        <br><br><br><br>
                        <div>
                            <h1 class="my-2 display-4 fw-bold" style="color:#408558">
                                Open me to see <span style="color:black">your ingredients!</span>
                            </h1>
                        </div>

                        <br />
                        <div class="card">
                            <div class="card-body py-3 px-md-3">
                                <form>
                                    <div class="col-12 mb-2">
                                        <div class="form-outline">
                                            <label for="fridgeItems">Enter Item</label>
                                            <input @keyup.enter="add" v-model="newItem" type="text" id="form3Example2"
                                                class="form-control" placeholder="Eg. Banana" />
                                        </div>
                                    </div>
                                    <br />
                                    <div class="col-12 mb-4">
                                        <div class="d-flex">
                                            <button type="button" class="btn btn-success w-100" @click="add">
                                                Add Item</button>
                                        </div>
                                    </div>
                                    <!-- Submit button -->
                                    <p style="color: hsl(217, 10%, 50.8%)">
                                        Add and remove items that are currently in your refrigerator.
                                    </p>
                                </form>
                            </div>
                        </div>
                        <p class="py-3">
                            <button @click=sendFridgeToServer class="btn btn-success">Save items</button>
                        </p>
                    </div>

                    <div class="fridge-container col-lg-6 mb-5 mb-lg-0 mt-5 align-items-center">
                        <img @click="toggleFridge()" id="fridge-image" class="fridge-img-closed"
                            src="../assets/FridgeClosed.png" alt="Fridge closed picture"
                            style="height:700px; width:420px" />
                        <div style="position:relative;">
                            <img @click="toggleFridge()" id="fridge-open" :class="{ hidden: !isFridgeOpen }"
                                src="../assets/FridgeOpen.png" alt="Fridge open picture"
                                style="height:700px; width:420px" />
                            <div id="child">
                                <div class="card fridge glowing-image" style="height:560px; overflow:auto;"
                                    :class="{ hidden: !isFridgeOpen }">
                                    <div class="card-body fridge"
                                        style="background-color:#86cbc99d; border: 3px solid #FF6F61;">
                                        <ul id="item-list" class="item-list" :class="{ hidden: !isFridgeOpen }">
                                            <li v-for="(item, i) in items">
                                                <div class="d-flex justify-content-between ingredient-card">
                                                    <span class="text-start">{{ item }}</span>
                                                    <button @click="(item).splice(i, 1)"
                                                        class="text-end btn-custom">Remove</button>
                                                </div>
                                                &nbsp;
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Jumbotron -->
    </section>
</template>
<script>
import axios from 'axios';

export default {
    data() {
        return {
            items: [],
            newItem: '',
            isFridgeOpen: false,
            test: '',
            data:[],
        }
    },
    mounted() {
        this.fetchFridgeFromServer();
        this.sendFridgeToServer();
    },
    methods: {
        async fetchFridgeFromServer() {
            try {
                const fridgeuser = 'julesrobins'; 
                const response = await axios.get(`http://127.0.0.1:5000/fridge/${fridgeuser}`);
                console.log('Fetched Fridge Data:', response.data); // Log the fetched data
                this.data = response.data;
                this.items=this.data[0].Fridge;

            } catch (error) {
                console.error('Error fetching items:', error);
            }
        },
        async sendFridgeToServer() {
            try {
                const fridgeuser = 'julesrobins'; 
                const updatedData = {
                    'Fridge': this.items,
                }
                const response = await axios.put(`http://127.0.0.1:5000/update_fridge/${fridgeuser}`, updatedData);
                console.log('Sending Fridge Data:', updatedData);
            } catch (error) {
                console.error('Error sending items:', error);
            }
        },
        add() {
            if (this.newItem != '') {
                this.items.push(this.newItem)
                this.newItem = ''
            }
        },
        goToNext() {
            this.$router.push({ name: 'Login' });
            console.log(JSON.stringify(this.form));
        },
        toggleFridge() {
            this.isFridgeOpen = !this.isFridgeOpen;
            const fridgeImage = document.getElementById("fridge-image");
            if (this.isFridgeOpen) {
                fridgeImage.classList.remove("fridge-img-closed");
                fridgeImage.classList.add("fridge-img-open");
            } else {
                fridgeImage.classList.remove("fridge-img-open");
                fridgeImage.classList.add("fridge-img-closed");
            }
        },
    }
}
</script>