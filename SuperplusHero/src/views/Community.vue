<style scoped>
.content {
    margin-top: 100px;
}

img {
    height: 600px;
    width: 600px;
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
</style>

<template>
    <section class="content">
        <div class="container posts-content">
            <div class="row">
                <!-- Use v-for to iterate through the posts fetched from Supabase -->
                <div v-for="(post, index) in posts" :key="index" class="col-lg-6">
                    <div class="card mb-4">
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
                            <img :src="post.imageURL" class="ui-rect ui-bg-cover"> <!-- Need to make this responsive-->
                        </div>
                        <div class="card-footer">
                            <small class="align-middle">
                                <a href="#" class="d-inline-block text-muted like-button">
                                    <img v-if="post.liked" @click="unlikePost(post)" src="../assets/heartFilled.png"
                                        alt="Liked" class="heart-icon" />
                                    <img v-else @click="likePost(post)" src="../assets/heartNoFill.png" alt="Not Liked"
                                        class="heart-icon" />
                                    <strong class="like-count">{{ post.Likes }} Likes</strong>
                                </a>
                            </small>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            posts: []
        };
    },
    mounted() {
        this.fetchPostsFromServer();
    },
    methods: {
        async fetchPostsFromServer() {
            try {
                const response = await axios.get('http://localhost:5000/communityposts');
                this.posts = response.data;
            } catch (error) {
                console.error('Error fetching posts:', error);
            }
        },
        async likePost(post) {
            try {
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

                // if (response.data) {
                //     // Update the post with the updated data from the server
                //     const updatedPost = response.data;
                //     const index = this.posts.findIndex(p => p.id === updatedPost.id);
                //     if (index !== -1) {
                //         this.posts[index] = updatedPost;
                //     }
                // }
            } catch (error) {
                console.error('Error updating likes:', error);
                // // Revert local changes on failure, if necessary
                // if (post) {
                //     post.Likes = updatedLikes;
                //     post.liked = !post.liked;
                // }
            }
        }
    },
};
</script>