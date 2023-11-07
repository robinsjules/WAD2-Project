import axios from "axios";

export async function signIn(email, password) {
    const basicAuth = 'Basic ' + btoa(email + ':' + password);

    const api_url = 'http://127.0.0.1:5000/auth_sign_in';
    try {
        const response = await axios.post(api_url, null, {
            headers: { 'Authorization': basicAuth }
        });
        return response;
    } catch (error) {
        console.error('Error on Authentication', error);
        throw new Error('Authentication failed');
    }
}
