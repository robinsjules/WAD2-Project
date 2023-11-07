<style scoped>
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

.dropdown {
    position: relative;
    display: inline-block;
}

.dropdown-toggle {
    background-color: #f8f9fa;
    border: 1px solid #ced4da;
    padding: 8px 12px;
    cursor: pointer;
}

.dropdown-menu {
    display: none;
    position: absolute;
    background-color: #fff;
    min-width: 160px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
    z-index: 1;
}

.dropdown-menu a {
    display: block;
    padding: 8px 12px;
    text-decoration: none;
    color: #333;
}

.dropdown-menu a:hover {
    background-color: #f5f5f5;
}

.dropdown-menu a:focus {
    outline: none;
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
                            <input v-model="searchQuery" type="text" class="form-control" placeholder="Search for post">
                            <!--Edit to be responsive-->
                        </div>
                    </div>
                </div>
            </div>

            <div class="form-group m-3">
                <label for="sortOptions">Sort by: &nbsp;</label>
                <select id="sortOptions" v-model="selectedSortOption" @change="sortPosts">
                    <option v-for="option in sortOptions" :key="option">{{ option }}</option>
                </select>
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
                                <p>
                                    <!-- Display post content fetched from Supabase -->
                                    {{ post.Caption }}
                                </p>
                                <img :src="post.imageURL" class="post-image"> <!-- Need to make this responsive-->
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
import dropdown from 'vue-dropdowns';

export default {
    data() {
        return {
            posts: [],
            sortOptions: ['Newest', 'Oldest', 'Most Liked'],
            selectedSortOption: 'Newest',
            searchQuery: '',
            isDropdownOpen: false
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

    components: {
        'dropdown': dropdown,
    },

    methods: {
        async fetchPostsFromServer() {
            try {
                const response = await axios.get('http://localhost:5000/communityposts');
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
                const response = await axios.get('http://localhost:5000/communityposts');
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

        toggleDropdown() {
            this.isDropdownOpen = !this.isDropdownOpen;
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
                const response = await axios.put('http://localhost:5000/likepost', {
                    id: postId,
                    likes: updatedLikes
                });
            } catch (error) {
                console.error('Error updating likes:', error);
            }
        }
    },
};
</script>
