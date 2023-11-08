<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap');

* {
    font-family: "Montserrat";
}

.background {
    background-color: rgb(237, 243, 235);
}

.page-title {
    color: rgb(10, 160, 10);
    margin-left: 15px;
    margin-top: 100px;
    font-weight: bold;
}

.content {
    margin-top: 80px;
}

.card {
    width: 615px;
    height: 620px;
    max-width: 100%;
    overflow: hidden;
    margin: 10px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
}

.card-body {
    position: relative;
    /* height: 200px; */
    overflow: hidden;
}

.post-image {
    width: 100%;
    object-fit: cover;
    height: 350px;
}

.caption {
    margin-top: 10px;
}

.recipe-button {
    background-color: rgb(10, 160, 10);
    color: white;
    border-color: black;
}

.right {
    margin-left: 5px;
    float: right;
}

.heart-icon {
    height: 30px;
    width: 30px;
    margin-right: 5px;
    float: left;
}

.like-count {
    display: inline-block;
    margin-left: 5px;
    margin-top: 3px;
}

.sort {
    padding: 10px;
}

.form-floating {
    margin-bottom: 10px;
}

.custom-dropdown {
    width: 150px;
    /* transform: translateY(25%); */
    background-color: rgb(10, 160, 10);
    position: relative;
    color: white;
}

.dropdown-item:hover {
    background-color: lightgreen;
    color: black;
}
</style>

<template>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
    <section class="content">
        <div class="container posts-content">
            <h2 class="page-title">CommunityHero</h2>
            <div class="container-fluid">
                <div class="form-group">
                    <div class="row justify-content-center">
                        <div class="col-12">
                            <!-- Search Input -->
                            <div class="form-floating">
                                <input v-model="searchQuery" type="text" class="form-control" id="floatingInput"
                                    placeholder="Search for post">
                                <label for="floatingInput">Search for post</label>
                            </div>

                            <!-- Dropdown for Sorting -->
                        </div>

                        <div class="col-lg-3 align-items-center">
                            <div class="dropdown">
                                <span class="mr-auto sort">Sort by:</span>
                                <button class="btn btn-secondary dropdown-toggle custom-dropdown" type="button"
                                    data-bs-toggle="dropdown" aria-expanded="false">
                                    {{ selectedSortOption }}
                                </button>
                                <ul class="dropdown-menu">
                                    <li v-for="option in sortOptions" :key="option">
                                        <a class="dropdown-item" href="#" @click="selectSortOption(option)">{{ option }}</a>
                                    </li>
                                </ul>
                            </div>
                        </div>

                        <div class="col-lg-3 align-items-center">
                            <div class="dropdown">
                                <span class="mr-2 sort">Cuisine:</span>
                                <button class="btn btn-secondary dropdown-toggle custom-dropdown" type="button"
                                    data-bs-toggle="dropdown">
                                    {{ selectedCuisineOption || 'All' }} <!-- Set the default text to 'All' -->
                                </button>
                                <ul class="dropdown-menu">
                                    <li v-for="cuisine in cuisines" :key="cuisine">
                                        <a class="dropdown-item" href="#" @click="selectCuisineOption(cuisine)">{{ cuisine
                                        }}</a>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>

                </div>

            </div>

            <div v-if="posts.length > 0">
                <div class="row">
                    <!-- Use v-for to iterate through the posts fetched from Supabase -->
                    <div v-for="(post, index) in posts" :key="index" class="col-lg-6">
                        <div class="card">
                            <div class="card-body">
                                <div class="media mb-3">
                                    <!-- Display user image fetched from Supabase -->
                                    <!-- <img :src="post.userImage" class="d-block ui-w-40 rounded-circle" alt="User Image"> -->
                                    <div class="media-body ml-3">
                                        <!-- Display username and timestamp from Supabase -->
                                        {{ post.PostedBy }}
                                        <div class="text-muted small">Posted on {{ post.CreatedAt }}</div>
                                    </div>
                                </div>
                                <img :src="post.imageURL" class="post-image"> <!-- Need to make this responsive-->
                                <p class="caption">
                                    <!-- Display post content fetched from Supabase -->
                                    {{ post.Caption }}
                                </p>
                            </div>
                            <div class="card-footer">
                                <small class="align-middle">
                                    <a href="#" class="d-inline-block text-muted like-button">
                                        <img v-if="post.liked" @click="unlikePost(post)" src="../assets/heartFilled.png"
                                            alt="Liked" class="heart-icon" />
                                        <img v-else @click="likePost(post)" src="../assets/heartNoFill.png" alt="Not Liked"
                                            class="heart-icon" />
                                        <strong class="like-count">{{ post.Likes }} likes</strong>
                                    </a>
                                    <button @click="readRecipe(post)"
                                        class="recipe-button btn btn-sm ml-auto right">See Recipe</button>
                                </small>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div v-else-if="postsNotFound">
                <p style="margin-left:15px;">Post not found! Please check your spelling.</p>
            </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios';
import Cookies from 'js-cookie';

export default {
    data() {
        return {
            posts: [],
            sortOptions: ['Newest', 'Oldest', 'Most Liked'],
            selectedSortOption: 'Newest',
            cuisines: [],
            selectedCuisineOption: '',
            searchQuery: ''
        }
    },

    mounted() {
        this.fetchPostsFromServer();
        this.fetchCuisines();
    },

    watch: {
        searchQuery(newSearch) {
            if (newSearch === '') {
                this.fetchPostsFromServer();
            } else {
                this.searchPosts();
            }
        }
    },

    methods: {
        async fetchPostsFromServer() {
            try {
                const response = await axios.get('http://127.0.0.1:5000/communityposts');
                const sortedPosts = response.data.sort((a, b) => {
                    return new Date(b.CreatedAt) - new Date(a.CreatedAt);
                });
                this.posts = sortedPosts;
                this.filterPosts();
            } catch (error) {
                console.error('Error fetching posts:', error);
            }
        },

        filterPosts() {
            if (this.searchQuery.trim() !== '') {
                this.posts = this.posts.filter(post =>
                    post.Caption.toLowerCase().includes(this.searchQuery.trim().toLowerCase())
                );
            }
        },

        async searchPosts() {
            try {
                const response = await axios.get('http://127.0.0.1:5000/communityposts');
                let posts = response.data;
                this.posts = posts;
                this.filterPosts();

                if (this.posts.length === 0) {
                    this.postsNotFound = true;
                } else {
                    this.postsNotFound = false;
                }
            } catch (error) {
                console.error('Error searching posts:', error);
            }
        },

        selectSortOption(option) {
            this.selectedSortOption = option;
            this.sortPosts();
        },

        sortPosts() {
            if (this.selectedSortOption === 'Newest' || this.selectedSortOption === 'Oldest') {
                this.sortByCreatedAt(this.selectedSortOption);
            } else if (this.selectedSortOption === 'Most Liked'
                // || this.selectedSortOption === 'Least Liked'
            ) {
                this.sortByLikes(this.selectedSortOption);
            }
        },

        sortByCreatedAt(option) {
            if (option === 'Newest') {
                this.posts.sort((a, b) => new Date(b.CreatedAt) - new Date(a.CreatedAt));
            } else if (option === 'Oldest') {
                this.posts.sort((a, b) => new Date(a.CreatedAt) - new Date(b.CreatedAt));
            }
        },

        sortByLikes(option) {
            if (option === 'Most Liked') {
                this.posts.sort((a, b) => b.Likes - a.Likes);
            }
            // else if (option === 'Least Liked') {
            //     this.posts.sort((a, b) => a.Likes - b.Likes);
            // }
        },

        async fetchCuisines() {
            try {
                const response = await axios.get('http://127.0.0.1:5000/communityposts');
                const allCuisines = response.data.map(post => post.Cuisine);
                this.cuisines = ['All', ...new Set(allCuisines)];
            } catch (error) {
                console.error('Error fetching cuisines:', error);
            }
        },

        async filterRecipesByCuisine(cuisine) {
            try {
                const response = await axios.get('http://127.0.0.1:5000/communityposts');
                let filteredPosts = response.data;

                if (cuisine !== 'All') {
                    filteredPosts = filteredPosts.filter(post => post.Cuisine === cuisine);
                }

                this.posts = filteredPosts;
            } catch (error) {
                console.error('Error filtering recipes by cuisine:', error);
            }
        },

        selectCuisineOption(cuisine) {
            this.selectedCuisineOption = cuisine;
            this.filterRecipesByCuisine(cuisine);
        },

        async likePost(post) {
            try {
                event.preventDefault();
                post.liked = true;
                post.Likes++; // Update the local count
                const updatedLikes = post.Likes; // Store the updated count
                await this.updateLikes(post.id, updatedLikes, post);
            } catch (error) {
                console.error('Error liking post:', error);
            }
        },

        async unlikePost(post) {
            try {
                event.preventDefault();
                post.liked = false;
                post.Likes--; // Update the local count
                const updatedLikes = post.Likes; // Store the updated count
                await this.updateLikes(post.id, updatedLikes, post);
            } catch (error) {
                console.error('Error unliking post:', error);
            }
        },

        async updateLikes(postId, updatedLikes, post) {
            try {
                const response = await axios.put('http://127.0.0.1:5000/likepost', {
                    id: postId,
                    likes: updatedLikes
                });
            } catch (error) {
                console.error('Error updating likes:', error);
            }
        },

        // navigateToRecipe(post) {
        //     // Navigate to the readRecipe page with the recipeURL
        //     this.$router.push('/readRecipe/' + post.recipeURL);
        // },
        
        readRecipe(post) {
            this.recipeTitle = post.recipeTitle; 
            this.$router.push('/readRecipe/' + post.postTitle);
            Cookies.set("recipeTitle", this.recipeTitle);
        }
    },
};
</script>
