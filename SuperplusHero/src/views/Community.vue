<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap');

*{
    font-family: "Montserrat";
}
.content {
    margin-top: 100px;
}
.card {
    width: 615px;
    height: 600px;
    max-width: 100%;
    overflow: hidden;
    margin: 10px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
}

.card-body {
    position: relative;
    height: 200px;
    overflow: hidden;
}

.post-image {
    width: 100%;
    object-fit: cover;
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

button {
    float: right;
    background-color: rgb(10, 160, 10);
    color: white;
    /* border-color: black; */
}

.dropdown-item:hover {
    background-color: lightgreen;
    color: black;
}
</style>

<template>
    <section class="content">
        <div class="container posts-content">
            <!-- Search Bar -->
            <div class="container-fluid">
                <div class="form-group">
                    <div class="row justify-content-center">
                        <div class="input-group">
                            <!-- Search Input -->
                            <div class="form-floating mb-3 search-input">
                                <input v-model="searchQuery" type="text" class="form-control" id="floatingInput"
                                    placeholder="Search for post">
                                <label for="floatingInput">Search for post</label>
                            </div>

                            <!-- Dropdown for Sorting -->
                        </div>
                        <div class="dropdown-center">
                                <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown"
                                    aria-expanded="false">
                                    {{ selectedSortOption }}
                                </button>
                                <ul class="dropdown-menu">
                                    <li v-for="option in sortOptions" :key="option">
                                        <a class="dropdown-item" href="#" @click="selectSortOption(option)">{{ option }}</a>
                                    </li>
                                </ul>
                            </div>
                    </div>
                </div>
            </div>

            <div class="form-group m-3">
                <label for="sortOptions">Sort by: ▼&nbsp;</label>
                <select id="sortOptions" v-model="selectedSortOption" @change="sortPosts" class="custom-dropdown">
                    <option v-for="option in sortOptions" :key="option">{{ option }}</option>
                </select>
            </div> -->

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
                                <p>
                                    <!-- Display post content fetched from Supabase -->
                                    {{ post.Caption }}
                                </p>
                                <img :src="post.imageURL" class="post-image"> <!-- Need to make this responsive-->
                            </div>
                            <div class="card-footer">
                                <small class="align-middle d-flex">
                                    <a href="#" class="d-inline-block text-muted like-button">
                                        <img v-if="post.liked" @click="unlikePost(post)" src="../assets/heartFilled.png"
                                            alt="Liked" class="heart-icon" />
                                        <img v-else @click="likePost(post)" src="../assets/heartNoFill.png" alt="Not Liked"
                                            class="heart-icon" />
                                        <strong class="like-count">{{ post.Likes }} likes</strong>
                                    </a>
                                    &nbsp;
                                    <button @click="navigateToRecipe(post)" class="btn btn-success btn-sm ml-auto">See Recipe</button>
                                    <button @click="navigateToRecipe(post)" class="btn btn-primary btn-sm ml-auto right">See
                                        Recipe</button>
                                </small>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div v-else-if="postsNotFound">
                <p>Post not found! Please check your spelling.</p> <!-- Edit to have space above -->
            </div>

        </div>
    </section>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            posts: [],
            sortOptions: ['Newest', 'Oldest', 'Most Liked'],
            selectedSortOption: 'Newest',
            searchQuery: ''
        };
    },

    mounted() {
        this.fetchPostsFromServer();
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

        sortPosts() {
            if (this.selectedSortOption === 'Newest' || this.selectedSortOption === 'Oldest') {
                this.sortByCreatedAt(this.selectedSortOption);
            } else if (this.selectedSortOption === 'Most Liked'
            // || this.selectedSortOption === 'Least Liked'
            ){
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

        navigateToRecipe(post) {
            // Navigate to the readRecipe page with the recipeURL
            this.$router.push('/readRecipe/' + post.recipeURL);
        }
    },
};
</script>
