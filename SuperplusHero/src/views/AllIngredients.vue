<style>
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
            <h1>
                <span class="text-primary" style="font-weight: bold;" >All Ingridients</span>
            </h1>

            <div class="form-group">
                
                <div class="form-group">
                    <div class="row justify-content-center mt-5">
                    <div class="col-md">
                    <div class="input-group">
                        <input type="text" class="form-control" placeholder="Search Recipe..">
                    
                        <div class="input-group-append">
                            <button class="btn btn-primary" type="button">Search</button>
                        </div>
                    </div>
                    </div>
                    </div>
                </div>
                        <!-- Filter Button Start --> 
                        <div class="col-4 btn-group mt-2"> 
                            <select class="form-select" aria-label="Default select example"> 
                            <option selected value="all">Filter by Ingridients</option>
                            <option value="mns" name="mns">Meat & Seafood</option>
                            <option value="fnv" name="fnv">Fruits & Vegetables</option> 
                            <option value="rnc" name="rnc">Rice,Noodle & Cooking Ingridients</option> 
                            <option value="dce" name="dce">Dairy, Chilled & Eggs</option>
                        </select>
                        <!-- Filter Button End  -->
                        
                        
                        
                    
                    
                    <!-- <input type="button" class="col-2 input-group-btn"> -->
                        
                    
                
                </div>
                
                
        </div>
        </div>
    </form>


    
<section>
    <div class="container-fluid">
        <div class="row justify-content-center">
            <!-- BS card 1: Start --> 
            
            <div class="card m-2 pt-2" style="width: 18rem;"> 
                <img src="./images/ingridients/Broccoli.png" class="card-img-top" alt="..."> 
                <div class="card-body"> 
                    <h5 class="card-title">Broccoli (250g)</h5>
                    <p class="card-text">
                        <span style="font-weight: bold; font-size: 20px;">$3.05</span>&nbsp;
                        <span style="text-decoration: line-through;">$4.20</span>
                    </p>
                    <p class="card-text">Some quick example text to make up the bulk of the card's content.</p>  
                </div> 
                
                <div class="card-body"> 
                    <button type="button" class="btn btn-primary">Add To Cart</button>
                </div> 
            </div>
            <!-- BS card: End --> 

            <!-- BS card 2: Start --> 
            <div class="card m-2 pt-2" style="width: 18rem;"> 
                <img src="./images/ingridients/Cabbage.png" class="card-img-top" alt="..."> 
                <div class="card-body"> 
                    <h5 class="card-title">Cabbage</h5>
                    <p class="card-text">
                        <span style="font-weight: bold; font-size: 20px;">$3.05</span>&nbsp;
                        <span style="text-decoration: line-through;">$4.20</span>
                    </p>
                    <p class="card-text">Some quick example text to make up the bulk of the card's content.</p>  
                </div> 
                
                <div class="card-body"> 
                    <button type="button" class="btn btn-primary">Add To Cart</button>
                </div> 
            </div>
            <!-- BS card: End -->
            
            <!-- BS card 3: Start --> 
            <div class="card m-2 pt-2" style="width: 18rem;"> 
                <img src="./images/ingridients/Pork Belly.png" class="card-img-top" alt="..."> 
                <div class="card-body"> 
                    <h5 class="card-title">Pork Belly</h5>
                    <p class="card-text">
                        <span style="font-weight: bold; font-size: 20px;">$3.05</span>&nbsp;
                        <span style="text-decoration: line-through;">$4.20</span>
                    </p>
                    <p class="card-text">Some quick example text to make up the bulk of the card's content.</p>  
                </div> 
                
                <div class="card-body"> 
                    <button type="button" class="btn btn-primary">Add To Cart</button>
                </div> 
            </div>
            <!-- BS card: End -->

            <!-- BS card 4: Start --> 
            <div class="card m-2 pt-2" style="width: 18rem;"> 
                <img src="./images/ingridients/Salmon.png" class="card-img-top" alt="..."> 
                <div class="card-body"> 
                    <h5 class="card-title">Salmon</h5>
                    <p class="card-text">
                        <span style="font-weight: bold; font-size: 20px;">$3.05</span>&nbsp;
                        <span style="text-decoration: line-through;">$4.20</span>
                    </p>
                    <p class="card-text">Some quick example text to make up the bulk of the card's content.</p>  
                </div> 
                
                <div class="card-body"> 
                    <button type="button" class="btn btn-primary">Add To Cart</button>
                </div> 
            </div>
            <!-- BS card: End -->

            <!-- BS card 5: Start --> 
            <div class="card m-2 pt-2" style="width: 18rem;"> 
                <img src="./images/ingridients/Broccoli.png" class="card-img-top" alt="..."> 
                <div class="card-body"> 
                    <h5 class="card-title">Broccoli</h5>
                    <p class="card-text">
                        <span style="font-weight: bold; font-size: 20px;">$3.05</span>&nbsp;
                        <span style="text-decoration: line-through;">$4.20</span>
                    </p>
                    <p class="card-text">Some quick example text to make up the bulk of the card's content.</p>  
                </div> 
                
                <div class="card-body"> 
                    <button type="button" class="btn btn-primary">Add To Cart</button>
                </div> 
            </div>
            <!-- BS card: End -->
            
            <!-- BS card 6: Start --> 
            <div class="card m-2 pt-2" style="width: 18rem;"> 
                <img src="./images/ingridients/Pork Belly.png" class="card-img-top" alt="..."> 
                <div class="card-body"> 
                    <h5 class="card-title">Pork Belly</h5>
                    <p class="card-text">
                        <span style="font-weight: bold; font-size: 20px;">$3.05</span>&nbsp;
                        <span style="text-decoration: line-through;">$4.20</span>
                    </p>
                    <p class="card-text">Some quick example text to make up the bulk of the card's content.</p>  
                </div> 
                
                <div class="card-body"> 
                    <button type="button" class="btn btn-primary">Add To Cart</button>
                </div> 
            </div>
            <!-- BS card: End -->
        </div>
    </div> 
</section>

</template>
<script href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootspanstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous"></script>
