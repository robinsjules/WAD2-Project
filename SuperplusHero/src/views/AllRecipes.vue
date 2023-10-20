<template>
    <!-- All Recipes Page -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">

    <form>
        <div class="container-fluid">
            <h1>
                <span class="text-primary" >All Recipes</span>
            </h1>

            <div class="form-group">
                
                    <label class="fw-bold"></label>
                    <div class="form-group">
                    <div class="col-6 input-group">
                        <input type="search" class="form-control me-2" placeholder="Search Recipes..." name="find_recipe">

                        
                            <!-- Example single danger button --> 
                            <div class="col-4 btn-group mx-2"> 
                                <select class="form-select" aria-label="Default select example"> 
                                <option selected>Filter by cuisine</option> 
                                <option value="western" name="western">Western</option> 
                                <option value="chinese" name="chinese">Chinese</option> 
                                <option value="indian" name="indian">Indian</option>
                                <option value="malay" name="malay">Malay</option> 
                                <option value="japanese" name="japanese">Japanese</option>
                                <option value="korean" name="korean">Korean</option>
                                <option value="thai" name>Thai</option>
                                <option value="french">French</option> 
                            </select>
                            </div> 

                            
                            
                            
                        
                        
                        <span class="col-2 input-group-btn">
                            <button class="btn btn-outline-primary" type="search" style="width: 100%;" >Search</button>
                        </span>
                    </div>
                    </div>
                    
                    
            </div>
        </div>
    </form>
    


</template>
<script href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootspanstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous"></script>
