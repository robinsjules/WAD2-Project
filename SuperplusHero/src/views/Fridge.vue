<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap');
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Montserrat', sans-serif;
}

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
    border: 2px solid rgb(10, 160, 10);
    padding: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-radius: 20px;
    background-color: rgb(237, 243, 235);
    color: black;
}

.fridge {
    border-radius: 30px;
}

.btn-custom {
    background-color: rgb(112, 112, 112);
    color: white;
    border: 1px solid white; 
    padding: 5px;
    border-radius: 15px;
}

.btn-custom.hovered{
    background-color: rgb(161, 0, 0);
}


.glowing-image {
    animation: glow 2s infinite;
}

@keyframes glow {
    0% {
        box-shadow: 0 0 40px rgba(255, 225, 0, 0.7);
    }

    50% {
        box-shadow: 0 0 60px rgba(255, 225, 0, 0.9);
    }

    100% {
        box-shadow: 0 0 40px rgba(255, 225, 0, 0.7);
    }
}
</style>
<template>
    <section>
        <!-- Jumbotron -->
        <div class="px-5 py-5 px-md-5 text-center text-lg-start"
            style="background-color: rgb(237, 243, 235); background-size: cover; height: 100vh; overflow:auto">
            <div class="container">
                <div class="row gx-lg-5">
                    <div class="col-lg-6 mb-5 mb-lg-0">
                        <br><br><br><br>
                        <div>
                            <h1 class="my-2 display-4 fw-bold" style="color:rgb(10, 160, 10)">
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
                                            <input v-model="newItem" type="text" id="form3Example2"
                                                class="form-control" placeholder="Eg. Banana" />
                                        </div>
                                    </div>
                                    <br />
                                    <div class="col-12 mb-4">
                                        <div class="d-flex">
                                            <button type="button" class="btn btn-success w-100" style="background-color:rgb(10, 160, 10)" @click="addnewFridge">
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
                                        style="background-color:rgb(237, 243, 235); border: 2px solid rgba(10, 160, 10, 0.728);">
                                        <ul id="item-list" class="item-list" :class="{ hidden: !isFridgeOpen }">
                                            <li v-for="(item, i) in items">
                                                <div class="d-flex justify-content-between ingredient-card">
                                                    <span class="text-start" style="font-weight:600;">{{ item.name }}</span>&nbsp;
                                                    <span class="text-start" style="font-weight:600;"> ({{ item.expiryDate }})</span>&nbsp;
                                                    <button @click="removeItem(item)" @mouseover="changeButtonColor" @mouseout="restoreButtonColor"
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
            data: [],
        }
    },
    mounted() {
        this.fetchFridgeFromServer();
    },
    methods: {
        async fetchFridgeFromServer() {
            try {
                const fridgeuser = 'julesrobins';
                const response = await axios.get(`http://127.0.0.1:5000/fridge/${fridgeuser}`);
                console.log('Fetched Fridge Data:', response.data); // Log the fetched data
                this.data = response.data;
                this.items = this.data[0].Fridge;

            } catch (error) {
                console.error('Error fetching items:', error);
            }
        },
        async add() {
            if (this.newItem != '') {
                this.items.push(this.newItem)
                this.newItem = ''
            }
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
        async addnewFridge() {
            if (this.newItem != '') {
                const [itemName, expiryDate] = this.newItem.split(',').map((item) => item.trim());
                const newfridgeItem = {
                "name": itemName,
                "expiryDate": expiryDate,
                };
                this.items.push(newfridgeItem);
                this.newItem='';
            }
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
        // [{
        // "name": "sesame seeds",
        // "expiryDate": "2023/11/15"
        // },
        // {
        // "name": "sesame seeds",
        // "expiryDate": "2023/11/15"
        // },
        // {
        // "name": "sesame seeds",
    
        async removeItem(index) {
            this.items.splice(index, 1);
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
        changeButtonColor() {
        // Add a class to change the button color on hover
        document.querySelector('.btn-custom').classList.add('hovered');
         },
        restoreButtonColor() {
        // Remove the added class to restore the original button color
        document.querySelector('.btn-custom').classList.remove('hovered');
        },
    }
}
</script>