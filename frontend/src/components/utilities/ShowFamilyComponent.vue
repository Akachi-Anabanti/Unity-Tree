<script setup>
import { useUserStore } from '@/stores/user'
import { onBeforeMount, watchEffect, ref, reactive } from 'vue'
import AddFamily from './createFamilyButton.vue'
import { useAuthStore } from '@/stores/auth'
import { useFamilyStore } from '@/stores/family'
import { useRouter } from 'vue-router'
import { useAlertStore } from '@/stores/alert'
import { storeToRefs } from 'pinia'


const userStore = useUserStore()
const authStore = useAuthStore()
const useFamily = useFamilyStore()
const useAlert = useAlertStore()
const router = useRouter()

const family = ref(userStore.getFamily)


const showConfirmModal = ref(false)
const modalRemoveFamily = ref({})
const modalRemoveFamId = ref('')
const confirmModalDelete = ref(false)


const modalButtonOptions = ref({
  color: 'danger',
  hoverMaskColor: '#ffff'
})


const handleModalOk = async (hide) => {
  // set modaldelte value
  confirmModalDelete.value = true
  hide()
}

// Handles Child member removal
const promptDelete = (family) => {
  modalRemoveFamily.value = family
  modalRemoveFamId.value = modalRemoveFamily.value.id
  showConfirmModal.value = true
}

// watches for the change in value of confirmModal.delte value
// and sends the dispatches
watchEffect(async () => {
  if (confirmModalDelete.value) {
    try {
      const { success } = await useFamily.dispatchDeleteFamily(modalRemoveFamily.value.id)
      if (success) {
        const message = `${modalRemoveFamily.value.name} deleted!`
        useAlert.dispatchShowMainAlertSuccess(message)
      } else {
        useAlert.dispatchShowMainAlertFailure('failed to delete ! try again :)')
      }
    } catch (error) {
      console.error(error)
    }

    confirmModalDelete.value = !confirmModalDelete.value
  }
})

const navigateToTree = async(familyId) => {
  router.push({ name: 'tree', params: { familyId: familyId } })
}
</script>
<template>
  <VaModal
    v-model="showConfirmModal"
    size="auto"
    okText="Yes"
    cancelText="No"
    :child:okButton="modalButtonOptions"
    :beforeOk="handleModalOk"
  >
    Delete <em>{{ modalRemoveFamily.name }} </em> family?
  </VaModal>

  <div class="fam-cards">
    <div v-for="family in family" :key="family.id" class="fam-card">
      <VaCard :bordered="false" stripe @click="navigateToTree(family.id)">
        <VaCardTitle>{{ family.name }}</VaCardTitle>
        <VaCardContent>
          {{ family.created_at }}
        </VaCardContent>
        <VaCardActions>
          <VaIcon
            name="delete"
            color="danger"
            @click.stop="promptDelete(family)"
            v-if="authStore.getCurrentUserId === family.creator_id"
            class="fam-delete-icon"
          />
        </VaCardActions> 
      </VaCard>
    </div>
  </div>
  <AddFamily />
</template>

<style scoped>
.fam-cards {
  display: flex;
  flex-wrap: wrap;
}
.fam-card {
  margin: 5px;
  transition: transform 0.3s ease-in-out;
  position: relative;
}
.fam-card:hover {
  transform: scale(1.05);
  cursor:pointer;
}
.fam-delete-icon{
  z-index: 999;
  position: absolute;
}
</style>
