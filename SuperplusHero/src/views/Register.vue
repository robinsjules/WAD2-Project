<template>
    <!-- <h2>Register Page</h2> --> 
    <!-- Section: Design Block -->
    <section class="">
        <!-- Jumbotron -->
        <div class="px-5 py-5 px-md-5 text-center text-lg-start" style="background-color: hsl(0, 0%, 96%)">
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
                                <div class=" fw-bolder ls-tight"><h1>Create Account</h1></div><br>
                                <form>
                                    <!-- 2 column grid layout with text inputs for the first and last names -->
                                    <div class="row">
                                        <div class="col-md-6 mb-4">
                                            <div class="form-outline">
                                                <input type="text" id="form3Example1" class="form-control" placeholder="First Name" />
                                                <!-- <label class="form-label" for="form3Example1">First name</label> -->
                                            </div>
                                        </div>
                                        <div class="col-md-6 mb-4">
                                            <div class="form-outline">
                                                <input type="text" id="form3Example2" class="form-control" placeholder="Last Name" />
                                                <!-- <label class="form-label" for="form3Example2">Last name</label> -->
                                            </div>
                                        </div>
                                    </div>

                                    <!-- Email input -->
                                    <div class="form-outline mb-4">
                                        <input type="email" id="form3Example3" class="form-control" placeholder="Email Address"/>
                                        <!-- <label class="form-label" for="form3Example3">Email address</label> -->
                                    </div>

                                    <!-- Phone Number -->
                                    <div class="form-outline mb-4">
                                        <input type="phonenum" id="form3Example3" class="form-control" placeholder="Phone Number"/>
                                        <!-- <label class="form-label" for="form3Example3">Phone Number</label> -->
                                    </div>

                                    <!-- Password input -->
                                    <div class="form-outline mb-4">
                                        <input type="password" id="form3Example4" class="form-control" placeholder="Password"/>
                                        <!-- <label class="form-label" for="form3Example4">Password</label> -->
                                    </div>

                                    <!-- Checkbox -->
                                    <div class="form-check d-flex justify-content-center mb-4">
                                        <input class="form-check-input me-2" type="checkbox" value="" id="form2Example33"
                                            checked />
                                        <label class="form-check-label" for="form2Example33">
                                            Subscribe to our newsletter
                                        </label>
                                    </div>
                                    <!-- Submit button -->
                                    <button @click="goToNext" type="submit" class="btn btn-success btn-block mb-4">
                                        Next
                                    </button>
                                    <p style="text-align: center;">Already have an account? Click <router-link :to="{ name: 'Login' }">here</router-link> to log in</p>

                                    <!-- Register buttons -->
                                    <!-- <div class="text-center">
                                        <p>or sign up with:</p>
                                        <button type="button" class="btn btn-link btn-floating mx-1">
                                            <i class="fab fa-facebook-f"></i>
                                        </button>

                                        <button type="button" class="btn btn-link btn-floating mx-1">
                                            <i class="fab fa-google"></i>
                                        </button>

                                        <button type="button" class="btn btn-link btn-floating mx-1">
                                            <i class="fab fa-twitter"></i>
                                        </button>

                                        <button type="button" class="btn btn-link btn-floating mx-1">
                                            <i class="fab fa-github"></i>
                                        </button>
                                    </div> -->
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
export default {
  // Your component data and methods go here
  methods: {
    goToNext() {
    this.$router.push({ name: 'Register2' });
    }
  }
}
</script>
<!-- for register, have to make sure all fields are compulsory, and must be filled in properly
eg. email must have @ sign
Password must be 8-10 characters long
phone number cannot have any letters
name and last name cannot have any numbers -->