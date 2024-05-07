<script setup>
// import { useAuthStore } from '@/stores/auth';
import { ref } from 'vue';
// const authStore = useAuthStore()
const email = ref("")
const  password = ref("")

// const {dispatchLogin} = authStore

</script>

<template>
    <VaInput
      v-model="email"
      type="email"
      placeholder="hello@epicmax.co"
      label="Email"
    />
    <VaValue
      v-slot="isPasswordVisible"
      :default-value="false"
    >
      <VaInput
        v-model="password"
        :type="isPasswordVisible.value ? 'text' : 'password'"
        label="Password with toggle"
        placeholder="#########"
        @click-append-inner="isPasswordVisible.value = !isPasswordVisible.value"
      >
        <template #appendInner>
          <VaIcon
            :name="isPasswordVisible.value ? 'visibility_off' : 'visibility'"
            size="small"
            color="primary"
          />
        </template>
      </VaInput>
    </VaValue>
    <VaButton>
      <router-link to="register">
        Register
      </router-link>
    </VaButton>
    
</template>