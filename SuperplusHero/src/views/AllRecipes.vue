<style scoped>
/* img {
    width: 260px;
    height:200px
} */
.card-img-top {
    width: 20vh;
    height: 200px;
    object-fit: cover;
}
</style>
<template>
    <!-- All Recipes Page -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
    
    <!-- Start of Search Bar -->
    <form>
        <div class="container-fluid">
            <h1 class="text-success" style="font-weight: bold;">
                All Recipes
            </h1>

            <div class="form-group">
                    <div class="row justify-content-center">
                    <div class="col-md">
                    <div class="input-group">
                        <input type="text" class="form-control" placeholder="Search Recipe..">
                    
                        <div class="input-group-append">
                            <button class="btn btn-success" type="button">Search</button>
                        </div>
                    </div>
                    </div>
                    </div>
                </div>
                        <!-- Filter Button Start --> 
                        <div class="col-4 btn-group mt-2"> 
                            <select class="form-select" aria-label="Default select example"> 
                            <option selected>Filter by cuisine</option>
                            <option value="local" name="local">Local (Singapore)</option>
                            <option value="western" name="western">Western</option> 
                            <option value="chinese" name="chinese">Chinese</option> 
                            <option value="indian" name="indian">Indian</option>
                            <option value="malay" name="malay">Malay</option> 
                            <option value="japanese" name="japanese">Japanese</option>
                            <option value="korean" name="korean">Korean</option>
                            <option value="thai" name>Thai</option>
                            <option value="french">French</option> 
                        </select>
                        <!-- Filter Button End  -->
                        
                        
                        
                    
                    
                    <!-- <input type="button" class="col-2 input-group-btn"> -->
                        
                    
                
                </div>
                
                
        </div>
        
    </form>


    
<section>
    <div class="container-fluid">
        <div class="row justify-content-center">
            <!-- BS card 1: Start --> 
            
            <div class="card m-2 pt-2" style="width: 18rem;"> 
                <img src="./images/recipes/laksa.jpg" class="card-img-top" alt="..." > 
                <div class="card-body"> 
                    <h5 class="card-title">Laksa</h5> 
                    <p class="card-text">Some quick example text to make up the bulk of the card's content.</p>  
                </div> 
                
                <div class="card-body"> 
                    <button type="button" class="btn btn-outline-success">Read more</button>
                </div> 
            </div>
            <!-- BS card: End --> 

            <!-- BS card 2: Start --> 
            <div class="card m-2 pt-2" style="width: 18rem;"> 
                <img src="./images/recipes/chicken_rice.webp" class="card-img-top" alt="..."> 
                <div class="card-body"> 
                    <h5 class="card-title">Chicken Rice</h5> 
                    <p class="card-text">Some quick example text to make up the bulk of the card's content.</p>  
                </div> 
                
                <div class="card-body"> 
                    <button type="button" class="btn btn-outline-success">Read more</button>
                </div> 
            </div>
            <!-- BS card: End -->
            
            <!-- BS card 3: Start --> 
            <div class="card m-2 pt-2" style="width: 18rem;"> 
                <img src="./images/recipes/hokkien_mee.webp" class="card-img-top" alt="..."> 
                <div class="card-body"> 
                    <h5 class="card-title">Hokkien Mee</h5> 
                    <p class="card-text">Some quick example text to make up the bulk of the card's content.</p>  
                </div> 
                
                <div class="card-body"> 
                    <button type="button" class="btn btn-outline-success">Read more</button>
                </div> 
            </div>
            <!-- BS card: End -->

            <!-- BS card 4: Start --> 
            <div class="card m-2 pt-2" style="width: 18rem;"> 
                <img src="./images/recipes/charkwayteow.jpg" class="card-img-top" alt="..."> 
                <div class="card-body"> 
                    <h5 class="card-title">Char Kway Teow</h5> 
                    <p class="card-text">Some quick example text to make up the bulk of the card's content.</p>  
                </div> 
                
                <div class="card-body"> 
                    <button type="button" class="btn btn-outline-success">Read more</button>
                </div> 
            </div>
            <!-- BS card: End -->

            <!-- BS card 5: Start --> 
            <div class="card m-2 pt-2" style="width: 18rem;"> 
                <img src="./images/recipes/hokkien_mee.webp" class="card-img-top" alt="..."> 
                <div class="card-body"> 
                    <h5 class="card-title">Hokkien Mee</h5> 
                    <p class="card-text">Some quick example text to make up the bulk of the card's content.</p>  
                </div> 
                
                <div class="card-body"> 
                    <button type="button" class="btn btn-outline-success">Read more</button>
                </div> 
            </div>
            <!-- BS card: End -->
            
            <!-- BS card 6: Start --> 
            <div class="card m-2 pt-2" style="width: 18rem;"> 
                <img src="./images/recipes/charkwayteow.jpg" class="card-img-top" alt="..."> 
                <div class="card-body"> 
                    <h5 class="card-title">Char Kway Teow</h5> 
                    <p class="card-text">Some quick example text to make up the bulk of the card's content.</p>  
                </div> 
                
                <div class="card-body"> 
                    <button type="button" class="btn btn-outline-success">Read more</button>
                </div> 
            </div>
            <!-- BS card: End -->
        </div>
    </div> 
</section>

</template>
<script href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootspanstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous"></script>
