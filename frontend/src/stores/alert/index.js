import { defineStore } from 'pinia'
import { ref } from 'vue'
export const useAlertStore = defineStore('alert', () => {
  // Main Alert Modifiers

  const showMainAlertSuccess = ref(false)
  const showMainAlertFailure = ref(false)
  const showMainAlertWarning = ref(false)

  // Modal Alert Modifiers
  const showModalAlertSuccess = ref(false)
  const showModalAlertFailure = ref(false)
  const showModalAlertWarning = ref(false)

  const alertMessage = ref('')

  // Resets the store
  function $reset() {
    showMainAlertSuccess.value = false
    showMainAlertFailure.value = false
    showMainAlertWarning.value = false
    showModalAlertSuccess.value = false
    showModalAlertFailure.value = false
    showModalAlertWarning.value = false
    alertMessage.value = ''
  }

  function dispatchShowMainAlertSuccess(message) {
    showMainAlertSuccess.value = true
    alertMessage.value = message
    setTimeout(() => {
      showMainAlertSuccess.value = false
    }, 3000)
  }

  function dispatchShowMainAlertWarning(message) {
    showMainAlertWarning.value = true
    alertMessage.value = message
    setTimeout(() => {
      showMainAlertWarning.value = false
    }, 3000)
  }

  function dispatchShowMainAlertFailure(message) {
    showMainAlertFailure.value = true
    alertMessage.value = message
    setTimeout(() => {
      showMainAlertFailure.value = false
    }, 3000)
  }

  function dispatchShowModalAlertSuccess(message) {
    showModalAlertSuccess.value = true
    alertMessage.value = message
    setTimeout(() => {
      showModalAlertSuccess.value = false
    }, 3000)
  }

  function dispatchShowModalAlertWarning(message) {
    showModalAlertWarning.value = true
    alertMessage.value = message
    setTimeout(() => {
      showModalAlertWarning.value = false
    }, 3000)
  }

  function dispatchShowModalAlertFailure(message) {
    showModalAlertFailure.value = true
    alertMessage.value = message
    setTimeout(() => {
      showModalAlertFailure.value = false
    }, 3000)
  }

  return {
    $reset,
    showMainAlertSuccess,
    showMainAlertWarning,
    showMainAlertFailure,
    showModalAlertSuccess,
    showModalAlertWarning,
    showModalAlertFailure,
    alertMessage,
    dispatchShowMainAlertSuccess,
    dispatchShowMainAlertWarning,
    dispatchShowMainAlertFailure,
    dispatchShowModalAlertSuccess,
    dispatchShowModalAlertWarning,
    dispatchShowModalAlertFailure
  }
})
