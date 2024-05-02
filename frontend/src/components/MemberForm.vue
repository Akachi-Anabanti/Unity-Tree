<template>
    <VaForm ref="formRef" class="items-baseline gap-6">
      <VaInput
        v-model="form.firstName"
        :rules="[(value) => (value && value.length > 0) || 'First name is required']"
        label="firstName"
      />
    
      <VaInput
        v-model="form.lastName"
        :rules="[(value) => (value && value.length > 0) || 'Last name is required']"
        label="Last Name"
      />
    
      <VaDateInput 
        v-model="form.birthDate"
        :rules="[(value) => validateBirthday(value)]"
        label="Birth Date"
        manual-input
        clearable
      />
      <div>
        <span class="va-title">Gender</span>
        <VaOptionList
          v-model="form.Gender"
          :options="['Female', 'Male']"
          type="radio"
        />      
      </div>
      
      <VaFileUpload
        v-model='basic'
       
        file-types="jpg,png,jpeg"
        />

      <div class="m-8">
        <VaButton color="success" :disabled="!isValid" @click="validate() && submit()">
          Save
      </VaButton>
      </div>
   
    </VaForm>
  </template>
  

<script setup lang="ts">
import { reactive } from 'vue';
import { useForm } from 'vuestic-ui';
import { ref } from 'vue'

const basic = ref([])

const { isValid, validate } = useForm('formRef')

const form = reactive({
  firstName: '',
  lastName: '',
  country: '',
  birthDate: null,
  Gender: '',
})

const validateBirthday = (value) => {
  if (!value) {
    return 'Field is required'
  }
}
//   const today = new Date()
//   let yearDiff = today.getFullYear() - value.getFullYear()
//   const monthDiff = today.getMonth() - value.getMonth()

//   if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < value.getDate())) {
//     yearDiff--
//   }

//   return yearDiff >= 18 || 'You must be at least 18 years old'
// }


const submit = () => { 
  alert("Form Saved Successfully")
}
</script>