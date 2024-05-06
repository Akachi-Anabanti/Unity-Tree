import { API } from "@/services";
import { defineStore } from "pinia";
import { computed, ref} from 'vue'


export const useFamilyStore =  defineStore('family',() =>{

    const familyMembers = ref({})
    const memberInfo = ref({})

    const familyData = ref({
        id:"1234DevId",
        name:"Smith"
    })

    const hasFamily = ref(false)

    // // Static data
    // familyData.value= {
    //     "father": {
    //     "name": "C-3PO",
    //     "dateOfBirth": new Date(1877, 2, 14).toDateString(),
    //     "img": "https://randomuser.me/api/portraits/men/1.jpg",
    //     "role":"parent"
    //     },
    //     "mother": {
    //     "name": "Luke Skywalker",
    //     "dateOfBirth": new Date(1887, 1, 29).toDateString(),
    //     "img": "https://randomuser.me/api/portraits/women/5.jpg",
    //     "role": "parent"
    //     },
    //     "children": [
    //     {
    //         "name": "Obi-Wan Kenobi",
    //         "dateOfBirth": new Date(1987, 1, 29).toDateString(),
    //         "img": "https://randomuser.me/api/portraits/men/2.jpg",
    //         "role": "child"
    //     },
    //     {
    //         "name": "Jabba Desilijic Tiure",
    //         "dateOfBirth": new Date(1787, 1, 29).toDateString(),
    //         "img": "https://randomuser.me/api/portraits/women/4.jpg",
    //         "role": "child"
    //     },
    //     {
    //         "name": "Yoda",
    //         "dateOfBirth": new Date(1987, 1, 29).toDateString(),
    //         "img": "https://randomuser.me/api/portraits/men/5.jpg",
    //         "role": "child"
    //     },
    //     {
    //         "name": "Darth Vader",
    //         "dateOfBirth": new Date(1897, 1, 29).toDateString(),
    //         "img": "https://randomuser.me/api/portraits/men/6.jpg",
    //         "role": "child"
    //     },
    //     {
    //         "name": "Obi-Wan Kenobi",
    //         "dateOfBirth": new Date(1887, 1, 29).toDateString(),
    //         "img": "https://randomuser.me/api/portraits/men/2.jpg",
    //         "role": "child"
    //     },
    //     ]
    // };

    const numberOfChildren = computed(() => familyMembers.value.children.length)
    const isFamilyEmpty = computed(() => Object.keys(familyMembers.value).length === 0)
    const getFamilyName = computed(() => familyData.value.name)
    const getFamilyId = computed(() => familyData.value.id)


    const getChildIdx = (person) => {
        return familyMembers.value.children.findIndex((cd) => cd.id === person.id)
    }

    /**
     * @description creates the inital familyMmebers data
     * @param {*} data 
     */
    const initFamily = (data) => {
        familyMembers.value = data
    }


    const createFamily = (data) => {
        familyData.value = data
    }
    
    const updateFamily = (data) => {
        familyData.value = data
    }

    const deleteFamily = () => {
        familyData.value = {}
    }

    const initMemberInfo = (person) => {
        memberInfo.value = person
    }

    const createFamilyMember = (person) => {
        if (person.role === 'child'){
            familyMembers.value.children.push(person)
        } else {
            familyMembers[person.role] = person
        }

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
            const index = familyMembers.value.children.findIndex((cd) => cd === person)
            if (index !== -1) {
              familyMembers.value.children.splice(index, 1)
            }
        } else
        {
            delete familyMembers.value[parent.role];
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
            if (status === 201){
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
            if (status === 201){
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

    async  function dispatchgetFamilyMember(memberId) {
        try {
            const {status, data} = await API.family.getFamilyMember(memberId)
            if (status === 201) {

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
            if (status === 201) {

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
            if (status === 201) {

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
    async function dispatchDeleteFamilyMembers(familyId) {
        try {
            const {status} = await API.family.deleteFamilyMembers(familyId)
            if (status === 200) {
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
        initFamily,
        dispatchGetFamily,
        dispatchCreateFamily,
        dispatchUpdateFamily,
        dispatchDeleteFamily,
        dispatchgetFamilyMember,
        dispatchCreateFamilyMember,
        dispatchUpdateFamilyMember,
        dispatchDeleteFamilyMember,
        dispatchDeleteFamilyMembers,
        numberOfChildren,
        isFamilyEmpty,
        familyMembers,
        getFamilyName,
        getFamilyId,
        memberInfo,
        hasFamily
    }

})
