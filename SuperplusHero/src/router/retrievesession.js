import axios from "axios";

export async function retrieveSession() {
    try {
        const api_url = "http://127.0.0.1:5000/retrieve_session";
        const response = await axios.get(api_url);
        if (!response.data.email) {
            throw new Error('No session found');
        }
        return response.data;
    } catch (error) {
        console.error('Error retrieving session:', error);
        throw new Error('Retrieving session failed');
    }
}