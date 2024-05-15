<script setup>
import { useAuthStore } from '@/stores/auth'
import { reactive } from 'vue'
import { useForm } from 'vuestic-ui'

const form = reactive({
  email: '',
  password: ''
})

const { validate, isValid } = useForm('myForm')

const authStore = useAuthStore()

function validateEmail(email) {
  const re = /^[\w.-]+@[\w.-]+\.\w+$/
  return re.test(email)
}

const submit = async () => {
  let res
  try {
    res = await authStore.dispatchLogin(form)
  } catch (error) {
    console.error(error)
    console.log(res)
  }
}
</script>

<template>
  <VaForm ref="myForm" class="form-grp">
    <VaInput
      v-model="form.email"
      type="email"
      placeholder="hello@epicmax.co"
      label="Email"
      :rules="[
        (v) => Boolean(v) || 'Email is required',
        (v) => validateEmail(v) || 'Invalid email address'
      ]"
    />

    <VaValue v-slot="isPasswordVisible" :default-value="false">
      <VaInput
        v-model="form.password"
        :type="isPasswordVisible.value ? 'text' : 'password'"
        label="Password"
        placeholder="#########"
        @click-append-inner="isPasswordVisible.value = !isPasswordVisible.value"
        :rules="[(v) => Boolean(v) || 'Password is required']"
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
    <VaButton
      :disabled="!isValid"
      @click="validate() && submit()"
      color="success"
      class="submit-btn"
    >
      Login
    </VaButton>
  </VaForm>

  <div class="alt-auth">
    <p>Don't have an account?</p>
    <VaButton size="medium">
      <router-link to="register"> Register </router-link>
    </VaButton>
  </div>
</template>

<style scoped>
.form-grp {
  justify-content: center;
  align-items: center;
  display: grid;
  grid-template-columns: 1fr;
  margin: auto;
  height: 50%;
  width: 50%;
}

.submit-btn {
  margin-left: 15px;
  width: 100%;
}

.alt-auth {
  justify-content: space-around;
  margin: 10px;
  justify-content: right;
}
</style>
