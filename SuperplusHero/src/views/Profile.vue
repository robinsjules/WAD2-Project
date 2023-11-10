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
    width:200px;
    height:200px;
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
    
    <section class="">
      <!-- Jumbotron -->
        <div class="px-4 py-5 px-md-5 text-center text-lg-start" style="background-color:rgb(237, 243, 235)">
            <div class="container">
                <div class="row gx-lg-5 justify-content-center">
                    <div class="col-lg-4 mb-5 mb-lg-0">
                        <div class="fixed-position">
                            <h1 span class="my-5 display-3 fw-bold ls-tight">
                                <span>Profile of<br/> our <br/></span>
                                <span style="color:rgb(10, 160, 10)">Surplus <br/>Hero!</span>
                            </h1>
                        </div>
                    </div>
    <!-- card -->
    <div class="mx-auto col-lg-6 mb-5 mb-lg-0 ">
            <div class="card" style="border: 3px solid rgb(10, 160, 10); width:500px">
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
                                <input type="email" class="form-control" id="email" v-model="email" autocomplete="on" placeholder="robinsjules2019@gmail.com">
                                <label for="email">Email Address</label>
                            </div>
                            <div class="form-outline mb-4">
                                <!-- need to include original phone num in box-->
                                <input type="name" class="form-control" id="phoneNum" v-model="phoneNum" placeholder="88889999">
                                <label for="phoneNum">Phone Number</label>
                            </div>
                            <hr/>
                            <div>
                                <p>Change Password</p>
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
export default {
    data() {
        return {
            userPicture:'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png',
            email: '',
            phoneNum: '',
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
        data:[],
        checkPassword:''};
  },
    mounted() {
        this.getProfile();
    },
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
        async getProfile(){
            try {
            const userName = 'julesrobins';
            const response = await axios.get(`http://127.0.0.1:5000/get_profile/${userName}`);
            console.log('Fetched User Data:', response.data);
            this.data = response.data[0];
            this.userPicture=this.data.UserPicture;
            this.email=this.data.Email;
            this.phoneNum=this.data.Phone;
            this.intolerances=this.data.Allergies;
            this.checkPassword=this.data.Password;
        } catch (error) {
            console.error('Error fetching items:', error);
        }},
        async updateProfile(){
            console.log(this.checkPassword);
            if(this.password && this.password!==this.checkPassword){
                alert('Old password you have keyed in is incorrect.');
                return;
            }
            if (this.newPassword && this.newPassword !== this.confirmPassword) {
                alert('New passwords do not match.');
                return;
            }
            try {
            const userName = 'julesrobins';
            const updatedData = {
                'UserPicture':this.userPicture,
                'Email':this.email,
                'Phone':this.phoneNum,
                'FoodPreferences':this.foodPreferences,
                'Allergies':this.intolerances,
                }
            if (this.password && this.newPassword){
                updatedData['Password']=this.newPassword;
            }
            const response = await axios.put(`http://127.0.0.1:5000/update_profile/${userName}`, updatedData);
            console.log('Sending User Data:', response.data);
            alert('Profile updated successfully');
        } catch (error) {
            console.error('Error updating profile', error);
        }
        },
            logoutProfile() {
            alert("You have signed out successfully!")
            this.$router.push({ name: 'Register' });
        },
            addIntolerance(event) {
            event.preventDefault(); 
            this.intolerances.push(this.newIntolerances);
            this.newIntolerances = '';
        },
            removeIntolerance(index) {
            this.intolerances.splice(index, 1);
        },
    }
}
</script>

<script href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous"></script>