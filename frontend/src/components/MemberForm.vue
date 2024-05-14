
<script setup lang="ts">
import { reactive, watch } from 'vue';
import { useForm } from 'vuestic-ui';
import { ref } from 'vue'


const emit = defineEmits(['submit'])

const basic = ref([])

const { isValid, validate, resetValidation, reset} = useForm('formRef')

const form = reactive({
  firstName: '',
  dateOfBirth: null,
  img: "",
  role: ""
})
const roleOptions = ref([
  'child',
  'mother',
  'father'
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
    return false
  }
}


const submit =  () => {
  const formCopy = {...form}
  emit('submit', formCopy)
  resetValidation()
  reset()
}

// the end date of the date picker
// gets the current year
const date_picker_end_date = new Date().getFullYear()
</script>


<template>
    <VaForm ref="formRef" class="items-baseline gap-6"
    >
      <VaInput
        v-model="form.firstName"
        :rules="[(value) => (value && value.length > 0) || 'First name is required']"
        label="First Name"
      />
    
      <VaDateInput
        v-model="form.dateOfBirth"
        :rules="[(value) => validateBirthday(value)]"
        label="Birth Date"
        manual-input
        clearable
        :start-year=1600
        :end-year=date_picker_end_date
        highlight-weekend
        :allowed-days="(date) => {
          const today = new Date()
          today.setHours(0,0,0,0)
          return date <= today
        }"
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