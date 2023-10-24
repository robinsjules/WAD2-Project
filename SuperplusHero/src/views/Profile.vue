
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
    

        <div id="app">

  <div class="row around-xs">
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
    <h3>
        Result: {{ foodPreferences }}
    </h3>

    
    </div>

</template>

<script>
    export default{
    data() {
        return {
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
            }]
            }
        }
    };
</script>
<script href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous"></script>