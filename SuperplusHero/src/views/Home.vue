<style>
/* #surplusCaro{
    margin-left: 50px;
    margin-right: 50px;
}

.carousel-control.left {
    margin-left: -25px;
}

.carousel-control.right {
    margin-right: -25px;
} */


.carousel-item .card {
    height: 100%;
}

/* .carousel-control-prev-icon,
.carousel-control-next-icon {
  height: 30px;
  width: 30px;
  background-size: 30px, 30px;
}
*/

button.carousel-control-prev,
button.carousel-control-next {
    width: 9%;
} 

.card button {
    border: none;
    outline: 0;
    padding: 12px;
    color: white;
    background-color: #000000;
    text-align: center;
    cursor: pointer;
    width: 100%;
    font-size: 18px;
}

.navbar-nav{
    margin-left: auto;

}

/* .nav-link{
    height: 10%;
    width: 10%
} */



</style>


<template>
    <!-- <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous"> -->
    <!-- <script type="application/javascript" src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL" crossorigin="anonymous"></script> -->

        <!-- <h2>Home Page</h2>  -->

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
                        <a class="nav-link" id="cartSize" href="#"><img src="../assets/cart.png" alt="Cart" width="50" height="50"></a>
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

        <div class="container">
            <div class="row row-cols-1 row-cols-md-3 g-4">
                <div class="col">
                    <div class="card h-100">
                    <img src="..." class="card-img-top" alt="...">
                        <div class="card-body">
                            <h5 class="card-title">Money Saved</h5>
                            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="card h-100">
                        <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                        <div class="card-body">
                            <h5 class="card-title">Viewed Recipes</h5>
                            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                        </div>
                    </div>
                </div>
                <div class="col">
                    <div class="card h-100">
                    <img src="..." class="card-img-top" alt="...">
                        <div class="card-body">
                            <h5 class="card-title">Notifications</h5>
                            <p class="card-text">This is a longer card with supporting text below as a natural lead-in to additional content.</p>
                        </div>
                    </div>
                </div>
                
            </div>
        </div>



    <!-- BS carousel: start -->
    <!-- Carousel title Produce -->
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-1"></div>
            <div class="col-md-2"><h2>Produce</h2></div>
            </div>
    </div>

        <div id="surplusCaro" class="carousel carousel-dark slide" >
                <div class="carousel-inner">
    
                    <div class="carousel-item active">
                        <div class="container-fluid">
    
                            <div class="row">
                                
                                <div class="col-md-1"></div>
                                <div class="col-md-2 mb-3">
                                        <div class="card">
                                            <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                            <h1>Lettuce</h1>
                                            <p class="price"> <s>$61.99</s><strong class="ms-2 text-danger">$50.99</strong></p>
                                            <p>Some text about the product</p>
                                            <p><button>Add to Cart</button></p>    
                                        </div>
                                </div>
                                <div class="col-md-2 mb-3">
                                        <div class="card">
                                            <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                            <h1>Lettuce</h1>
                                            <p class="price"> <s>$61.99</s><strong class="ms-2 text-danger">$50.99</strong></p>
                                            <p>Some text about the product</p>
                                            <p><button>Add to Cart</button></p>    
                                        </div>
                                </div>
                                <div class="col-md-2 mb-3">
                                        <div class="card">
                                            <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                            <h1>Lettuce</h1>
                                            <p class="price"> <s>$61.99</s><strong class="ms-2 text-danger">$50.99</strong></p>
                                            <p>Some text about the product</p>
                                            <p><button>Add to Cart</button></p>    
                                        </div>
                                </div>
                                <div class="col-md-2 mb-3">
                                        <div class="card">
                                            <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                            <h1>Lettuce</h1>
                                            <p class="price"> <s>$61.99</s><strong class="ms-2 text-danger">$50.99</strong></p>
                                            <p>Some text about the product</p>
                                            <p><button>Add to Cart</button></p>    
                                        </div>
                                </div>
                                <div class="col-md-2 mb-3">
                                        <div class="card">
                                            <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                            <h1>Lettuce</h1>
                                            <p class="price"> <s>$61.99</s><strong class="ms-2 text-danger">$50.99</strong></p>
                                            <p>Some text about the product</p>
                                            <p><button>Add to Cart</button></p>    
                                        </div>
                                </div>
                                <div class="col-md-1"></div>
                            </div>
    
                        </div>
                    </div>
                    <!-- Next carousel item -->
                    <div class="carousel-item">
                        <div class="container-fluid">
    
                            <div class="row">
                                <div class="col-md-1"></div>
                                <!-- <div class="col-md-2 mb-3">
                                        <div class="card">
                                            <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                            <h1>Lettuce</h1>
                                            <p class="price"> <s>$61.99</s><strong class="ms-2 text-danger">$50.99</strong></p>
                                            <p>Some text about the product</p>
                                            <p><button>Add to Cart</button></p>    
                                        </div>
                                </div> -->
                                <div class="card text-center col-md-2 mb-3" data-bs-toggle="modal" data-bs-target="#myModal" role="button" tabindex="0" aria-label="Open information in a popup modal">
                                    <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" class="card-img-top" alt="Card image cap">
                                        <div class="card-body">
                                            <h5 class="card-title">Card title</h5>
                                            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                                            <p><button>Add to Cart</button></p> 
                                        </div>
                                </div>

                                <div class="modal fade" id="myModal" tabindex="-1" aria-labelledby="myModalLabel" aria-hidden="true" role="dialog">
                                    <div class="modal-dialog" role="document">
                                        <div class="modal-content">
                                            <div class="modal-header">
                                                <h5 class="modal-title" id="myModalLabel">Modal title</h5>
                                                <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close">
                                                <span aria-hidden="true">&times;</span>
                                                </button>
                                            </div>
                                                <div class="modal-body">
                                                    <p>Modal body text goes here.</p>
                                                </div>
                                                <div class="modal-footer">
                                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                                </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-md-2 mb-3">
                                        <div class="card">
                                            <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                            <h1>Lettuce</h1>
                                            <p class="price"> <s>$61.99</s><strong class="ms-2 text-danger">$50.99</strong></p>
                                            <p>Some text about the product</p>
                                            <p><button>Add to Cart</button></p>    
                                        </div>
                                </div>
                                <div class="col-md-2 mb-3">
                                        <div class="card">
                                            <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                            <h1>Lettuce</h1>
                                            <p class="price"> <s>$61.99</s><strong class="ms-2 text-danger">$50.99</strong></p>
                                            <p>Some text about the product</p>
                                            <p><button>Add to Cart</button></p>    
                                        </div>
                                </div>
                                <div class="col-md-2 mb-3">
                                        <div class="card">
                                            <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                            <h1>Lettuce</h1>
                                            <p class="price"> <s>$61.99</s><strong class="ms-2 text-danger">$50.99</strong></p>
                                            <p>Some text about the product</p>
                                            <p><button>Add to Cart</button></p> 
                                        </div>
                                </div>
                                <div class="col-md-2 mb-3">
                                        <div class="card">
                                            <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                            <h1>Lettuce</h1>
                                            <p class="price"> <s>$61.99</s><strong class="ms-2 text-danger">$50.99</strong></p>
                                            <p>Some text about the product</p>
                                            <p><button>Add to Cart</button></p> 
                                        </div>
                                </div>
                                <div class="col-md-1"></div>
                            </div>
    
                        </div>
                    </div>
                </div>
                <!-- <a class="left carousel-control" href="#surplusCaro" role="button" data-slide="prev">
                    <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                    <span class="sr-only">Previous</span>
                </a>
                <a class="right carousel-control" href="#surplusCaro" role="button" data-slide="next">
                    <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                    <span class="sr-only">Next</span>
                </a> -->
    
                <button class="carousel-control-prev" type="button" data-bs-target="#surplusCaro" data-bs-slide="prev" >
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Previous</span>
                </button>
                <button class="carousel-control-next" type="button" data-bs-target="#surplusCaro" data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Next</span>
                </button>
        </div>

    <div class="container-fluid">
        <div class="row">
            <div class="col-md-1"></div>
            <div class="col-md-2"><h2>Produce</h2></div>
            </div>
    </div>



    <!-- Carousel title Recipe -->
    <div class="container-fluid">
        <div class="row">
            <div class="col-md-1"></div>
            <div class="col-md-2"><h2>Recipe</h2></div>
            </div>
    </div>


        <div id="recipeCaro" class="carousel carousel-dark slide">
            <div class="carousel-inner">
                <div class="carousel-item active">
                    <div class="container-fluid">
    
                        <div class="row">
                            
                            <div class="col-md-1"></div>
                            <!-- <div class="col-md-2 mb-3">
                                    <div class="card">
                                        <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                        <h1>Chicken Rice</h1>
                                        <p>Some text about the recipe</p>
                                        <p><button class="repBtn">Make!</button></p>    
                                    </div>
                            </div> -->
                            <div class="card text-center col-md-2 mb-3" data-bs-toggle="modal" data-bs-target="#myModal" role="button" tabindex="0" aria-label="Open information in a popup modal">
                                    <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" class="card-img-top" alt="Card image cap">
                                        <div class="card-body">
                                            <h5 class="card-title">Chicken Rice</h5>
                                            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                                            <p><button class="repBtn">Make!</button></p>   
                                        </div>
                                </div>

                                <div class="modal fade" id="myModal" tabindex="-1" aria-labelledby="myModalLabel" aria-hidden="true" role="dialog">
                                    <div class="modal-dialog" role="document">
                                        <div class="modal-content">
                                            <div class="modal-header">
                                                <h5 class="modal-title" id="myModalLabel">Modal title</h5>
                                                <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close">
                                                <span aria-hidden="true">&times;</span>
                                                </button>
                                            </div>
                                                <div class="modal-body">
                                                    <p>Modal body text goes here.</p>
                                                </div>
                                                <div class="modal-footer">
                                                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                                                </div>
                                        </div>
                                    </div>
                                </div>
                            <div class="col-md-2 mb-3">
                                    <div class="card">
                                        <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                        <h1>Chicken Rice</h1>
                                        <p>Some text about the recipe</p>
                                        <p><button class="repBtn">Make!</button></p>   
                                    </div>
                            </div>
                            <div class="col-md-2 mb-3">
                                    <div class="card">
                                        <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                        <h1>Chicken Rice</h1>
                                        <p>Some text about the recipe</p>
                                        <p><button class="repBtn">Make!</button></p>    
                                    </div>
                            </div>
                            <div class="col-md-2 mb-3">
                                    <div class="card">
                                        <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                        <h1>Chicken Rice</h1>
                                        <p>Some text about the recipe</p>
                                        <p><button class="repBtn">Make!</button></p>    
                                    </div>
                            </div>
                            <div class="col-md-2 mb-3">
                                    <div class="card">
                                        <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                        <h1>Chicken Rice</h1>
                                        <p>Some text about the recipe</p>
                                        <p><button class="repBtn">Make!</button></p>    
                                    </div>
                            </div>
                            <div class="col-md-1"></div>
                        </div>
    
                    </div>
                </div>
                <!-- Next carousel item -->
                <div class="carousel-item">
                    <div class="container-fluid">
    
                        <div class="row">
                            <div class="col-md-1"></div>
                            <div class="col-md-2 mb-3">
                                    <div class="card">
                                        <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                        <h1>Chicken Rice</h1>
                                        <p>Some text about the recipe</p>
                                        <p><button class="repBtn">Make!</button></p>    
                                    </div>
                            </div>
                            <div class="col-md-2 mb-3">
                                    <div class="card">
                                        <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                        <h1>Chicken Rice</h1>
                                        <p>Some text about the recipe</p>
                                        <p><button class="repBtn">Make!</button></p>    
                                    </div>
                            </div>
                            <div class="col-md-2 mb-3">
                                    <div class="card">
                                        <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                        <h1>Chicken Rice</h1>
                                        <p>Some text about the recipe</p>
                                        <p><button class="repBtn">Make!</button></p>    
                                    </div>
                            </div>
                            <div class="col-md-2 mb-3">
                                    <div class="card">
                                        <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                        <h1>Chicken Rice</h1>
                                        <p>Some text about the recipe</p>
                                        <p><button class="repBtn">Make!</button></p> 
                                    </div>
                            </div>
                            <div class="col-md-2 mb-3">
                                    <div class="card">
                                        <img src="https://blog.udemy.com/wp-content/uploads/2014/05/bigstock-test-icon-63758263.jpg" alt="Recipe" style="width:100%">
                                        <h1>Chicken Rice</h1>
                                        <p>Some text about the recipe</p>
                                        <p><button class="repBtn">Make!</button></p> 
                                    </div>
                            </div>
                            <div class="col-md-1"></div>
                        </div>
    
                    </div>
                </div>
            </div>
            <!-- <a class="left carousel-control" href="#surplusCaro" role="button" data-slide="prev">
                <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                <span class="sr-only">Previous</span>
            </a>
            <a class="right carousel-control" href="#surplusCaro" role="button" data-slide="next">
                <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                <span class="sr-only">Next</span>
            </a> -->
    
            <button class="carousel-control-prev" type="button" data-bs-target="#recipeCaro" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#recipeCaro" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
            </button>

        </div>
    <!-- BS carousel: end -->
    


    <div class="card text-center" data-bs-toggle="modal" data-bs-target="#myModal" role="button" tabindex="0" aria-label="Open information in a popup modal">
        <img src="your_image.jpg" class="card-img-top" alt="Card image cap">
            <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
            </div>
    </div>

    <div class="modal fade" id="myModal" tabindex="-1" aria-labelledby="myModalLabel" aria-hidden="true" role="dialog">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="myModalLabel">Modal title</h5>
                <button type="button" class="close" data-bs-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
                </button>
            </div>
                <div class="modal-body">
                    <p>Modal body text goes here.</p>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>
</template>

