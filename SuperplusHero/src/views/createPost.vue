<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap');

* {
    font-family: "Montserrat";
}

.page-title {
    color: rgb(10, 160, 10);
    margin-top: 100px;
    font-weight: bold;
}

.content {
    margin-top: 80px;
    margin-left: 15px;
}

.post-button {
    background-color: rgb(10, 160, 10);
    color: white;
    border-color: black;
}

.post-button:hover{
    background-color: rgb(10, 160, 10);
    color: white;
    border-color: black;

}

</style>

<template>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
    <section class="content">
        <div class="container posts-content">
            <h2 class="page-title">CommunityShare</h2>
            <div class="card">
                <div class="card-body">
                    <form>
                        <div class="form-group">
                            <input type="email" class="form-control" id="exampleFormControlInput1"
                                placeholder="Caption your creation!">
                        </div>
                        <button type="submit" class="post-button btn btn-sm">Post!</button>
                    </form>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
</script>