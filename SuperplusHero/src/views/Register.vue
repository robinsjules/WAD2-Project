<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css');

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Montserrat', sans-serif;
}

body {
    background-color: #c9d6ff;
    background: linear-gradient(to right, #e2e2e2, #c9d6ff);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    height: 100vh;
    background-image: url('https://www.europenowjournal.org/wp-content/uploads/2019/04/shutterstock_321864554.jpg');
    background-size: cover;
}

.container {
    background-color: #fff;
    border-radius: 30px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.35);
    position: relative;
    overflow: hidden;
    width: 768px;
    max-width: 100%;
    min-height: 690px;
}

.container p {
    font-size: 14px;
    line-height: 20px;
    letter-spacing: 0.3px;
    margin: 20px 0;
}

.container span {
    font-size: 12px;
}

.container a {
    color: #333;
    font-size: 13px;
    text-decoration: none;
    margin: 15px 0 10px;
}

.container button {
    background-color: #436a43;
    color: #fff;
    font-size: 12px;
    padding: 10px 45px;
    border: 1px solid transparent;
    border-radius: 8px;
    font-weight: 600;
    letter-spacing: 0.5px;
    text-transform: uppercase;
    margin-top: 10px;
    cursor: pointer;
}

.container button.hidden {
    background-color: transparent;
    border-color: #fff;
}

.container form {
    background-color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    padding: 0 40px;
    height: 100%;
}

.container input {
    background-color: #eee;
    border: none;
    margin: 8px 0;
    padding: 10px 15px;
    font-size: 13px;
    border-radius: 8px;
    width: 100%;
    outline: none;
}

.form-container {
    position: absolute;
    top: 0;
    height: 100%;
    transition: all 0.6s ease-in-out;
}

.sign-in {
    left: 0;
    width: 50%;
    z-index: 2;
}

.container.active .sign-in {
    transform: translateX(100%);
}

.sign-up {
    left: 0;
    width: 50%;
    opacity: 0;
    z-index: 1;
}

.container.active .sign-up {
    transform: translateX(100%);
    opacity: 1;
    z-index: 5;
    animation: move 0.6s;
}

@keyframes move {

    0%,
    49.99% {
        opacity: 0;
        z-index: 1;
    }

    50%,
    100% {
        opacity: 1;
        z-index: 5;
    }
}

.toggle-container {
    position: absolute;
    top: 0;
    left: 50%;
    width: 50%;
    height: 100%;
    overflow: hidden;
    transition: all 0.6s ease-in-out;
    border-radius: 150px 0 0 100px;
    z-index: 1000;
}

.container.active .toggle-container {
    transform: translateX(-100%);
    border-radius: 0 150px 100px 0;
}

.toggle {
    background-color: #512da8;
    height: 100%;
    background: linear-gradient(to right, #5eab69, #445043);
    color: #fff;
    position: relative;
    left: -100%;
    height: 100%;
    width: 200%;
    transform: translateX(0);
    transition: all 0.6s ease-in-out;
}

.container.active .toggle {
    transform: translateX(50%);
}

.toggle-panel {
    position: absolute;
    width: 50%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    padding: 0 30px;
    text-align: center;
    top: 0;
    transform: translateX(0);
    transition: all 0.6s ease-in-out;
}

.toggle-left {
    transform: translateX(-200%);
}

.container.active .toggle-left {
    transform: translateX(0);
}

.toggle-right {
    right: 0;
    transform: translateX(0);
}

.container.active .toggle-right {
    transform: translateX(200%);
}

@media screen and (max-width: 768px) {

    /* Styles for screens with a maximum width of 768px */
    .container {
        width: 100%;
        border-radius: 0;
    }

    .form-container {
        position: relative;
        height: auto;
        transition: none;
    }

    .sign-up,
    .sign-in {
        width: 100%;
        opacity: 1;
        transform: translateX(0);
    }

    .toggle-container {
        display: none;
    }

    .container.active .sign-in {
        transform: translateX(100%);
    }

    .container.active .sign-up {
        transform: translateX(100%);
        opacity: 1;
        z-index: 5;
        animation: move 0.6s;
    }

    .container.active .toggle-container {
        transform: translateX(-100%);
        border-radius: 0 150px 100px 0;
    }

    .container.active .toggle {
        transform: translateX(50%);
    }

    .container.active .toggle-left {
        transform: translateX(0);
    }

    .container.active .toggle-right {
        transform: translateX(200%);
    }
}
</style>
<template>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>

    <body>
        <div>
            <div class="container" :class="containerClasses">
                <div class="form-container sign-up">
                    <form @submit.prevent="goToNext">
                        <img src="../../src/assets/appLogo.png" style="max-width: 80px; max-height: 80px;">
                        <h1 style="font-weight: bolder;">Sign Up</h1><br>
                        <select v-model="form.UserType" class="form-control" id="dropdown">
                            <option value="What type of user are you?" selected>What type of user are you?</option>
                            <option value="Consumer">Consumer</option>
                            <option value="Business">Business</option>
                        </select>
                        <input v-model="form.UserName" type="text" placeholder="Username">
                        <input v-model="form.Email" type="email" id="form3Example3" class="form-control"
                            placeholder="Email Address" />
                        <input v-model="form.Phone" type="phonenum" id="form3Example4" class="form-control"
                            placeholder="Phone Number" />
                        <input v-model="form.Password" type="password" id="form3Example5" class="form-control"
                            placeholder="Password" />
                        <textarea v-if="form.UserType === 'Consumer'" cols="4" rows="5" v-model="form.Fridge" type="text"
                            id="Fridge" class="form-control" placeholder="Items in your fridge (Eg. Banana)" />
                        <button @click="goToNext" @click.prevent="activate">submit</button>
                    </form>
                </div>
                <div class="form-container sign-in">
                    <form @submit.prevent="login">
                        <img src="../../src/assets/appLogo.png" style="max-width: 80px; max-height: 80px;">
                        <h1 style="font-weight: bolder;">Sign In</h1><br>
                        <input v-model="Email" type="email" id="form3Example3" class="form-control" placeholder="Email" />
                        <input v-model="Password" type="password" id="form3Example4" class="form-control"
                            placeholder="Password" />
                        <a href="#">Forgot Your Password?</a>
                        <button>Sign In</button>
                    </form>
                </div>
                <div class="toggle-container">
                    <div class="toggle active">
                        <div class="toggle-panel toggle-left">
                            <h1 style="font-weight: bolder;">Welcome to SurplusHero!</h1>
                            <p>Already have an account? Sign in here.</p>
                            <button @click.prevent="deactivate" class="hidden">Sign In</button>
                        </div>
                        <div class="toggle-panel toggle-right">
                            <h1 style="font-weight: bolder;">Welcome Back to SurplusHero!</h1>
                            <p>Don't have an account? Sign up now!</p>
                            <button @click.prevent='activate' class="hidden">Sign Up</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </body>
    <!-- Section: Design Block -->
    <!-- Section: Design Block -->
</template>
<script>
import axios from 'axios';
import { signIn } from "@/router/signIn";

export default {
    // Your component data and methods go here
    data() {
        return {
            Email: '',
            Password: '',
            containerClasses: {
                active: false
            },
            form: {
                UserType: 'What type of user are you?',
                UserName: '',
                Email: '',
                Phone: '',
                Password: '',
                Fridge: '',
            }
        }
    },
    methods: {
        activate() {
            this.containerClasses.active = true;
        },
        deactivate() {
            this.containerClasses.active = false;
        },
        goToNext() {
            if (this.form.UserType === 'What type of user are you?' && this.form.Password === '' && this.form.UserName === '' && this.form.Email === '' && this.form.Phone === '') {
                alert('Please fill up the form!')
            }
            else if (this.form.UserType === 'What type of user are you?') {
                alert('Please select a user type')
            }
            else if (this.form.Password === '') {
                alert('Please enter a password')
            }
            else if (this.form.Password.length < 8) {
                alert('Minimum Password length is 8')
            }
            else if (this.form.UserName === '') {
                alert('Please enter a username!')
            }
            else if (this.form.Email === '') {
                alert('Please enter your email!')
            }
            else if (this.form.Phone === '') {
                alert('Please enter your phone number!')
            }
            else {
                var url = 'http://127.0.0.1:5000/register_user';
                var para = {
                    UserType: this.form.UserType,
                    UserName: this.form.UserName,
                    Email: this.form.Email,
                    Phone: this.form.Phone,
                    Password: this.form.Password,
                    Fridge: JSON.stringify(this.form.Fridge),
                }
                axios.post(url, para)
                    .then(response => {
                        console.log(response.data)
                        this.$router.push({ name: 'Profile' });
                    })
                    .catch(error => {
                        console.log(error.message)
                        console.error(error.response.data)
                    });
            }
        },
        async login() {
            if (this.Password === '' && this.Email === '') {
                alert('Please enter your email and password!')
            }
            else if (this.Email === '') {
                alert('Please enter your email!')
            }
            else if (this.Password === '') {
                alert('Please enter your password!')
            }
            else {
                try {
                    const response = await signIn(this.Email, this.Password);
                    console.log('Response:', response);
                    if (response.status === 200) {
                        // Successful authentication
                        this.$router.push({ path: '/home' });
                    } else {
                        console.error('Authentication failed');
                        // Handle authentication failure
                    }
                } catch (error) {
                    console.error('Error signing in:', error);
                    alert('Wrong Email/Password! Please try again.')
                    // Handle sign-in error
                }
            }
        }
    },
}
</script>
    

