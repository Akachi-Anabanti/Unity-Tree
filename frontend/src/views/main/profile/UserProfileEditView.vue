<template>
  <div v-if="isLoading">
    <SpinnerComp />
  </div>
  <VaForm ref="updateForm" v-else>
    <VaInput v-model="form.first_name" label="Firts Name"></VaInput>
    <VaInput v-model="form.nickname" label="Nickname"></VaInput>
    <VaInput v-model="form.ethnicity" label="Ethnicity"></VaInput>
    <VaInput v-model="form.gender" label="Gender"></VaInput>
    <VaInput v-model="form.genotype" label="Genotype"></VaInput>
    <VaInput v-model="form.height" label="Height"></VaInput>
    <VaInput v-model="form.hobbies" label="Hobbies"></VaInput>
    <VaInput v-model="form.nationality" label="Nationlity"></VaInput>
    <VaInput v-model="form.occupation" label="Occupation"></VaInput>
    <VaInput v-model="form.blood_group" label="Blood Group"></VaInput>
    <VaInput v-model="form.skin_color" label="Skin Color"></VaInput>
    <VaInput v-model="form.state_of_origin" label="State Of Origin"></VaInput>
    <VaInput v-model="form.race" label="Race"></VaInput>
    <VaInput v-model="form.marital_status" label="Marital Status"></VaInput>
    <VaButton @click="validate() && Submit()">update</VaButton>
  </VaForm>
</template>

<script setup>
import SpinnerComp from '@/components/utilities/spinnerComp.vue'
import { useFamilyStore } from '@/stores/family'
import { formToJSON } from 'axios'
import { ref, reactive, onMounted } from 'vue'
import { useForm } from 'vuestic-ui'

const { isValid, validate, resetValidation, reset } = useForm('updateForm')

const isLoading = ref(true)
const useFamily = useFamilyStore()

const props = defineProps({ _Id: { type: String } })

onMounted(async () => {
  await useFamily.dispatchGetFamilyMember(props._Id)
  isLoading.value = false
})

const form = reactive({
  first_name: useFamily.memberInfo.first_name,
  nickname: useFamily.memberInfo.nickname,
  ethnicity: useFamily.memberInfo.ethnicity,
  gender: useFamily.memberInfo.gender,
  genotype: useFamily.memberInfo.genotype,
  height: useFamily.memberInfo.height,
  hobbies: useFamily.memberInfo.hobbies,
  nationality: useFamily.memberInfo.nationality,
  occupation: useFamily.memberInfo.occupation,
  skin_color: useFamily.memberInfo.skin_color,
  state_of_origin: useFamily.memberInfo.state_of_origin,
  race: useFamily.memberInfo.race,
  marital_status: useFamily.memberInfo.marital_status
})

function Submit() {
  console.log(formToJSON(form))
}
</script>
