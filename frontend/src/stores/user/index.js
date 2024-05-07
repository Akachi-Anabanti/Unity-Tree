import { API } from "@/services";
import { defineStore } from "pinia";


export const useUserStore = defineStore('userStore', () =>{



    // // function to remove user from state
    // const deleteUser = (id) => {

    // }

    // // updates the user value in state
    // const updateUser = (id, data) => {

    // }

    // creates the user and updates the users list
    async function dispatchCreateUser (input){
        try {

            const {status} = await API.users.createUser(input);
            if(status == 200){
                // addNewUser(data)
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
            status: 400
        }
    }

    // deletes a user from the db and updates the state
    async function dispatchDeleteUser(id){
        try {

            const {status} = await API.users.deleteUser(id);
            if(status == 200){
                // removeUser(id)
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
        dispatchCreateUser,
        dispatchDeleteUser,
        dispatchUpdateUser
    }
});
