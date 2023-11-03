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
                                <!--<img :src="post.userImage" class="d-block ui-w-40 rounded-circle" alt="User Image">-->
                                <div class="media-body ml-3">
                                    <!-- Display username and timestamp from Supabase -->
                                    {{ post.User }}
                                    <div class="text-muted small">{{ post.CreatedAt }}</div>
                                </div>
                            </div>

                            <p>
                                <!-- Display post content fetched from Supabase -->
                                {{ post.Caption }}
                            </p>
                            <img :src="post.imageURL" class="ui-rect ui-bg-cover">
                        </div>
                        <div class="card-footer">
                            <a href="#" class="d-inline-block text-muted like-button" @click="likePost(post.id)">
                                <!-- Show like count from Supabase -->
                                <small class="align-middle">
                                    <strong class="like-count">{{ post.Likes }}</strong> Likes
                                </small>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
import { ref, onMounted } from 'vue'; // Import the necessary Vue functionalities

export default {
    setup() {
        // Define variables using the Composition API
        const posts = ref([]); // Store posts fetched from Supabase

        // Fetch posts from Supabase on component mount
        onMounted(async () => {
            // Fetch posts from Supabase and set them in the 'posts' variable
            posts.value = await fetchPostsFromSupabase();
        });

        // Function to fetch posts from Supabase
        const fetchPostsFromSupabase = async () => {
            // Code to fetch posts from Supabase goes here
            // Use Supabase queries to get data from your database
            const { data, error } = await supabase.from('Posts').select('*');
            // Return the fetched data (posts)
            return data;
        };

        // Function to like a post
        const likePost = async (postId) => {
            // Implement the logic to like a post using Supabase
            // Example: Update the like count in the database and update the 'likes' field for the post
            await supabase.from('posts').update({ likes: post.likes + 1 }).eq('id', postId);
            // After liking, refresh the posts or update the specific post's like count in 'posts'
            posts.value = await fetchPostsFromSupabase();
        };

        return {
            posts,
            likePost
        };
    }
}
</script>