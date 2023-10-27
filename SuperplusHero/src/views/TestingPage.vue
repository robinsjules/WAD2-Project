<template>
    <div>
        <h2>Users:</h2>
        <p>{{ users }}</p>
    </div>
</template>
<script>
// testing to see if user data can be retrieved
// import { fetchUsers } from '@/services/getUsers';
// file not in used pls ignore
import axios from 'axios';
import { watchEffect } from 'vue';

export default {
    setup() {
        const users = ref(null);

        watchEffect(() => {
            axios
                .get('http://127.0.0.1:5000/users')
                .then((response) => (users.value = response.data))
                .catch((error) => {
                    console.log('Error fetching users', error);
                });
        });

        return {
            users,
        };
    },
};
