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
  border: 1px solid #ccc; /* Add a border around the card */
  padding: 10px;
  display: flex;
  justify-content: space-between; /* Align label and checkbox to opposite ends */
  align-items: center; /* Vertically center the content */
  margin-bottom: 5px; /* Add some space between cards */
}

</style>
<template>
    <section>
        <!-- Jumbotron -->
        <div class="px-5 py-5 px-md-5 text-center text-lg-start"
            style="background-color: hsl(0, 0%, 96%);background-size: cover; height: 100vh;">
            <div class="container">
                <div class="row gx-lg-5">
                    <div class="col-lg-6 mb-5 mb-lg-0">
                        <br><br><br><br>
                        <h1 class="my-2 display-4 fw-bold" style="color:#408558">
                            Open me to see <span style="color:black">your ingredients!</span>
                        </h1>
                        <br/>
                        <div class="card">
                            <div class="card-body py-3 px-md-3">
                                <form>
                                    <div class="col-12 mb-2">
                                        <div class="form-outline">
                                            <label for="fridgeItems">Enter Item</label>
                                            <input @keyup.enter="add" v-model="newItem" type="text" id="form3Example2" class="form-control"
                                                placeholder="Eg. Banana" />
                                        </div>
                                    </div>
                                    <br/>
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
                    </div>

                    <div class="fridge-container col-lg-6 mb-5 mb-lg-0 mt-5 align-items-center">
                        <img
                            @click="toggleFridge()"
                            id="fridge-image"                           
                            class="fridge-img-closed"
                            src="../assets/FridgeClosed.png"
                            alt= "Fridge closed picture"
                            style="height:700px; width:420px"
                        />
                        <div style="position:relative;">
                            <img
                                @click="toggleFridge()"
                                id="fridge-open"
                                :class="{ hidden: !isFridgeOpen }"
                                src="../assets/FridgeOpen.png"
                                alt= "Fridge open picture" 
                                style="height:700px; width:420px"
                            />
                            <div id="child">
                                <div class="card" style="height:560px; overflow:auto;" :class="{ hidden: !isFridgeOpen }">
                                    <div class="card-body rounded" style="background-color:#408c5b; color:white">
                                        <ul id="item-list" class="item-list" :class="{ hidden: !isFridgeOpen }">
                                            <li v-for="(item, i) in items">
                                                <div class="d-flex justify-content-between ingredient-card">
                                                    <span class="text-start">{{item}}</span>
                                                    <button @click="items.splice(i, 1)" class="btn btn-dark text-end" >Remove</button>
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
export default {
    data() {
        return {
                items: ['Chicken', 'Pork', 'Ginger', 'Bak Choy', 'Kai Lan'],
                newItem: '',
                isFridgeOpen: false,
                test: '',

        }
    },
    // async created(){ 
    //     // console.log(this.isFridgeOpen);
    //     this.test='../assets/FridgeClosed.png';
    //     // console.log(this.test);
    // },
    methods: {
        add() {
            if (this.newItem != '') {
                        this.items.push(this.newItem)
                        this.newItem = ''  // clear the input box
                    }
        },
        goToNext() {
            this.$router.push({ name: 'Login' });
            console.log(JSON.stringify(this.form));
        },
        toggleFridge() {
            this.isFridgeOpen = !this.isFridgeOpen;

            // Get the fridge image element
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