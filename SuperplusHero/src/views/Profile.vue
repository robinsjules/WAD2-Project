
<template>
    
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
    <!-- <h2>Profile Page</h2> -->
    <!-- navbar -->
    <nav class="navbar navbar-expand-lg navbar-success bg-success   ">
            <a class="navbar-brand" href="#"><img src="" alt="Logo" width="80" height="30"></a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <a class="nav-link" href="#"><img src="../assets/comm.png" alt="Community" width="50" height="50"></a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#"><img src="../assets/cart.png" alt="Cart" width="50" height="50"></a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#"><img src="../assets/fridge.png" alt="Fridge" width="50" height="50"></a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#"><img src="../assets/profile.png" alt="Profile" width="50" height="50"></a>
                    </li>
                </ul>
            </div>
    </nav>
        
    <div class="col-lg-6 mb-5 mb-lg-0">
                    <div class="card">
                        <div class="card-body py-5 px-md-5">
                            <form>
    <div id="app">
        <!-- <div style="text-align: center;">
            <div style="display: inline-block; text-align: left;">
                Centered<br />
                Content<br />
                That
            </div>
        </div> -->
        <div class="row around-xs">
            <div class="text-center">
            <img src="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png" alt="Admin" class="rounded-circle p-1 bg-primary" width="200">
            </div>
            <div class="profile-picture">
                <img :src="userPicture" alt="User's Profile Picture" />
                <input type="file" @change="uploadPicture" accept="image/*" />
            </div>
            <p>
                First Name: 
                <input v-model="fName">
            </p>
            <p>
                Last Name: 
                <input v-model="lName">
            </p>
            <p>
                Email: 
                <input v-model="email" type="email">
            </p>
            <p>
                Phone Number: 
                <input v-model="phonenum" type="number">
            </p>
            <p>
                <h5>Change Password:</h5> 
                Old Password:  
                <input v-model="password" type="password">
            </p>
            <p>
                New Password: 
                <input v-model="password" type="password">
            </p>
            <p>
                Confirm New Password: 
                <input v-model="password" type="password">
            </p>
            <div>
            <h4>Dietary Preferences</h4>
            <div v-for="(preference,index) in dPreferences" :key="index">
                <label>{{preference.name}}</label>
                <input type="checkbox" :value="preference.value" v-model="foodPreferences">
            </div>
            </div>
            <div>
            <h4>Dietary Preferences</h4>
            <select v-model="foodPreferences" multiple>
                <option :value="preference.value" v-for="(preference,index) in dPreferences" :key="index">{{preference.name}}</option>
            </select>
            </div>
        </div>
        <!-- test to see value -->
        <!-- <h3>
            Result: {{ foodPreferences }}
        </h3> -->
            <button type="submit" class="btn btn-primary btn-block mb-4" name="save"> Save </button>
                
    </div>
                            </form>
                        </div>
                    </div>
    </div>

</template>

<script>
    export default{
    data() {
        return {
            // fetch first and last name of user from data stored
            userPicture:"",
            fName:"",
            lName:"",
            email:"",
            phonenum:"",
            password:[],
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
            }],
            save:""
            }
        }
    };
</script>
<script href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous"></script>