import { API } from "@/services";
import { defineStore } from "pinia";
import { useAuthStore } from "../auth";
import { computed, reactive} from "vue";


export const useUserStore = defineStore('userStore', () =>{

    const authStore = useAuthStore()
    let familiesCreated = reactive([])

    const numberOfFamiliesCreated = computed (() => familiesCreated.length)
    const isNumberNotZero = computed (() => numberOfFamiliesCreated.value > 0) 

    const getFamily = ()=>{
        return familiesCreated
    }

    async function dispatchGetUser(){
        try {

            const {status, data} = await API.users.getUser();
            if(status == 200){
                return {
                    success: true,
                    content: data
                }
            }
            
        } catch (error) {

            return {
                success: false,
                status: error.response?.status,
                content: null
            }
            
        }

        return {
            success:false,
            content:null,
            status:400
        }
    }

    // deletes a user from the db and updates the state
    async function dispatchDeleteUser(id){
        try {

            const {status} = await API.users.deleteUser(id);
            if(status == 200){
                authStore.dispatchLogout()
                return {
                    success: true,
                    content: null
                }
            }
            
        } catch (error) {

            return {
                success: false,
                status: error.response?.status,
                content: null
            }
            
        }

        return {
            success:false,
            content:null,
            status:400
        }
    }

    // updates the user in the database
    async function dispatchUpdateUser(id, input){
        try {

            const {status} = await API.users.updateUser(id, input);
            if(status == 200){
                // updateUser(id, data);
                return {
                    success: true,
                    content: null
                }
            }
            
        } catch (error) {

            return {
                success: false,
                status: error.response?.status,
                content: null
            }
            
        }

        return {
            success:false,
            content:null,
            status:400
        }
    }

    async function dispatchGetFamiliesCreated(){
        try {
            const {status, data} = await API.users.getFamiliesCreated()
            if (status === 200) {
                familiesCreated = data
                return {
                    success:true,
                    content:null
                }
            }
        } catch (error) {
            return {
                success: false,
                content:null,
                status: error.response?.status
            }

        }

    }

    return {
        isNumberNotZero,
        numberOfFamiliesCreated,
        getFamily,
        dispatchGetUser,
        dispatchDeleteUser,
        dispatchUpdateUser,
        dispatchGetFamiliesCreated
    }
});
