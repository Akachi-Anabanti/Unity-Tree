import axios from "axios";
import { useAuthStore } from "@/stores/auth";

const instance = axios.create({
    baseURL: import.meta.env.VITE_API_ENDPOINT,
});

instance.interceptors.request.use(async(config) => {

    if(config.url !== '/register' && config.url !== '/login'){
        const authStore = useAuthStore();
        // if the route is not register and login
        if (authStore.token){
            // if token is set then
            // add it to headers
            config.headers.Authorization = `Bearer ${authStore.token}`;

        }else {
            // if token is null try refreshing it
            const response = await instance.post('/refresh');
            authStore.setToken(response.data.access_token)
            config.headers.Authorization = `Bearer ${authStore.token}`;
        }
    }
})
export default instance