<style scoped>
#div {
    position: absolute;
    top: 50%;
    left: 75%;
    transform: translate(-50%, -50%);
}
.fridge-container {
  display: flex;
  flex-direction: column;
  justify-content: end;
  text-align: center;
  max-width: 100%;
}

.fridge-img {
  max-width: 100%;
  cursor: pointer;
}

.item-list {
  list-style: none;
  padding: 0;
}

.hidden {
  display: none;
}

</style>
<template>
    <section>
        <!-- Jumbotron -->
        <div class="px-5 py-5 px-md-5 text-center text-lg-start"
            style="background-color: hsl(0, 0%, 96%);background-size: cover; height: 100vh;">
            <div class="container">
                <div class="row gx-lg-5 align-items-center">
                    <div class="col-lg-6 mb-5 mb-lg-0">
                        <br><br><br><br>
                        <h1 class="my-2 display-4 fw-bold" style="color:#408558">
                            Open me to see <span style="color:black">your ingredients!</span>
                        </h1>
                        <br/>
                    </div>
                    <!-- <img src="../assets/FridgeOpen.png"> -->
                    <div class="fridge-container col-lg-6 mb-5 mb-lg-0 mt-5 align-items-center">
                        <img
                            @click="toggleFridge()"
                            id="fridge-image"
                            class="fridge-img"
                            :src="test"
                            alt= "Fridge picture"
                            style="height:500px; width:300px"
                        />
                        <ul id="item-list" class="item-list" :class="{ hidden: !isFridgeOpen }">
                            <li v-for="(item, i) in items">
                            {{item}}
                            <button @click="items.splice(i, 1)">Remove</button> 
                            </li>
                        </ul>
                    </div>
                    <!-- <div class="col-lg-6 mb-5 mb-lg-0 ">
                        <div style="position: relative;" class="col-lg-6 mb-5 mb-lg-0">
                            <img src="../assets/FridgeClosed.png" alt="Fridge Closed" style="height:500px; width:300px">
                            <div style="position: absolute; left: 10px; top: 10px;  color: white; background: rgba(108, 108, 108, 0.5); padding: 10px; border-radius: 20px; height: 450px; width:250px;">
                                <h3>Items:</h3>
                                <ul>
                                    <li v-for="(item, i) in items">
                                    {{item}}
                                    <button @click="items.splice(i, 1)">Remove</button> 
                                    </li>
                                </ul>
                            </div>
                        </div>   
                    </div> -->
                </div>

                <div class="card col-4">
                            <div class="card-body py-3 px-md-3">
                                <form>
                                    <!-- 2 column grid layout with text inputs for the first and last names -->
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
    async created(){ 
        console.log(this.isFridgeOpen);
        this.test='../SuperplusHero/src/assets/FridgeClosed.png';
        console.log(this.test);
    },
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
            const itemList = document.getElementById("item-list");
            itemList.classList.toggle("hidden", !this.isFridgeOpen);
            var fridgeImage = document.getElementById("fridge-image");
            this.test = this.isFridgeOpen ? "../assets/FridgeOpen.png" : "../assets/FridgeClosed.png";
            console.log(this.isFridgeOpen);
            console.log(this.test);
        },
    }
}
</script>