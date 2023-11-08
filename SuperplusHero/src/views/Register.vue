<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css');

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Montserrat', sans-serif;
}

body{
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

.container{
    background-color: #fff;
    border-radius: 30px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.35);
    position: relative;
    overflow: hidden;
    width: 768px;
    max-width: 100%;
    min-height: 480px;
}

.container p{
    font-size: 14px;
    line-height: 20px;
    letter-spacing: 0.3px;
    margin: 20px 0;
}

.container span{
    font-size: 12px;
}

.container a{
    color: #333;
    font-size: 13px;
    text-decoration: none;
    margin: 15px 0 10px;
}

.container button{
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

.container button.hidden{
    background-color: transparent;
    border-color: #fff;
}

.container form{
    background-color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    padding: 0 40px;
    height: 100%;
}

.container input{
    background-color: #eee;
    border: none;
    margin: 8px 0;
    padding: 10px 15px;
    font-size: 13px;
    border-radius: 8px;
    width: 100%;
    outline: none;
}

.form-container{
    position: absolute;
    top: 0;
    height: 100%;
    transition: all 0.6s ease-in-out;
}

.sign-in{
    left: 0;
    width: 50%;
    z-index: 2;
}

.container.active .sign-in{
    transform: translateX(100%);
}

.sign-up{
    left: 0;
    width: 50%;
    opacity: 0;
    z-index: 1;
}

.container.active .sign-up{
    transform: translateX(100%);
    opacity: 1;
    z-index: 5;
    animation: move 0.6s;
}

@keyframes move{
    0%, 49.99%{
        opacity: 0;
        z-index: 1;
    }
    50%, 100%{
        opacity: 1;
        z-index: 5;
    }
}



.toggle-container{
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

.container.active .toggle-container{
    transform: translateX(-100%);
    border-radius: 0 150px 100px 0;
}

.toggle{
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

.container.active .toggle{
    transform: translateX(50%);
}

.toggle-panel{
    position: absolute;
    width: 50%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    padding: 0 30px;
    text-align: center;
<<<<<<< Updated upstream
}
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
                        <div class="card bg-success text-white">
                            <div class="card-body">
                                <h1 class="my-5 display-3 fw-bold ls-tight mt-0">
                                Welcome to <br />
                                <span class="text-dark">Surplus Hero.</span>
                                </h1>
                                <p style="color: hsl(101, 100%, 85%)" >
                                The one-stop platform for surplus groceries and recipe generation!
                                </p>
                            </div>
                        </div>
=======
    top: 0;
    transform: translateX(0);
    transition: all 0.6s ease-in-out;
}

.toggle-left{
    transform: translateX(-200%);
}

.container.active .toggle-left{
    transform: translateX(0);
}

.toggle-right{
    right: 0;
    transform: translateX(0);
}

.container.active .toggle-right{
    transform: translateX(200%);
}

</style>
<template>
    <body>

        <div class="container">
            <div class="form-container sign-up">
                <form>
                    <h1>Create Account</h1>
                    <span>or use your email for registeration</span>
                    <input type="text" placeholder="Name">
                    <input type="email" placeholder="Email">
                    <input type="password" placeholder="Password">
                    <button>Sign Up</button>
                </form>
            </div>
            <div class="form-container sign-in">
                <form>
                    <h1>Sign In</h1>
                    <input type="email" placeholder="Email">
                    <input type="password" placeholder="Password">
                    <a href="#">Forget Your Password?</a>
                    <button>Sign In</button>
                </form>
            </div>
            <div class="toggle-container {active: isActive}">
                <div class="toggle">
                    <div class="toggle-panel toggle-left">
                        <h1>Welcome Back to SurplusHero!</h1>
                        <p>Enter your personal details to use all of site features</p>
                        <button @click= "showContainer" class="hidden">Sign In</button>
>>>>>>> Stashed changes
                    </div>
                    <div class="toggle-panel toggle-right">
                        <h1>Welcome to SurplusHero!</h1>
                        <p>Register with your personal details to use all of site features</p>
                        <button @click="hideContainer" class="hidden" >Sign Up</button>
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


export default {
    // Your component data and methods go here
    data() {
        return {
            isActive: false,
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
        showContainer() {
            this.active = true
        },
        hideContainer(){
            this.active = false
        },
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
    
