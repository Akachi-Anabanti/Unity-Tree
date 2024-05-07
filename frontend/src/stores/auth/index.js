import router from "@/router";
import { API } from "@/services";
import { defineStore } from "pinia";
import { computed, ref } from "vue";

export const useAuthStore = defineStore('auth', ()=>{


    const isAuthenticated = computed(() => !!accesToken.value);
    const isSuperUser = ref(false)
    const currentUser = ref({})
    const returnUrl = ref(null)
    const accesToken = ref(null)

    const token = computed(() => accesToken.value)

    const setToken = (tk) => {
        token.value = tk
        localStorage.setItem('token', JSON.stringify(tk))
    }

    const setUser = (user) => {
        currentUser.value = user
    }

    const login = (token, user) =>{

        setToken(token)
        setUser(user)
    }

    const logout = () => {
        setToken(null)
        setUser(null)
        router.push('/account/login')
    }

    async function dispatchLogin(credentials){
        try {
            const {status, data} = await API.auth.login(credentials)
            if(status == 201){
                login(data.token, data.user)
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
        logout()
    }

    return {
        token,
        returnUrl,
        isAuthenticated,
        isSuperUser,
        currentUser,
        setToken,
        dispatchLogin,
        dispatchLogout

    }
})