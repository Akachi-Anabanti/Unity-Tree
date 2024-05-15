import { API } from "@/services";
import { defineStore } from "pinia";
import { computed, ref} from 'vue'


export const useFamilyStore =  defineStore('family',() =>{

    let familyMembers = ref({father:null,mother:null, children:[]})
    const memberInfo = ref({})
    const familyData = ref({})
    const isFamilyEmpty = ref(true)
    const hasFamily = ref(false)

    const numberOfChildren = computed(() => familyMembers.value && familyMembers.value.children ? familyMembers.value.children.length : 0)
    const getFamilyName = computed(() => familyData.value.name)
    const getFamilyId = computed(() => familyData.value.id)
    const getCreatorId = computed(() => familyData.value.creator_id)


    // resets the store to empty state
    function $reset(){
        familyMembers.value = {}
        memberInfo.value = {}
        familyData.value = {}
        hasFamily.value = false
        isFamilyEmpty.value = true
    }



       // checks if the  family created is empty
       function isEmpty(obj) {
        for(let key in obj) {
            if(typeof obj[key] === 'object' && obj[key] !== null) {
                if(!isEmpty(obj[key])) {
                    return false;
                }
            } else if(Array.isArray(obj[key]) && obj[key].length > 0) {
                return false;
            } else if(obj[key] !== null && obj[key] !== undefined && obj[key] !== '') {
                return false;
            }
        }
        return true;
    }

    const getChildIdx = (person) => {
        return familyMembers.value.children.findIndex((cd) => cd.id === person.id)
    }

    /**
     * @description creates the inital familyMmebers data
     * @param {*} data 
     */
    const initFamily = (data) => {
        familyData.value = data
    }

    /**
 * @description creates the inital familyMmebers data
 * @param {*} data 
 */
    const initFamilyMembers = (data) => {
        familyMembers.value = data
    }

    //  creates a new family
    const createFamily = (data) => {
        familyData.value = data
    }
    
    //  updates the family information
    const updateFamily = (data) => {
        familyData.value = data
    }

    // deletes the family details

    const deleteFamily = () => {
        familyData.value = {}
    }

    // set the member information
    const initMemberInfo = (person) => {
        memberInfo.value = person
    }

    const createFamilyMember = (person) => {
        if (person.role === 'child'){
            familyMembers.value.children.push(person)
        } else {
            familyMembers.value[person.role] = person
        }

        // updates the isFamilyEmpty to false
        // as a new member has been created
        isFamilyEmpty.value = false

    }
    const updateFamilyMember = (person) => {
        if (person.role === "child"){
            const idx = getChildIdx(person)
            familyMembers.value.children[idx] = person
        } else {
            familyMembers[person.role] = person;
        }
    }
    const deleteFamilyMember = (person) => {
        if (person.role === 'child'){
          
            const index = familyMembers.value.children.findIndex((cd) => cd.id === person.member_id)
            if (index !== -1) {
              familyMembers.value.children.splice(index, 1)
            }
        } else
        {
            delete familyMembers.value[person.role];
        }

        // reset the value to empty if the 
        // familymembers are all deleted
        if (isEmpty(familyMembers.value)){
            isFamilyEmpty.value = true
        }

    }

    /**
     * @description resets the store familyData to 
     * empty object
     */
    const deleteFamilyMembers = () => {
        familyMembers.value = {}
    }

    //--------DISPATCHERS-----------//


    async function dispatchGetFamily(memberId){
        try {
            const {status, data} = await API.family.getFamily(memberId)

            if(status === 200){
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

    async function dispatchCreateFamily(){
        try {
            const {status, data} = await API.family.createFamily();
            if (status === 201){
                createFamily(data)

                return {
                    success: true,
                    content:null
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

    async function dispatchUpdateFamily(familyId, input){
        try {
            const {status, data} = await API.family.updateFamily(familyId, input);
            if (status === 200){
                updateFamily(data)
                return {
                    success: true,
                    content:null
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

    async function dispatchDeleteFamily(familyId){
        try {
            const {status, data} = await API.family.deleteFamily(familyId);
            if (status === 200){
                deleteFamily(data)
                return {
                    success: true,
                    content:null
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

    async  function dispatchGetFamilyMember(memberId) {
        try {
            const {status, data} = await API.family.getFamilyMember(memberId)
            if (status === 200) {

                initMemberInfo(data)
                return {
                    success:true,
                    content: null,
                }
            }

        } catch (error) {
            return {
                success: false,
                content:null,
                status: error.response?.status
            }
        }

        return {
            success:false,
            content: null,
            status: 401
        }
    }
    
    async  function dispatchCreateFamilyMember(familyId, input) {
        try {
            const {status, data} = await API.family.createFamilyMember(familyId, input)
            if (status === 201) {
                createFamilyMember(data)
                return {
                    success:true,
                    content: null,
                }
            }

        } catch (error) {
            return {
                success: false,
                content:null,
                status: error.response?.status
            }
        }

        return {
            success:false,
            content: null,
            status: 401
        }
    }

    async  function dispatchUpdateFamilyMember(memberId) {
        try {
            const {status, data} = await API.family.updateFamilyMember(memberId)
            if (status === 200) {

                updateFamilyMember(data)
                return {
                    success:true,
                    content: null,
                }
            }

        } catch (error) {
            return {
                success: false,
                content:null,
                status: error.response?.status
            }
        }

        return {
            success:false,
            content: null,
            status: 401
        }
    }
    async  function dispatchDeleteFamilyMember(familyId, memberId) {
        try {
            const {status, data} = await API.family.deleteFamilyMember(familyId, memberId)
            if (status === 200) {

                deleteFamilyMember(data)
                return {
                    success:true,
                    content: null,
                }
            }

        } catch (error) {
            return {
                success: false,
                content:null,
                status: error.response?.status
            }
        }

        return {
            success:false,
            content: null,
            status: 401
        }
    }
    /**
     * @description actor that gets the family members based on the familyId
     * @param {*} memberId 
     * @returns 
     */
    async function dispatchGetFamilyMembers(familyId){
        try {
                const {status, data} = await API.family.getFamilyMembers(familyId)

            if(status === 200){
                // create familyMembers data
                initFamilyMembers(data)
                isFamilyEmpty.value = false

                return {
                    success: true,
                    content: null,
                }

            } else {
                isFamilyEmpty.value = true
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

    async function dispatchDeleteFamilyMembers(familyId) {
        try {
            const {status} = await API.family.deleteFamilyMembers(familyId)
            if (status === 204) {
                deleteFamilyMembers()

                return {
                    success: true,
                    content:null,
                }
            }
            
        } catch (error) {
            return {
                success:false,
                status: error.response?.status,
                content:null,
            }
        }
        
        return {
            success:false,
            content:null,
            status: 401,
        }
    } 

    return {
        $reset,
        initFamily,
        dispatchGetFamily,
        dispatchCreateFamily,
        dispatchUpdateFamily,
        dispatchDeleteFamily,
        dispatchGetFamilyMember,
        dispatchCreateFamilyMember,
        dispatchUpdateFamilyMember,
        dispatchDeleteFamilyMember,
        dispatchGetFamilyMembers,
        dispatchDeleteFamilyMembers,
        numberOfChildren,
        isFamilyEmpty,
        familyMembers,
        familyData,
        getFamilyName,
        getFamilyId,
        memberInfo,
        hasFamily,
        getCreatorId
    }

})
