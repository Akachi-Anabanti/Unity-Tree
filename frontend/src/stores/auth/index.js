import router from "@/router";
import { API } from "@/services";
import { defineStore } from "pinia";
import { computed, ref } from "vue";
import { useUserStore } from "../user";

export const useAuthStore = defineStore('auth', ()=>{

    const userStore = useUserStore()

    const loggedIn = ref(false)

    const isAuthenticated = computed(() => loggedIn.value);
    const isSuperUser = ref(false)
    const currentUser = ref(null)
    const returnUrl = ref(null)

    const setUser = (user) => {
        currentUser.value = user
    }

    const login = (user) =>{

        setUser(user)
        loggedIn.value = true
    }

    const logout = () => {
        loggedIn.value = false
        setUser(null)
        router.push('/account/login')
    }

    async function dispatchLogin(credentials){
        try {
            const {status} = await API.auth.login(credentials)
            if(status == 201){
                // If login is successful then
                // get the user data
                // finally set the user data
                const {content} = await userStore.dispatchGetUser()
                login(content)
                {
                    router.push(returnUrl.value || '/');
                }
            }
        } catch (error) {
            return {
                success:false,
                content:null,
                status:error.response?.status
            }
            
        }
        return {
            success:false,
            content:null,
            status:401
        }
    }

    async function dispatchLogout(){

        try {
            const {message} = await API.auth.logout()
            logout()
            return {
                success:true,
                content: message
                
            }
        } catch (error) {
            return {
                success: false,
                content:null,
                status: error.response?.status
            }
        }
    }


    async function dispatchRegister(info){
        try {
            const {status} = await API.auth.register(info)
            if(status == 201){
                const credentials = {
                    password: info.password,
                    email: info.email
                }
                // if registration is successful automatically login
                //  user and update
                dispatchLogin(credentials)
            }
        } catch (error) {
            return {
                success:false,
                content:null,
                status:error.response?.status
            }
            
        }
        return {
            success:false,
            content:null,
            status:401
        }

    }
    return {
        returnUrl,
        isAuthenticated,
        isSuperUser,
        currentUser,
        dispatchLogin,
        dispatchLogout,
        dispatchRegister

    }
})