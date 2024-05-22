<script setup>
import TreeComponent from '@/components/TreeComponent.vue'
import modalComponent from '@/components/modalComponent.vue'
import MemberForm from '@/components/MemberForm.vue'
import { onBeforeMount, ref } from 'vue'
import { useAlertStore } from '@/stores/alert'
import { useFamilyStore } from '@/stores/family'
import { onBeforeRouteLeave, useRouter } from 'vue-router'

const router = useRouter()
const useAlert = useAlertStore()
const useFamily = useFamilyStore()

const props = defineProps({ familyId: { type: String, required: true } })

const showModal = ref(false)

onBeforeMount(async () => {
  await useFamily.dispatchGetFamily(props.familyId)

  if (!useFamily.hasFamily) {
    useAlert.dispatchShowMainAlertFailure('This family does not exist consider creating it')
    await router.push('/')
  }
})

onBeforeRouteLeave(() => {
  useFamily.$reset()
})

// Function to handle Modal Form Submit
const handleFormSubmit = async (newMember) => {
  try {
    const res = await useFamily.dispatchCreateFamilyMember(useFamily.getFamilyId, newMember)
    if (res.success) {
      const message = `${newMember.firstName} added successfully as ${newMember.role}!`
      useAlert.dispatchShowModalAlertSuccess(message)
    } else {
      const message = 'Failed to Add member!'
      useAlert.dispatchShowModalAlertFailure(message)
    }
  } catch (error) {
    console.error(error)
  }
}
</script>

<template>
  <div v-if="useFamily.hasFamily">
    <modalComponent v-model="showModal">
      <template #form>
        <MemberForm @submit="handleFormSubmit" />
      </template>
    </modalComponent>

    <!-- Add member button -->
    <div class="flex items-center gap-8 flex-wrap add-member">
      <VaButton round icon="va-plus" size="large" @click="showModal = true" />
    </div>
    <TreeComponent :family-id="props.familyId" />
  </div>
</template>

<style scoped>
.add-member {
  position: fixed;
  right: 70px;
  bottom: 50px;
  z-index: 100;
}

.va-modal {
  opacity: 0;
}

.zoom-effect {
  animation: zoom 2s;
}

@keyframes zoom {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.1);
  }
  100% {
    transform: scale(1);
  }
}
</style>
