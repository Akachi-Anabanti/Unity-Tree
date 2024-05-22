<script setup>
import { useAuthStore } from '@/stores/auth'
import { reactive } from 'vue'
import { useForm } from 'vuestic-ui'

const registerForm = reactive({
  first_name: '',
  last_name: '',
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
  <VaForm ref="myForm" class="form-grp">
    <div class="row-1">
      <div>
        <VaInput
          v-model="registerForm.first_name"
          type="text"
          placeholder="First Name"
          label="First Name"
          :rules="[
            (v) => Boolean(v) || 'Firstname is required',
            (v) => v.length >= 3 || 'minimum of 3 characters'
          ]"
        />
      </div>

      <div class="form-input">
        <VaInput
          v-model="registerForm.last_name"
          type="text"
          placeholder="Last Name"
          label="Last Name"
          :rules="[
            (v) => Boolean(v) || 'Lastname is required',
            (v) => v.length >= 3 || 'minimum of 3 characters'
          ]"
        />
      </div>
    </div>

    <div class="row-2">
      <div class="form-input">
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
      </div>
      <div class="form-input">
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
      </div>
    </div>

    <div class="row-3">
      <div class="form-input">
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
      </div>
      <div class="form-input">
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
      </div>
    </div>
      <VaButton
      :disabled="!isValid"
      @click="validate() && submit()"
      color="success"
      class="submit-btn"
      >Register
    </VaButton>
  </VaForm>
  <div class="alt-auth">
    <p>Already have an account?</p>
    <VaButton>
      <router-link to="login"> Login </router-link>
    </VaButton>
  </div>
</template>


<style scoped>
.form-grp {
  display: grid;
  grid-template-rows: repeat(3, auto); /* Adjusts the row height based on content */
  gap: 20px;
}

.row-1,
.row-2,
.row-3 {
  display: grid; /* Use grid instead of contents */
  grid-template-columns: 1fr 1fr;
  grid-auto-rows: auto; /* Adjusts the row height based on content */
  gap: 10px; /* Add gap between rows */
}

/* Add a class for error messages */
.error-message {
  grid-column: span 2; /* Makes the error message span both columns */
  color: red; /* Example color */
}

.alt-auth {
  justify-content: space-evenly;
  grid-column: span 2;
}
@media (max-width: 600px) {
  .row-1,
  .row-2,
  .row-3 {
    grid-template-columns: 1fr; /* Stack the inputs vertically on small screens */
  }
}

</style>
