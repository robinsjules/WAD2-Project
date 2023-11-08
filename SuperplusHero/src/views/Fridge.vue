<style scoped>
#div {
    position: absolute;
    top: 50%;
    left: 75%;
    transform: translate(-50%, -50%);
}
</style>
<template>
    <section class="">
        <!-- Jumbotron -->
        <div class="px-5 py-5 px-md-5 text-center text-lg-start"
            style="background-image: ; background-color: hsl(0, 0%, 96%);background-size: cover; height: 100vh;">
            <div class="container">
                <div class="row gx-lg-5 align-items-center">
                    <div class="col-lg-6 mb-5 mb-lg-0">
                        <br><br><br><br>
                        <h1 class="my-5 display-4 fw-bold" style="">
                            What is in your fridge?
                        </h1>
                        <p style="color: hsl(217, 10%, 50.8%)">
                            Add and remove items that are currently in your refrigerator.
                        </p>
                    </div>
                    

                    <div class="col-lg-6 mb-5 mb-lg-0">
                        <div class="card" id="div">
                            <div class="card-body py-5 px-md-5">
                                <form>
                                    <!-- 2 column grid layout with text inputs for the first and last names -->
                                    <div class="col-md-12 mb-4">
                                        <div class="form-outline">
                                            <label for="fridgeItems">Enter Item</label>
                                            <input @keyup.enter="add" v-model="newItem" type="text" id="form3Example2" class="form-control"
                                                placeholder="Eg. Banana" />
                                        </div><br>
                                    </div>
                                    <div class="col-md-12 mb-4">
                                        <div class="d-flex justify-content-between">
                                            <button type="button" class="btn btn-primary w-100" @click="add">Add
                                                Item</button>
                                        </div>
                                    </div>
                                    <!-- Submit button -->
                                    
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
                <br>
                <div style="position: relative;" class="col-lg-6 mb-5 mb-lg-0">
                    <img src="../assets/FridgePicture.png" alt="Fridge background" style="height:500px; width:300px">
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
        }
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
        }
    }
}
</script>