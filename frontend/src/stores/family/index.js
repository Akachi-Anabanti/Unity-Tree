import { API } from "@/services";
import { defineStore } from "pinia";
import { reactive} from 'vue'


export const useFamilyStore =  defineStore('family',() =>{

    const familyData = reactive({});

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

    return {
        initFamily,
        deleteFamily,
        dispatchGetFamily
    }

})
