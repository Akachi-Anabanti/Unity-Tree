<template>
  <VaForm ref="formRef" class="form-group gap-6">
    <VaInput
      v-model="form.name"
      :rules="[(value) => (value && value.length > 0) || 'Family name is required']"
      label="Family Name"
    />

    <VaSelect
      v-model="form.country"
      :options="countries"
      :rules="[(v) => v || 'Field is required']"
      label="Country"
      searchable
      virtual-scroller
      clearable
    />

    <VaSelect
      v-model="form.state"
      :options="states"
      label="State"
      searchable
      virtual-scroller
      clearable
    />

    <VaSelect
      v-model="form.city"
      :options="cities"
      label="City"
      searchable
      virtual-scroller
      allow-create="unique"
      clearable
    />

    <VaCheckbox v-model="form.member" label="Are you a member of this family?" />

    <VaSelect
      v-model="form.role"
      :options="roles"
      :rules="[(v) => (form.member ? Boolean(v) || 'Field is required' : true)]"
      label="Your role"
      :disabled="!form.member"
      clearable
    />

    <VaButton :disabled="!isValid" @click="validate() && submit()"> Submit </VaButton>
  </VaForm>
  <div class="mt-8 flex w-full gap-3 background-element">
    <VaButton @click="reset"> Reset </VaButton>
  </div>
</template>

<script setup>
import { reactive, ref, watch, watchEffect } from 'vue'
import { useForm } from 'vuestic-ui'
import { Country, State, City } from 'country-state-city'
import { useFamilyStore } from '@/stores/family'
import { useAlertStore } from '@/stores/alert'
import { useRouter } from 'vue-router'

const { isValid, validate, reset } = useForm('formRef')
const useFamily = useFamilyStore()
const useAlert = useAlertStore()
const router = useRouter()

const form = reactive({
  name: '',
  country: '',
  state: '',
  city: '',
  role: '',
  member: false
})

const roles = ['child', 'mother', 'father']

const countries = Country.getAllCountries().map((country) => ({
  value: country.isoCode,
  text: country.name
}))
let states = []
let cities = []

watch(
  () => form.country,
  (newCountry) => {
    states = State.getStatesOfCountry(newCountry.value).map((state) => ({
      value: state.isoCode,
      text: state.name
    }))
    form.state = ''
    form.city = ''
  }
)

watch(
  () => form.state,
  (newState) => {
    cities = City.getCitiesOfState(form.country.value, newState.value).map((city) => ({
      value: city.name,
      text: city.name
    }))
    form.city = ''
  }
)

watchEffect(() => {
  if (!form.member) {
    form.role = ''
  }
})

const submit = async () => {
  const formcpy = {
    name: form.name,
    country: form.country.text,
    state: form.state.text,
    city: form.city.text,
    role: form.role,
    member: form.member
  }
  try {
    const { success } = await useFamily.dispatchCreateFamily(formcpy)
    if (success) {
      useAlert.dispatchShowMainAlertSuccess('Family created successfully')
      router.push('/')
    } else {
      useAlert.dispatchShowMainAlertFailure('Failed to create family!')
    }
  } catch (error) {
    console.error(error)
  }
}
</script>

<style scoped>
.form-group {
  justify-content: center;
  align-items: center;
  display: grid;
  grid-template-columns: 1fr;
  margin: auto;
  height: 50%;
  width: 50%;
}
</style>
