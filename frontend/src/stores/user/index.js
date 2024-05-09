import { API } from "@/services";
import { defineStore } from "pinia";
import { useAuthStore } from "../auth";


export const useUserStore = defineStore('userStore', () =>{

    const authStore = useAuthStore()


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

    return {
        dispatchGetUser,
        dispatchDeleteUser,
        dispatchUpdateUser
    }
});
