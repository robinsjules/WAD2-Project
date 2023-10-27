// testing to see if supabase data can be retrieved
// file not in used pls ignore
import axios from "axios";
export async function fetchUsers() {
    const api_url = "http://localhost:5000/users";
    try {
        const response = await axios.get(api_url);
        const usersData = response.data;
        return usersData;
    } catch (error) {
        console.log(error);
        return [];
    }
}