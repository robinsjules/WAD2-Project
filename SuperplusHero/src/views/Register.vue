<style scoped>
.btn {
    text-align: center;
};
@import url(../);
</style>
<template>
    <!-- Section: Design Block -->
    <section class="">
        <!-- Jumbotron -->
        <div class="px-5 py-5 px-md-5 text-center text-lg-start"
            style="background-color: hsl(0, 0%, 96%);background-size: cover; height: 115vh; background-image: url('https://www.europenowjournal.org/wp-content/uploads/2019/04/shutterstock_321864554.jpg');">
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
                    </div>

                    <div class="col-lg-6 mb-5 mb-lg-0">
                        <div class="card">
                            <div class="card-body py-5 px-md-5">
                                <div class=" fw-bolder ls-tight">
                                    <h1 style="text-align: center;">Sign Up</h1>
                                </div><br>

                                <form @submit.prevent = "goToNext">
                                    <!-- 2 column grid layout with text inputs for the first and last names -->
                                    <div class="col-md-12 mb-4">
                                        <div class="form-outline">
                                            <select v-model="form.UserType" class="form-control" id="dropdown">
                                                <option value="What type of user are you?" selected>What type of user are
                                                    you?</option>
                                                <option value="Consumer">Consumer</option>
                                                <option value="Business">Business</option>

                                            </select>
                                        </div>
                                    </div>
                                    <div class="col-md-12 mb-4">
                                        <div class="form-outline">
                                            <input v-model="form.UserName" type="text" id="form3Example1"
                                                class="form-control" placeholder="Username" />
                                            <!-- <label class="form-label" for="form3Example1">First name</label> -->
                                        </div>
                                    </div>


                                    <!-- Email input -->
                                    <div class="form-outline mb-4">
                                        <input v-model="form.Email" type="email" id="form3Example3" class="form-control"
                                            placeholder="Email Address" />
                                        <!-- <label class="form-label" for="form3Example3">Email address</label> -->
                                    </div>

                                    <!-- Phone Number -->
                                    <div class="form-outline mb-4">
                                        <input v-model="form.Phone" type="phonenum" id="form3Example4"
                                            class="form-control" placeholder="Phone Number" />
                                        <!-- <label class="form-label" for="form3Example3">Phone Number</label> -->
                                    </div>

                                    <!-- Password input -->
                                    <div class="form-outline mb-4">
                                        <input v-model="form.Password" type="password" id="form3Example5"
                                            class="form-control" placeholder="Password" />
                                        <!-- <label class="form-label" for="form3Example4">Password</label> -->
                                    </div>

                                    <div v-if="form.UserType === 'Consumer'">
                                        <div class="col-md-12 mb-4">
                                        <div class="form-outline">
                                            <input v-model="form.Allergies" type="text" class="form-control" id="Allergies"
                                                placeholder="Allergies (Eg. Shellfish)">
                                        </div>
                                    </div>
                                    <div class="col-md-12 mb-4">
                                        <div class="form-outline">
                                            <textarea  cols="4" rows="5" v-model="form.Fridge" type="text" id="Fridge" class="form-control"
                                                placeholder="Items in your fridge (Eg. Banana)" />
                                        </div><br>
                                    </div>
                                    </div>
                                    <!-- Submit button -->
                                    <div class="col-md-12 mb-4">
                                        <div class="d-flex justify-content-between">
                                            <button @click="goToNext" type="submit"
                                                class="btn btn-success w-100">Submit</button>
                                        </div>
                                    </div>

                                    <p style="text-align: center;">Already have an account? Click <router-link
                                            :to="{ name: 'Login' }">here</router-link> to log in</p>

                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Jumbotron -->
    </section>
    <!-- Section: Design Block -->
</template>
<script>
import axios from 'axios';

export default {
    // Your component data and methods go here
    data() {
        return {
            form: {
                UserType: 'What type of user are you?',
                UserName: '',
                Email: '',
                Phone: '',
                Password: '',
                Allergies: '',
                Fridge: '',
            }
        }
    },
    methods: {
        goToNext() {
            if(this.form.UserType === 'What type of user are you?'){
                alert('Please select a user type');
            }else{
                var url = 'http://127.0.0.1:5000/register_user';
                var para = {
                    UserType: this.form.UserType,
                    UserName: this.form.UserName,
                    Email: this.form.Email,
                    Phone: this.form.Phone,
                    Password: this.form.Password,
                    Allergies: JSON.stringify(this.form.Allergies),
                    Fridge: JSON.stringify(this.form.Fridge),
                }
                axios.post(url, para)
                .then(response => {
                    console.log(response.data)
                    this.$router.push({ name: 'Login' });
                })
                .catch(error => {
                    console.log(error.message)
                    console.error(error.response.data)
                });
            }
            }
        },
    }
</script>
    
