<template>
    <!-- Section: Design Block -->
    <section class="">
        <!-- Jumbotron -->
        <div class="px-4 py-5 px-md-5 text-center text-lg-start"
            style="background-color: hsl(0, 0%, 96%);background-size: cover; height: 100vh;">
            <div class="container">
                <div class="row gx-lg-5 align-items-center">
                    <div class="col-lg-6 mb-5 mb-lg-0">
                        <h1 class="my-5 display-3 fw-bold ls-tight">
                            Welcome back to <br />
                            <span class="text-success">Surplus Hero!</span>
                        </h1>
                        <!-- <p style="color: hsl(217, 10%, 50.8%)">
                        The one stop platform for surplus groceries and recipe generation!
                    </p> -->
                    </div>

                    <div class="col-lg-6 mb-5 mb-lg-0">
                        <div class="card">
                            <div class="card-body py-5 px-md-5">
                                <div class=" fw-bolder ls-tight">
                                    <h1>Login</h1>
                                </div><br>
                                <form>
                                    <!-- email input -->
                                    <div class="form-outline mb-4">
                                        <input v-model="form.UserName" type="username" id="form3Example3" class="form-control" placeholder="Username"/>
                                        <!-- <label class="form-label" for="form3Example3">Username</label> -->
                                    </div>

                                    <!-- Password input -->
                                    <div class="form-outline mb-4">
                                        <input v-model="form.Password" type="password" id="form3Example4"
                                            class="form-control" placeholder="Password"/>
                                        <!-- <label class="form-label" for="form3Example4">Password</label> -->
                                    </div>

                                    <!-- Checkbox -->
                                    <div class="form-check d-flex justify-content-center mb-4">
                                        <input class="form-check-input me-2" type="checkbox" value="" id="form2Example33"
                                            checked />
                                        <label class="form-check-label" for="form2Example33">
                                            Remember me
                                        </label>
                                    </div>

                                    <!-- Submit button -->
                                    <div class="col-md-12 mb-4">
                                        <div class="d-flex justify-content-between">
                                            <button @click="goToNext" type="submit"
                                                class="btn btn-success w-100">Login</button>
                                        </div>
                                    </div>
                                    <p style="text-align: center;">New here? Click <router-link
                                            :to="{ name: 'Register' }">here</router-link> to register </p>
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
<!-- need to firstly store user's email and password when they register, and check if they are correct before they can login -->
<script>
import axios from 'axios';
export default {
    data() {
        return {
            form: {
                UserName: '',
                Password: ''
            }
        }
    },
    methods: {
        goToNext() {
            var url = 'http://127.0.0.1:5000/register_user';
            var para = {
                Email: this.form.UserName,
                Password: this.form.Password,
            }
            axios.post(url, para)
                .then(response => {
                    console.log(response.data)
                    this.$router.push({ name: 'Home' });
                })
                .catch(error => {
                    console.log(error.message)
                    console.error(error.response.data)
                });
            // console.log(JSON.stringify(this.form));
        }
    }
}
</script>