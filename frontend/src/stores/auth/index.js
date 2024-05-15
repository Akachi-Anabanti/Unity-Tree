import { API } from '@/services'
import { defineStore } from 'pinia'
import { computed, ref } from 'vue'
import { useUserStore } from '../user'
import { useAlertStore } from '../alert'
import { getCookie, saveLocalToken, removeLocalToken, getLocalToken } from '@/utils'
import { useRouter } from 'vue-router'
import { useFamilyStore } from '../family'

export const useAuthStore = defineStore('auth', () => {
  const router = useRouter()

  const userStore = useUserStore()
  const alertStore = useAlertStore()

  const isLoggedIn = ref(false)
  const token = ref(null)
  const isAuthenticated = computed(() => (isLoggedIn.value === true ? true : false))
  const isSuperUser = ref(false)
  const currentUser = ref(null)
  const returnUrl = ref(null)
  const currentUserHasFamily = ref(false)

  const getCurrentUserId = computed(() => (currentUser.value ? currentUser.value.id : null))

  // resets the store
  function $reset() {
    isLoggedIn.value = false
    token.value = null
    isSuperUser.value = false
    // currentUser.value = null
  }

  const setUser = (user) => {
    currentUser.value = user
  }

  const setReturnUrl = async (urlPath) => {
    returnUrl.value = urlPath
  }

  const logout = () => {
    isLoggedIn.value = false
    removeLocalToken()
    setUser(null)

    // resets all the stores
    useUserStore().$reset()
    useFamilyStore().$reset()
    $reset()

    // redirects to login page
    router.push('/account/login')
  }

  async function dispatchCheckLoggedIn() {
    if (!isLoggedIn.value) {
      if (!token.value) {
        const localToken = getCookie('csrf_access_token')
        if (localToken) {
          token.value = localToken
          isLoggedIn.value = true
        } else {
          logout()
        }
      }
      if (token.value) {
        try {
          isLoggedIn.value = true
          const { data } = await API.users.getUser()
          setUser(data)
        } catch (error) {
          logout()
        }
      } else {
        logout()
      }
    }
  }
  async function dispatchLogin(credentials) {
    try {
      const { status, data } = await API.auth.login(credentials)
      if (status == 200) {
        const tokenVal = getCookie('csrf_access_token')
        if (tokenVal) {
          saveLocalToken(tokenVal)
          const { content } = await userStore.dispatchGetUser()
          token.value = tokenVal
          setUser(content)

          isLoggedIn.value = true
          router.push(returnUrl.value || '/')

          alertStore.dispatchShowMainAlertSuccess(data.message)
        }
      } else {
        dispatchLogout()
        alertStore.dispatchShowMainAlertFailure(data.message)
      }
    } catch (error) {
      return {
        success: false,
        content: null,
        status: error.response?.status
      }
    }
    return {
      success: false,
      content: null,
      status: 401
    }
  }

  async function dispatchLogout() {
    try {
      const { message } = await API.auth.logout()
      logout()
      return {
        success: true,
        content: message
      }
    } catch (error) {
      return {
        success: false,
        content: null,
        status: error.response?.status
      }
    }
  }

  async function dispatchRegister(info) {
    try {
      const { status } = await API.auth.register(info)
      if (status == 201) {
        const credentials = {
          password: info.password,
          email: info.email
        }
        // if registration is successful automatically login
        //  user and update
        dispatchLogin(credentials)
      }
    } catch (error) {
      return {
        success: false,
        content: null,
        status: error.response?.status
      }
    }
    return {
      success: false,
      content: null,
      status: 401
    }
  }

  async function dispatchCheckCurrentUserHasFamily() {
    try {
      const { status, data } = await API.family.getFamily(getCurrentUserId.value)
      if (status == 200) {
        currentUserHasFamily.value = true
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
    isAuthenticated,
    isSuperUser,
    currentUser,
    getCurrentUserId,
    currentUserHasFamily,
    setReturnUrl,
    dispatchLogin,
    dispatchLogout,
    dispatchRegister,
    dispatchCheckLoggedIn,
    dispatchCheckCurrentUserHasFamily
  }
})
