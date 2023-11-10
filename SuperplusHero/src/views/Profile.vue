<style scoped>
    .content{
    margin-top: 80px;
    }

    * {
    font-family: "Montserrat";
    }
    
    .profile-form {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 20px;
    }   
    .profile-picture img {
    max-width: 200px;
    max-height: 200px;
    }
    .image-container {
    margin-bottom: 10px; 
    }
    .file-input input[type="file"] {
    display: none;
    }
    .file-input {
    text-align: center;
    }
    .remove-button {
    margin-top: 5px;
    }

    .fixed-position{
        margin:auto;
    }

    @media (min-width: 992px) {        
        .fixed-position{
        position: fixed;
        }
    }

</style>
<template>
    <div class="content">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
    <!-- <h2>Profile Page</h2> -->
    
    <section class="">
      <!-- Jumbotron -->
        <div class="px-4 py-5 px-md-5 text-center text-lg-start" style="background-color: hsl(0, 0%, 96%)">
            <div class="container">
                <div class="row gx-lg-5 justify-content-center">
                    <div class="col-lg-4 mb-5 mb-lg-0">
                        <div class="fixed-position">
                            <h1 span class="my-5 display-3 fw-bold ls-tight">
                                <span>Profile of<br/> our <br/></span>
                                <span class="text-success">Surplus <br/>Hero!</span>
                            </h1>
                        </div>
                    </div>
    <!-- card -->
    <div class="mx-auto col-lg-6 mb-5 mb-lg-0 ">
            <div class="card" style="border: 3px solid rgb(10, 160, 10);">
                <div class="card-body rounded py-5" style="background-color:rgb(237, 243, 235);">
                    <form id="profileEdit" class="my-4" autocomplete="on" @submit.prevent="">
                        <div id="app">
                            <div class="profile-form">
                                <div class="profile-picture">
                                    <div class="image-container">
                                        <img :src="userPicture" alt="User's Profile Picture" class="rounded-circle p-1" style="background-color: rgb(10, 160, 10)"/>
                                    </div>
                                    <div class="file-input">
                                        <label for="file-upload" class="btn btn-success" style="background-color:rgb(10, 160, 10)">Choose File</label>
                                        <input id="file-upload" type="file" @change="uploadPicture" accept="image/*" />
                                    </div>
                                </div>
                            </div>
                            <br/>
                            <div class="form-outline mb-4">
                                <!-- need to include original email in box-->
                                <input type="email" class="form-control" id="email" v-model="email" autocomplete="on">
                                <label for="email">Email Address</label>
                            </div>
                            <div class="form-outline mb-4">
                                <input type="number" class="form-control" id="postalCode" v-model="postalCode">
                                <label for="postalCode">Postal Code</label>
                            </div>
                            <div class="form-outline mb-4">
                                <!-- need to include original phone num in box-->
                                <input type="name" class="form-control" id="phoneNum" v-model="phoneNum">
                                <label for="phoneNum">Phone Number</label>
                            </div>
                            <hr/>
                            <div>
                                <h4>Change Password</h4>
                                <div class="form-group mb-4">
                                    <input type="password" id="password" v-model="password" class="form-control" />
                                    <label for="password">Old Password</label>
                                </div>
                                <div class="row">
                                    <div class="form-group mb-4 col-md-6">
                                        <input type="password" id="newPassword" v-model="newPassword" class="form-control" />
                                        <label for="newPassword">New Password</label>
                                    </div>
                                    <div class="form-group mb-4 col-md-6">
                                        <input type="password" id="confirmPassword" v-model="confirmPassword" class="form-control" />
                                        <label for="confirmPassword">Re-enter New Password</label>
                                    </div>
                                </div>
                            </div>
                            <hr/>
                            <div>
                                Dietary Preferences:
                                <div class="container">
                                    <div class="row">
                                        <div v-for="(preference, index) in dPreferences" :key="index" class="col-sm text-white rounded d-flex justify-content-center align-items-center m-1" style="background-color:rgb(10, 160, 10)">
                                            <div class="form-group form-check">
                                                <input class="form-check-input" type="checkbox" :value="preference.value" :id="preference.value" v-model="foodPreferences" />
                                                <label class="form-check-label" :for="preference.value">{{ preference.name }}</label>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <br/>
                            <div>
                                <div class="row">
                                    <div class="form-group col-sm-8">
                                        <input type="text" v-model="newIntolerances" class="form-control" id="intoleranceInput"/>
                                        <label for="intoleranceInput" >Intolerance</label>
                                    </div>
                                    <div class="col-sm-4">
                                        <button @click="addIntolerance" type="submit" class="btn btn-success" style="height:36px; width:100px;background-color:rgb(10, 160, 10)">Add</button>
                                    </div>
                                </div>
                                <br/>
                                <ul>
                                    <li v-for="(intolerance, index) in intolerances" :key="index">
                                        {{ intolerance }}
                                        <button @click="removeIntolerance(index)" type="button" class="btn btn-danger remove-button" style="background-color:rgb(10, 160, 10)">Remove</button>
                                    </li>
                                </ul>
                            </div>
                            <button @click= "updateProfile" class="btn btn-success btn-block mt-4" type="submit" value="submit" style="background-color:rgb(10, 160, 10)"> Save changes </button>&nbsp;
                            <button @click= "logoutProfile" class="btn btn-success mt-4" type="button" value= true style="background-color:rgb(10, 160, 10)">Log out</button>        
                        </div>
                    </form>
                </div>
            </div>
    </div>
                </div>
            </div>
        </div>
    </section>
</div>
</template>


<script>
import axios from 'axios';
import Cookies from 'js-cookie';

export default {
  data() {
    return {
        //need to add cookies to store username since not editable
        userName: 'test3',
        userPicture:'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
        email: '',
        phoneNum: '',
        postalCode: '',
        password: '', 
        newPassword: '',
        confirmPassword: '',
        foodPreferences: [],
        dPreferences: [{
            name: 'Halal',
            value: 'halal'
            },
            {
            name: 'Vegetarian',
            value: 'vegetarian'
            },
            {
            name: 'Vegan',
            value: 'vegan'
            },
            {
            name: 'Gluten-free',
            value: 'gluten free'
            },
            {
            name: 'Keto',
            value: 'ketogenic'
            }],
        intolerances:[],
        newIntolerances:'',
        updateurl: `http://127.0.0.1:5000/update_profile/${this.userName}`,
        geturl:`http://127.0.0.1:5000/get_profile/${this.userName}`
        };
    },
    //get userName from cookies 
    // created() {
    // // Get the 'username' cookie and set it in the component's data
    //     const userNameFromCookie = Cookies.get('username');
    //     if (userNameFromCookie) {
    //     this.userName = userNameFromCookie;
    //     }
        
    //     axios.get(this.geturl)
    //   .then((response) => {
    //     const retrievedUserData = response.data;

    //     // Assign the data to the component's data properties
    //     this.userPicture = retrievedUserData.UserPicture;
    //     this.email = retrievedUserData.Email;
    //     this.phoneNum = retrievedUserData.Phone;
    //     this.postalCode = retrievedUserData.PostalCode;

    //     // Convert JSON strings to lists of objects
    //     this.foodPreferences = JSON.parse(retrievedUserData.FoodPreferences);
    //     this.intolerances = JSON.parse(retrievedUserData.Allergies);
    //   })
    //   .catch((error) => {
    //     console.error(error); // Log the error for debugging
    //     alert('Error in retrieving data');
    //   });
    // },

    // mounted() {
    // // Make a GET request to retrieve the user data
    // axios.get(`http://127.0.0.1:5000/get_profile/${this.userName}`)
    //   .then((response) => {
    //     const retrievedUserData = response.data;

    //     // Assign the data to the component's data properties and display
    //     this.userPicture = retrievedUserData.UserPicture;
    //     this.email = retrievedUserData.Email;
    //     this.phoneNum = retrievedUserData.Phone;
    //     this.postalCode = retrievedUserData.PostalCode;
        
    //     // Convert JSON strings to lists of objects
    //     this.foodPreferences = JSON.parse(retrievedUserData.FoodPreferences);
    //     this.intolerances = JSON.parse(retrievedUserData.Allergies);
    //   })
    //   .catch((error) => {
    //     // Handle errors
    //     alert('Error in retrieving data')
    //   })
    // },
    methods: {
        uploadPicture(event) {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = (e) => {
                this.userPicture = e.target.result;
                };
                reader.readAsDataURL(file);
                }
        },
        updateProfile() {
        // Check if new passwords is filled and if they match
            if (this.newPassword && this.newPassword !== this.confirmPassword) {
                alert('New passwords do not match.');
                return;
            }
            const updatedData = {
                UserPicture: this.userPicture,
                Email: this.email,
                Phone: this.phoneNum,
                PostalCode: this.postalCode,
                FoodPreferences: this.foodPreferences,
                Allergies: this.intolerances
            }
            // Perform an Axios GET request to your server to check the old password
            // Check if the old password is not blank
            if (this.password) {
                // Perform an Axios GET request to your server to check the old password
                axios.get(this.geturl, {
                    params: {
                    Password: this.password,
                    },
                })
                .then((response) => {
                    console.log("error1");
                    // Include newPassword in the data if it's not blank
                    updatedData.Password = this.newPassword;
                    // The old password is correct
                    // Perform an Axios PUT request to update the password in the database
                    axios.put(this.updateurl, updatedData)
                    .then((response) => {
                        console.log("error2");
                        alert('Profile updated successfully');
                    })
                    .catch((error) => {
                        console.log("error3");
                        alert('Error updating the profile');
                    });
                })
                .catch((error) => {
                    console.log("error4");
                    alert('Incorrect old password');
                });
            } 
            else {
                // If old password is blank, update the profile data without changing the password
                axios.put(this.updateurl, updatedData)
                .then((response) => {
                    console.log("error5");
                    alert('Profile updated successfully');
                })
                .catch((error) => {
                    console.log("error6");
                    alert('Error updating the profile');
                });
            }
        },
            logoutProfile() {
            alert("You have signed out successfully!")
            this.$router.push({ name: 'Register' });
        },
            addIntolerance(event) {
            event.preventDefault(); // Prevent the default form submission behavior
            this.intolerances.push(this.newIntolerances);
            this.newIntolerances = ''; // Clear the input field
        },
            removeIntolerance(index) {
            this.intolerances.splice(index, 1);
        },
    }
}
</script>

<script href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous"></script>