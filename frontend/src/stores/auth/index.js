import { defineStore } from "pinia";
import { ref } from "vue";

export const useAuthStore = defineStore('auth', ()=>{


    const isAuthenticated = ref(false);
    const isSuperUser = ref(false)
    const currentUser = ref({})

    const login = (user) =>{
        currentUser.value = user
        isAuthenticated.value = true
    }
    const logout = () => {
        isAuthenticated.value = false;
        currentUser.value = {}
    }

    return {
        isAuthenticated,
        isSuperUser,
        currentUser,
        login,
        logout,
    }
})