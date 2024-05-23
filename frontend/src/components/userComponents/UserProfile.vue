<script setup>
import { onMounted, watch, ref, onUnmounted, watchEffect } from 'vue'
import marqueeComponent from './marqueeComponent.vue'
import siblingsComponent from './siblingsComponent.vue'
import { useFamilyStore } from '@/stores/family'
import SpinnerComp from '../utilities/spinnerComp.vue'
import { useAuthStore } from '@/stores/auth'
import { VaForm, VaInput, VaButton, VaIcon, VaAvatar } from 'vuestic-ui'
import { useRouter } from 'vue-router'
import { useAlertStore } from '@/stores/alert'

const isLoading = ref(true)
const isEditing = ref('')
const formChanged = ref(false)

const props = defineProps({
  _Id: { type: String }
})

const useFamily = useFamilyStore()
const authStore = useAuthStore()
const router = useRouter()
const alertStore = useAlertStore()

const formValues = ref({})

watchEffect(() => {
  const unlisten = router.beforeEach((to, from, next) => {
    if (formChanged.value) {
      const answer = window.confirm('You have unsaved changes. Are you sure you want to leave?')
      if (answer) {
        next()
      } else {
        next(false)
      }
    } else {
      next()
    }
  })
  onUnmounted(unlisten)
})

onMounted(async () => {
  await useFamily.dispatchGetFamilyMember(props._Id)
  await useFamily.dispatchGetFamily(props._Id)
  await useFamily.dispatchGetSiblings(props._Id)
  formValues.value = { ...useFamily.memberInfo }
  delete formValues.value.id
  delete formValues.value.user_id
  delete formValues.value.created_at
  delete formValues.value.updated_at
  isLoading.value = false
})

watch(
  () => props._Id,
  async (newVal, oldVal) => {
    if (newVal !== oldVal) {
      isLoading.value = true
      await useFamily.dispatchGetFamilyMember(newVal)
      await useFamily.dispatchGetSiblings(newVal)
      formValues.value = { ...useFamily.memberInfo }
      isLoading.value = false
    }
  }
)

const avatarSizeConfig = {
  sizes: {
    large: 150
  }
}

function calculateAge(dateOfBirth) {
  const today = new Date()
  const birthDate = new Date(dateOfBirth)
  let age = today.getFullYear() - birthDate.getFullYear()
  const monthDifference = today.getMonth() - birthDate.getMonth()

  if (monthDifference < 0 || (monthDifference === 0 && today.getDate() < birthDate.getDate())) {
    age--
  }

  return age
}

function enableEditing(key) {
  isEditing.value = key
}

async function saveEdit() {
  try {
    const {success} = await useFamily.dispatchUpdateFamilyMember(props._Id, formValues.value)
    if (success) {
      isEditing.value = ''
      formChanged.value = false
      alertStore.dispatchShowMainAlertSuccess("Successfully update!")
    } else{
      alertStore.dispatchShowMainAlertFailure("update failed, Try again :)")
    }
  } catch (error) {
    alertStore.dispatchShowMainAlertFailure("Something went wrong!")
  }
}


function handleInputChange() {
  formChanged.value = true
}

function getInputType(key) {
  if (key.includes('date')) return 'date'
  if (key.includes('email')) return 'email'
  if (key.includes('phone')) return 'tel'
  if (key.includes('img')) return 'file'
  return 'text'
}
</script>

<template>
  <div v-if="isLoading" class="spinner-container">
    <SpinnerComp />
  </div>
  <div v-else class="profile-container">
    <div class="header-section">
      <VaAvatar
        size="large"
        :sizes-config="avatarSizeConfig"
        :src="useFamily.memberInfo.img ? useFamily.memberInfo.img : 'https://randomuser.me/api/portraits/women/4.jpg'"
      />
      <div class="right-header">
        <h2 v-if="useFamily.memberInfo.first_name">
          {{ useFamily.memberInfo.first_name }} {{ useFamily.memberInfo.last_name }}
        </h2>
        <h2 v-else>No name</h2>
        <p>Born: {{ useFamily.memberInfo.date_of_birth }}</p>
        <p>Age: {{ calculateAge(useFamily.memberInfo.date_of_birth) }}</p>
      </div>
    </div>
    <div class="gallery-section">
      <h3>Memories</h3>
      <marqueeComponent />
    </div>
    <div class="siblings" v-if="useFamily.getSiblingInfo.length > 0">
      <h3>Siblings</h3>
      <siblingsComponent :member-id="props._Id" />
    </div>
    <div>
      <h3>Detail</h3>
      <VaForm @submit.prevent="saveEdit" class="info-section" enctype="multipart/form-data">
        <div v-for="(value, key) in formValues" :key="key" class="info-item">
          <template v-if="isEditing === key && key !== 'registered'">
            <VaInput
              v-model="formValues[key]"
              :type="getInputType(key)"
              :label="key.replace('_', ' ')"
              @input="handleInputChange"
              :accept="key.includes('img') ? 'image/*' : undefined"      
            />
          </template>
          <template v-else>
            <p>
              {{ key.replace('_', ' ') }}: <strong>{{ value }}</strong>
              <VaIcon
                name="edit_square"
                class="edit-icon"
                @click.stop="() => enableEditing(key)"
                v-if="authStore.getCurrentUserId === useFamily.memberInfo.user_id || authStore.getCurrentUserId === useFamily.getCreatorId"
              />
            </p>
          </template>
        </div>
        <VaButton :disabled="!formChanged" v-if="isEditing" @click="saveEdit">Update</VaButton>
        <!-- <VaButton v-else @click="enableEditing">Edit</VaButton> -->
      </VaForm>
    </div>
  </div>
</template>

<style scoped lang="scss">
.spinner-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.profile-container {
  padding: 20px;
}

.header-section {
  display: grid;
  grid-template-columns: 1fr 2fr;
  column-gap: 20px;
  justify-items: center;
  align-items: center;
  margin: auto;
  width: 50%;
  padding-bottom: 50px;
  border-bottom: 1px solid black;

  .right-header {
    width: 100%;
    p {
      margin: 0;
    }
  }
}

.gallery-section, .siblings {
  margin-bottom: 30px;
}

.info-section {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;

  .info-item {
    position: relative;
    p {
      margin: 0;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px;
      background: #f9f9f9;
      border-radius: 5px;
    }

    .edit-icon {
      cursor: pointer;
      margin-left: 10px;
    }

    input {
      width: 100%;
      padding: 10px;
      border: 1px solid #ccc;
      border-radius: 5px;
    }
  }

  .va-button {
    margin-top: 20px;
    justify-self: end;
  }
}

@media (max-width: 900px) {
  .info-section {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 600px) {
  .header-section {
    grid-template-columns: 1fr;
    text-align: center;
    row-gap: 10px;
  }

  .info-section {
    grid-template-columns: 1fr;
  }
}

.highlight-green {
  border: 1px solid green;
}
</style>
