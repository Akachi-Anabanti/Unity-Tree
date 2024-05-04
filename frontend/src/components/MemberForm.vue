<template>
    <VaForm ref="formRef" class="items-baseline gap-6"
    >
      <VaInput
        v-model="form.name"
        :rules="[(value) => (value && value.length > 0) || 'Full name is required']"
        label="fullName"
      />
    
      <!-- <VaInput
        v-model="form.lastName"
        :rules="[(value) => (value && value.length > 0) || 'Last name is required']"
        label="Last Name"
      /> -->
    
      <VaDateInput
        v-model="form.dateOfBirth"
        :rules="[(value) => validateBirthday(value)]"
        label="Birth Date"
        manual-input
        clearable
      />
      <!-- <div>
        <span class="va-title">Gender</span>
        <VaOptionList
          v-model="form.Gender"
          :options="['Female', 'Male']"
          type="radio"
        />      
      </div> -->
      
      <VaSelect
        v-model="form.role"
        :options="roleOptions"
        placeholder="Role"
       /> 


      <VaFileUpload
        v-model='basic'
        file-types="jpg,png,jpeg"
        />

      <div class="m-8">
        <VaButton color="success" :disabled="!isValid" @click="validate() && submit()">
          Add
        </VaButton>
      </div>
   
    </VaForm>
  </template>

<script setup lang="ts">
import { reactive, watch } from 'vue';
import { useForm } from 'vuestic-ui';
import { ref } from 'vue'

const emit = defineEmits(['submit'])

const basic = ref([])

const { isValid, validate, resetValidation, reset} = useForm('formRef')

const form = reactive({
  name: '',
  dateOfBirth: null,
  img: "",
  role: ""
})
const roleOptions = ref([
  'child',
  'parent'
])
watch(() => basic.value, () => {
  if (form.img) {
    URL.revokeObjectURL(form.img);
  }
  if (basic.value.length > 0) {
    form.img = URL.createObjectURL(basic.value[0]);
  }
})

const validateBirthday = (value) => {
  if (!value) {
    return 'Field is required'
  }
}


const submit =  () => {
  const formCopy = {...form}
  emit('submit', formCopy)
  resetValidation()
  reset()
}
</script>