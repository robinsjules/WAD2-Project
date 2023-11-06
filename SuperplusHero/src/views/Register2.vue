<!-- <template> -->
    <!-- Section: Design Block -->
    <!-- <section class=""> -->
        <!-- Jumbotron -->
        <!-- <div class="px-5 py-5 px-md-5 text-center text-lg-start"
            style="background-color: hsl(0, 0%, 96%);background-size: cover; height: 100vh;">
            <div class="container">
                <div class="row gx-lg-5 align-items-center">
                    <div class="col-lg-6 mb-5 mb-lg-0">
                        <h1 class="my-5 display-3 fw-bold ls-tight">
                            Welcome to <br />
                            <span class="text-success">Surplus Hero.</span>
                        </h1>
                        <p style="color: hsl(217, 10%, 50.8%)">
                            The one stop platform for surplus groceries and recipe generation!
                        </p>
                    </div> -->

                    <!-- <div class="col-lg-6 mb-5 mb-lg-0">
                        <div class="card">
                            <div class="card-body py-5 px-md-5">
                                <div class=" fw-bolder ls-tight">
                                    <h1>Create Account</h1>
                                </div><br>
                                <form> -->
                                    <!-- 2 column grid layout with text inputs for the first and last names -->
                                    <!-- <div class="col-md-12 mb-4">
                                        <div class="form-outline">
                                            <label>Allergies</label>
                                            <input v-model="Allergies" type="text" class="form-control" id="Allergies"
                                                placeholder="Eg. Shellfish">
                                        </div>
                                    </div>
                                    <div class="col-md-12 mb-4">
                                        <div class="form-outline">
                                            <label for="Fridge">Items in Fridge</label>
                                            <input v-model="item" type="text" id="Fridge" class="form-control"
                                                placeholder="Eg. Banana" />
                                            <br><h4>Items:</h4>
                                            <ul>
                                                <li v-for="(item) in Fridge">
                                                    {{ item }}
                                                </li>
                                            </ul>
                                        </div><br>
                                    </div> -->

                                    <!-- <div class="col-md-12 mb-4">
                                        <div class="d-flex justify-content-between">
                                            <button type="button" class="btn btn-primary w-100" @click="addItem">Add
                                                Item</button>
                                            <button type="button" class="btn btn-danger w-100" @click="Fridge.splice(-1, 1)">Delete
                                                Item</button>
                                        </div>
                                    </div> -->
                                    <!-- Submit button -->
                                    <!-- <div class="col-md-12 mb-4">
                                        <div class="d-flex justify-content-between">
                                            <button @click="goToNext" type="submit"
                                                class="btn btn-success w-100">Next</button>
                                        </div>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
        </div> -->
        <!-- Jumbotron -->
    <!-- </section> -->
    <!-- Section: Design Block -->
<!-- </template>
<script>
import axios from 'axios';
export default {
    data() {
        return {
            Fridge: [],
            form: {
                Allergies: '',
                item: '',
            }
        }
    },
    methods: {
        addItem() {
            if (this.item != '') {
                        this.Fridge.push(this.item)
                        this.item = ''  // clear the input box -->
                    <!-- }
        },
        goToNext() {
            var url = 'http://127.0.0.1:5000/register_user';
            var para = {
                Allergies: this.form.Allergies,
                Fridge: this.Fridge,
            }
            console.log(para)
            axios.post(url, para)
                .then(response => {
                    console.log(response.data)
                    this.$router.push({ name: 'Login' });
                }) -->
                <!-- .catch(error => {
                    console.log(error.message)
                    console.error(error.response.data)
                    // document.getElementById("axios").innerText = error.message;
                });
            // this.$router.push({ name: 'Login' });
            // console.log(JSON.stringify(this.form));
        }
    }
} -->
<!-- </script> -->