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
    /* Adjust size for heart icons */
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
                            <img :src="post.imageURL" class="ui-rect ui-bg-cover">
                        </div>
                        <div class="card-footer">
                            <small class="align-middle">
                                <a href="#" class="d-inline-block text-muted like-button" @click="likePost(post)">
                                    <img v-if="post.liked" @click="unlikePost(post)" src="../assets/heartFilled.png"
                                        alt="Liked" class="heart-icon">
                                    <img v-else src="../assets/heartNoFill.png" alt="Not Liked" class="heart-icon">
                                    <strong class="like-count">{{ post.Likes }}  Likes</strong>
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
                post.Likes++;
                await axios.post('http://localhost:5000/likepost', { id: post.id, liked: true });
            } catch (error) {
                console.error('Error liking post:', error);
            }
        },
        async unlikePost(post) {
            try {
                post.liked = false;
                post.Likes--;
                await axios.post('http://localhost:5000/likepost', { id: post.id, liked: false });
            } catch (error) {
                console.error('Error unliking post:', error);
            }
        }
    },
};
</script>