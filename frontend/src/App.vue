<script setup lang="ts">
  import { useAuthStore } from './stores/auth';
  import mainLayout from '@/components/AppLayoutComponent.vue'
  const authStore = useAuthStore();
</script>

<template>
  <mainLayout v-if="authStore.isAuthenticated" />
  <RouterView />
</template>
