
<template>
    
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
    <!-- <h2>Profile Page</h2> -->
        
    <div class="col-lg-6 mb-5 mb-lg-0">
                    <div class="card">
                        <div class="card-body py-5 px-md-5">
                            <form>
    <div id="app">
        <div class="row around-xs">
            <div class="text-center">
            <img src="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png" alt="Admin" class="rounded-circle p-1 bg-primary" width="200">
            </div>
            <div class="profile-picture">
                <img :src="userPicture" alt="User's Profile Picture" />
                <input type="file" @change="uploadPicture" accept="image/*" />
            </div>
            <div class="form-outline mb-4">
                <!-- need to include original name in box-->
                <input type="text" class="form-control" id="fName">
                <label for="fName">First Name</label>
            </div>
            <div class="form-outline mb-4">
                <!-- need to include original name in box-->
                <input type="text" class="form-control" id="lName">
                <label for="lName">Last Name</label>
            </div>
            <div class="form-outline mb-4">
                <!-- need to include original email in box-->
                <input type="email" class="form-control" id="email">
                <label for="email">Email Address</label>
            </div>
            <div class="form-outline mb-4">
                <!-- need to include original phone num in box-->
                <input type="name" class="form-control" id="phoneNum">
                <label for="phoneNum">Phone Number</label>
            </div>
            <div class="form-outline mb-4">
                <input type="password" class="form-control" id="password">
                <label for="password">Enter Old Password</label>
            </div>
            <div class="form-outline mb-4">
                <input type="text" class="form-control" id="newPassword">
                <label for="newPassword">Enter New Password</label>
            </div>
            <div class="form-outline mb-4">
                <input type="text" class="form-control" id="newPassword2">
                <label for="newPassword2">Re-enter New Password</label>
                <!-- need to check newpw2 against newpw1-->
            </div>
            <div>
            Dietary Preferences
            <div v-for="(preference,index) in dPreferences" :key="index">
                <label class="container text-white bg-primary"> {{preference.name}} &nbsp; </label>
                <input type="checkbox" :value="preference.value" v-model="foodPreferences">
            </div>
            <br/>
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
            userPicture:"",
            fName:"",
            lName:"",
            email:"",
            phoneNum:"",
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