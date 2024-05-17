import { API } from '@/services'
import { defineStore } from 'pinia'
import { useAuthStore } from '../auth'
import { computed, reactive, ref } from 'vue'

export const useUserStore = defineStore('userStore', () => {

  const currentUserHasFamily = ref(false)
  const authStore = useAuthStore()
  

  let familiesCreated = reactive({ data: null })
  const currentUserFamilyData = ref(null)


  // gets the number of families created by the current user

  const numberOfFamiliesCreated = computed(() =>
    familiesCreated.data ? familiesCreated.data.length : 0
  )
  // checks if the number of families created by the user is zero
  const isNumberFamiliesCreatedZero = computed(() => numberOfFamiliesCreated.value === 0)
  const getUserFamilyId = computed(() => currentUserFamilyData? currentUserFamilyData.value.id:null)


  // resets the store values to default
  function $reset() {
    familiesCreated.data = []
    currentUserHasFamily.value = false
    currentUserFamilyData.value = null
  }

  const getFamily = computed(() => familiesCreated.data)

  const deleteFamily = (family) =>{
    const index = familiesCreated.data.findIndex((fm) => fm.id === family.id)
    if (index !== -1) {
      familiesCreated.data.splice(index, 1)
    }
  }

  async function dispatchGetUser() {
    try {
      const { status, data } = await API.users.getUser()
      if (status == 200) {
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
      success: false,
      content: null,
      status: 400
    }
  }

  // deletes a user from the db and updates the state
  async function dispatchDeleteUser(id) {
    try {
      const { status } = await API.users.deleteUser(id)
      if (status == 200) {
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
      success: false,
      content: null,
      status: 400
    }
  }

  // updates the user in the database
  async function dispatchUpdateUser(id, input) {
    try {
      const { status } = await API.users.updateUser(id, input)
      if (status == 200) {
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
      success: false,
      content: null,
      status: 400
    }
  }

  async function dispatchGetFamiliesCreated() {
    try {
      const { status, data } = await API.users.getFamiliesCreated()
      if (status === 200) {
        familiesCreated.data = data
        return {
          success: true,
          content: null
        }
      }
    } catch (error) {
      return {
        success: false,
        content: null,
        status: error.response?.status
      }
    }
  }

  async function dispatchGetUserFamily() {
    try {
      const { status, data } = await API.users.getUserFamily()
      if (status === 200) {
        currentUserHasFamily.value = true
        currentUserFamilyData.value = data
        return {
          success: true,
          content: null
        }
      }
    } catch (error) {
      return {
        success: false,
        content: null,
        status: error.response?.status
      }
    }
  }

  return {
    $reset,
    getFamily,
    getUserFamilyId,
    currentUserHasFamily,
    numberOfFamiliesCreated,
    isNumberFamiliesCreatedZero,
    deleteFamily,
    dispatchGetUser,
    dispatchDeleteUser,
    dispatchUpdateUser,
    dispatchGetUserFamily,
    dispatchGetFamiliesCreated
  }
})
