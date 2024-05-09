import axios from "axios";
import getCookie from "@/_helpers/getCookie";

const instance = axios.create({
    baseURL: import.meta.env.VITE_API_ENDPOINT,
});

instance.interceptors.request.use(async(config) => {

    if(config.url !== '/register' && config.url !== '/login'){
        config.headers["X-CSRF-TOKEN"]=getCookie('csrf_access_token')
    }
    return config
})
export default instance