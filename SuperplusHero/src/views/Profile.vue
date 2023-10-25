
<template>
    
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
    <!-- <h2>Profile Page</h2> -->
    
    <section class="">
      <!-- Jumbotron -->
      <div class="px-4 py-5 px-md-5 text-center text-lg-start" style="background-color: hsl(0, 0%, 96%)">
          <div class="container">
              <div class="row gx-lg-5 justify-content-center">
                  <div class="col-lg-4 mb-5 mb-lg-0">
                      <h1 class="my-5 display-3 fw-bold ls-tight">
                          Profile of our <br />
                          <span class="text-primary">Surplus Hero!</span>
                      </h1>
                  </div>
    <!-- card -->
    <div class="mx-auto col-lg-6 mb-5 mb-lg-0 ">
            <div class="card">
                <div class="card-body py-5 px-md-5">
                    <form>
                        <div id="app">
                                <div class="text-center">
                                <img src="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png" alt="Admin" 
                                class="rounded-circle p-1 bg-primary mx-auto" width="200">
                                </div>
                                    <br/><br/>
                                <div class="profile-picture">
                                    <img :src="userPicture" alt="Change Profile Picture" />
                                    <input type="file" @change="uploadPicture" accept="image/*" />
                                </div>
                                <br/>
                                <div class="row">
                                    <div class="form-outline mb-4 col-md-6">
                                        <!-- need to include original name in box-->
                                        <input type="text" class="form-control" id="fName">
                                        <label for="fName">First Name</label>
                                    </div>
                                    <div class="form-outline mb-4 col-md-6">
                                        <!-- need to include original name in box-->
                                        <input type="text" class="form-control" id="lName">
                                        <label for="lName">Last Name</label>
                                    </div>
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
                                <div class="row">
                                    <div class="form-outline mb-4 col-md-6">
                                        <input type="text" class="form-control" id="newPassword">
                                        <label for="newPassword">Enter New Password</label>
                                    </div>
                                    <div class="form-outline mb-4 col-md-6">
                                        <input type="text" class="form-control" id="newPassword2">
                                        <label for="newPassword2">Re-enter New Password</label>
                                        <!-- need to check newpw2 against newpw1-->
                                    </div>
                                </div>
                                <div>
                                    Dietary Preferences
                                    <div class="container">
                                        <div class="row">
                                            <div v-for="(preference,index) in dPreferences" :key="index" class="col-sm text-white bg-primary rounded d-flex justify-content-center m-1">
                                                <input type="checkbox" :value="preference.value" v-model="foodPreferences"> &nbsp;
                                                <label>
                                                    {{preference.name}} 
                                                </label>
                                            </div>
                                        </div>
                                    </div>
                                    <br/>
                                </div>
                                <div >

                                </div>
                                <button class="btn btn-primary btn-block mb-4" type="submit" value="submit"> Save changes </button>
                                <button class="btn btn-primary mb-4" type="submit" value="logout">Log out</button>
                                    
                        </div>
                    </form>
                </div>
            </div>
    </div>
                </div>
            </div>
        </div>
    </section>
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
            },
            {
            name: 'Gluten-free',
            value: 'gluten free'
            },
            {
            name: 'Keto',
            value: 'ketogenic'
            }],
            save:""
            }
        },
        computed: {
            rowsOfThree(){
                
            }
        }
    };
</script>
<script href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous"></script>