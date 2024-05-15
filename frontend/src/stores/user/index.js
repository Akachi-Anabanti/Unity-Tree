import { API } from '@/services'
import { defineStore } from 'pinia'
import { useAuthStore } from '../auth'
import { computed, reactive } from 'vue'
import family from '@/services/family'

export const useUserStore = defineStore('userStore', () => {
  const authStore = useAuthStore()

  let familiesCreated = reactive({ data: null })

  const numberOfFamiliesCreated = computed(() =>
    familiesCreated.data ? familiesCreated.data.length : 0
  )

  const isNumberFamiliesCreatedZero = computed(() => numberOfFamiliesCreated.value === 0)

  function $reset() {
    familiesCreated.data = []
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

  return {
    $reset,
    isNumberFamiliesCreatedZero,
    numberOfFamiliesCreated,
    getFamily,
    deleteFamily,
    dispatchGetUser,
    dispatchDeleteUser,
    dispatchUpdateUser,
    dispatchGetFamiliesCreated
  }
})
