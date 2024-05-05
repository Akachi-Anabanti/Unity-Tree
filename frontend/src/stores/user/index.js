import { API } from "@/services";
import { defineStore } from "pinia";

import { reactive, ref } from "vue";


export const useUserStore = defineStore('userStore', () =>{

    const users = reactive([]);
    const nextButton = ref(false)
    const prevButton = ref(false)
    const currentPage = ref(0)

    // function to inital users state
    const initUsers = (data) => {
        users.value = data
    }
    // function to remove user from state
    const removeUser = (id) => {
        const idx = users.value.findIndex((u) => u.id === id)
        if (idx === -1) return;

        users.value.splice(idx, 1);
    }

    //function to add user to state
    const addNewUser = (user) => {
        users.value.push(user);
    }

    // updates the user value in state
    const updateUser = (id, data) => {
        const idx = users.value.findIndex((u) => u.id === id)
        if (idx === -1) return;
        users.value[idx] = data
    }

    // makes the API call and updates the users value
    async function dispatchGetUsers (params){
        try {

            const {status, data} = await API.users.getUsers(params);
            if(status == 200){
                initUsers(data.data)

                // check for page values
                const {page, total_pages} = data
                // sets the ref value of current page
                currentPage.value = page
                if (page === 1 && total_pages === 1){
                    nextButton.value = false;
                    prevButton.value = false;
                } else if (page === 1 && page < total_pages){
                    prevButton.value = false;
                    nextButton.value = true;
                } else if (page === total_pages){
                    nextButton.value = false;
                    prevButton.value = true;
                } else {
                    nextButton.value = true;
                    prevButton.value = true;
                }

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
    }

    // creates the user and updates the users list
    async function dispatchCreateUser (input){
        try {

            const {status, data} = await API.users.createUser(input);
            if(status == 200){
                addNewUser(data.data)
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
                removeUser(id)
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

            const {status, data} = await API.users.updateUser(id, input);
            if(status == 200){
                updateUser(id, data.data);
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
        users,
        currentPage,
        prevButton,
        nextButton,
        initUsers,
        removeUser,
        addNewUser,
        dispatchGetUsers,
        dispatchCreateUser,
        dispatchDeleteUser,
        dispatchUpdateUser
    }
});

// dispatchers are responsible for mutating state values
// These dispatchers are state `actions`