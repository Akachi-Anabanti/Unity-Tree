import axios from 'axios'
import { getCookie } from '@/utils'
import { useRouter } from 'vue-router'
import { useAlertStore } from '@/stores/alert'
const router = useRouter()

const instance = axios.create({
  baseURL: import.meta.env.VITE_API_ENDPOINT,
  withCredentials: true,
  withXSRFToken: true
})

instance.interceptors.request.use(async (config) => {
  if (config.url !== '/register' && config.url !== '/login' && config.url !== '/status') {
    config.headers['X-CSRF-TOKEN'] = getCookie('csrf_access_token')
    config.headers['Content-Type'] = 'application/json'
  }
  return config
})

instance.interceptors.response.use(
  (response) => {
    // If the request succeeds, we don't have to do anything and just return the response
    return response
  },
  (error) => {
    if (error.response && error.response.status === 401) {
      const useAlert = useAlertStore()
      useAlert.dispatchShowMainAlertFailure(error.response.data.msg)
      router.push('/account/login')
      return error.response
    }

    // If the error is due to other reasons, we just throw it back to axios
    return Promise.reject(error)
  }
)

export default instance
