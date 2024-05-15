<script setup>
import { useAuthStore } from '@/stores/auth'
import { reactive } from 'vue'
import { useForm } from 'vuestic-ui'

const registerForm = reactive({
  username: '',
  email: '',
  password: '',
  password2: ''
})

const { validate, isValid } = useForm('myForm')

const authStore = useAuthStore()

const submit = async () => {
  try {
    await authStore.dispatchRegister(registerForm)
  } catch (error) {
    console.error(error)
  }
}

function validateEmail(email) {
  const re = /^[\w.-]+@[\w.-]+\.\w+$/
  return re.test(email)
}

function isValidPassword(password) {
  var regex = /^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{6,}$/
  return regex.test(password)
}
</script>

<template>
  <div>
    <VaForm ref="myForm" class="form-grp">
      <VaInput
        v-model="registerForm.username"
        type="text"
        placeholder="username"
        label="Username"
        :rules="[
          (v) => Boolean(v) || 'Username is required',
          (v) => v.length >= 3 || 'minimum of 3 characters'
        ]"
      />
      <VaInput
        for="email"
        v-model="registerForm.email"
        type="email"
        placeholder="hello@epicmax.co"
        label="Email"
        :rules="[
          (v) => Boolean(v) || 'Email is required',
          (v) => validateEmail(v) || 'Email is not valid'
        ]"
      />

      <!-- Password 1 -->
      <VaValue v-slot="isPasswordVisible" :default-value="false">
        <VaInput
          v-model="registerForm.password"
          :type="isPasswordVisible.value ? 'text' : 'password'"
          label="Password"
          placeholder="#########"
          @click-append-inner="isPasswordVisible.value = !isPasswordVisible.value"
          :rules="[
            (v) => Boolean(v) || 'Password is required',
            (v) =>
              isValidPassword(v) ||
              'Password must contian at least one number,\
        one special character, one uppercase and have a minimum of\
        6 characters'
          ]"
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
      <!-- Password 2 -->
      <VaValue v-slot="isPasswordVisible" :default-value="false">
        <VaInput
          v-model="registerForm.password2"
          :type="isPasswordVisible.value ? 'text' : 'password'"
          label="Password 2"
          placeholder="re-type password"
          @click-append-inner="isPasswordVisible.value = !isPasswordVisible.value"
          :rules="[(v) => v === registerForm.password || 'Passwords must match']"
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
        >Register
      </VaButton>
    </VaForm>
  </div>
  <div class="alt-auth">
    <p>Already have an account?</p>
    <VaButton>
      <router-link to="login"> Login </router-link>
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
  width: 70%;
}

.submit-btn {
  margin-left: 15px;
  width: 100%;
}

.alt-auth {
  justify-content: space-evenly;
}
</style>
