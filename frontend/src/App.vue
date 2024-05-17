<script setup>
import { onBeforeMount, ref } from 'vue'
import { useAuthStore } from './stores/auth'
import { useUserStore } from './stores/user';

const authStore = useAuthStore()
// const useFamily = useFamilyStore()
const userStore = useUserStore()
const isLoading = ref(true)

onBeforeMount(async () => {
  // check if user is logged in
  await authStore.dispatchCheckLoggedIn()
  isLoading.value = false
})
</script>

<template>
  <div class="spinner-container" v-if="isLoading">
    <div class="spinner"></div>
  </div>
  <RouterView v-else />
</template>

<style scoped>
.api-status-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  animation: blink 1s infinite;
  position: absolute;
  bottom: 2%;
  right: 2%;
}

.api-status-dot.online {
  background-color: green;
}

.api-status-dot.offline {
  background-color: yellow;
}

@keyframes blink {
  0% {
    opacity: 0.2;
  }
  50% {
    opacity: 1;
  }
  100% {
    opacity: 0.2;
  }
}

.spinner-container {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(5px);
}

.spinner {
  border: 7px solid var(--va-background-primary);
  border-top: 7px solid var(--va-primary);
  border-radius: 50%;
  width: 120px;
  height: 120px;
  animation: spin 2s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
