<script setup>
import { useAuthStore } from '@/stores/auth'
import { useFamilyStore } from '@/stores/family'
import { useRouter } from 'vue-router'

const router = useRouter()

const authStore = useAuthStore()
const useFamily = useFamilyStore()

const person = defineProps({
  id: { type: String },
  img: {},
  first_name: { type: String },
  last_name: {},
  date_of_birth: {},
  role: { type: String }
})

const emit = defineEmits(['removeMember', 'cardClick'])
const handleRemove = () => {
  emit('removeMember')
}
const handleCardClick = () => {
  emit('cardClick', person.id)
}

const handleProfileClick = () => {
  router.push({ name: 'view', params: { _Id: person.id } })
}

const dateFormat = (date) => {
  let options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' }
  let formattedDate = date.toLocaleDateString('en-US', options)
  return formattedDate
}

// converts to JS date Object format
let dob = new Date(person.date_of_birth)
let formattedDate = dateFormat(dob)

// Capitalize functon
function capitalize(str) {
  return str.charAt(0).toUpperCase() + str.slice(1)
}

// Capitalzes the role funtion
let role = capitalize(person.role)

function goToTree(memberId) {
  router.replace({ name: 'tree', params: { familyId: memberId } })
}

function goToProfileEdit(memberId) {
  router.push({ name: 'edit', params: { _Id: memberId } })
}
</script>

<template>
  <VaCard :bordered="false" @click="handleCardClick">
    <div class="card-avatar">
      <VaAvatar
        :src="person.img ? person.img : 'https://randomuser.me/api/portraits/men/1.jpg'"
        size="large"
        @click.stop="handleProfileClick"
      />
    </div>
    <VaCardTitle class=""> {{ person.first_name }} {{ person.last_name }} </VaCardTitle>
    <VaCardContent>
      <div>
        <em>{{ role }}</em>
      </div>
      <div class="mb-4"><strong>Born: </strong>{{ formattedDate }}</div>
    </VaCardContent>
    <VaCardActions align="between" style="margin-top: 10px">
      <VaIcon name="info" size="medium" color="success" @click.stop="" />

      <VaIcon name="account_tree" size="medium" color="primary" @click.stop="goToTree(person.id)" />

      <VaIcon
        name="edit_square"
        size="medium"
        color="warning"
        @click.stop="goToProfileEdit(person.id)"
        v-if="
          authStore.getCurrentUserId === useFamily.getCreatorId ||
          person.id === authStore.getCurrentUserId
        "
      />

      <VaIcon
        name="delete"
        size="medium"
        @click.stop="handleRemove"
        color="danger"
        v-if="authStore.getCurrentUserId === useFamily.getCreatorId"
      />
    </VaCardActions>
  </VaCard>
</template>

<style scoped>
.va-card {
  width: 150px;
  padding: 20px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.15);
  margin-bottom: 20px;
  position: relative;
}
.va-card__content {
  padding: 0;
  /* background-color: aqua */
}
.va-avatar {
  margin: 0.5rem;
  height: 100px;
  width: 100px;
  align-self: center;
  border: solid 1px blue;
}
.card-avatar {
  display: flex;
  justify-content: center;
  align-items: center;
}

/* .va-card__actions{
  display: flex;
  justify-content: space-evenly;
} */
</style>
