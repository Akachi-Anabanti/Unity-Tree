import { API } from "@/services";
import { defineStore } from "pinia";
import { computed, reactive, ref} from 'vue'


export const useFamilyStore =  defineStore('family',() =>{

    const familyData = reactive({
        father:{},
        mother:{},
        children:[]
    });

    const hasFamily = ref(true)

    // Static data
    familyData.value = {
        "father": {
        "name": "C-3PO",
        "dateOfBirth": new Date(1877, 2, 14).toDateString(),
        "img": "https://randomuser.me/api/portraits/men/1.jpg",
        "role":"parent"
        },
        "mother": {
        "name": "Luke Skywalker",
        "dateOfBirth": new Date(1887, 1, 29).toDateString(),
        "img": "https://randomuser.me/api/portraits/women/5.jpg",
        "role": "parent"
        },
        "children": [
        {
            "name": "Obi-Wan Kenobi",
            "dateOfBirth": new Date(1987, 1, 29).toDateString(),
            "img": "https://randomuser.me/api/portraits/men/2.jpg",
            "role": "child"
        },
        {
            "name": "Jabba Desilijic Tiure",
            "dateOfBirth": new Date(1787, 1, 29).toDateString(),
            "img": "https://randomuser.me/api/portraits/women/4.jpg",
            "role": "child"
        },
        {
            "name": "Yoda",
            "dateOfBirth": new Date(1987, 1, 29).toDateString(),
            "img": "https://randomuser.me/api/portraits/men/5.jpg",
            "role": "child"
        },
        {
            "name": "Darth Vader",
            "dateOfBirth": new Date(1897, 1, 29).toDateString(),
            "img": "https://randomuser.me/api/portraits/men/6.jpg",
            "role": "child"
        },
        {
            "name": "Obi-Wan Kenobi",
            "dateOfBirth": new Date(1887, 1, 29).toDateString(),
            "img": "https://randomuser.me/api/portraits/men/2.jpg",
            "role": "child"
        },
        ]
    };

    const numberOfChildren = computed(() => {return familyData.children.length})

    /**
     * @description creates the inital family data
     * @param {*} data 
     */
    const initFamily = (data) => {
        familyData.value = data
    }


    /**
     * @description resets the store familyData to 
     * empty object
     */
    const deleteFamily = () => {
        familyData.value = {}
    }

    const deleteChild = (child) => {
        const index = familyData.value.children.findIndex((cd) => cd === child)
        if (index !== -1) {
          familyData.value.children.splice(index, 1)
        }
    }

    const deleteParent = (parent) => {
        delete familyData.value[parent.role];
    }

    //--------DISPATCHERS-----------//


    /**
     * @description actor that gets the family based on the memberId
     * @param {*} memberId 
     * @returns 
     */
    async function dispatchGetFamily(memberId){
        try {
            const {status, data} = await API.family.getFamily(memberId)

            if(status === 200){
                // create family data
                initFamily(data)

                hasFamily.value = true

                return {
                    success: true,
                    content: null,
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
            success: false,
            content:null,
            status: 401
        }
    }


    async function dispatchDeleteChild(child){
        try {
            const {status} = await API.users.deleteUser(child.id)
            if (status === 200){
                deleteChild(child)
                return {
                    success: true,
                    content:null
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
            status: 401
        }
    }

    async function dispatchDeleteParent(parent){
        try {
                const {status} = await API.users.deleteUser(parent.id)
                if (status === 200){
                    deleteParent(parent)
        
                    return {
                        success:true,
                        content:null,
                    }
                }
        } catch (error) {
            return {
                success:false,
                content:null,
                status: error.response?.status
            }
        }

        return {
            success:false,
            content:null,
            status:401
        }

    }

    return {
        initFamily,
        deleteFamily,
        dispatchGetFamily,
        dispatchDeleteChild,
        dispatchDeleteParent,
        numberOfChildren,
        familyData,
        hasFamily
    }

})
