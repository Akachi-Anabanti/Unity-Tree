<script setup>
  import { onBeforeMount, ref } from 'vue'
  import MemberForm from '@/components/MemberForm.vue'
  import TreeComponent from '@/components/TreeComponent.vue';
  import modalComponent from '@/components/modalComponent.vue';
  import AlertComponent from '@/components/AlertComponent.vue';
  import { useAlertStore } from '@/stores/alert';
  import { useFamilyStore } from '@/stores/family';

  const isLoading = ref(true)
  const currentUser = ref({createdFamilies:[]})

  onBeforeMount(async()=>{
    await useFamily.dispatchGetFamily("testMemberId")

    if(useFamily.hasFamily) {
      await useFamily.dispatchGetFamilyMembers(useFamily.familyData.id)
    }
    isLoading.value = false
  })

  const useAlert = useAlertStore()
  const useFamily = useFamilyStore()


  const showModal = ref(false);


// Function to handle Modal Form Submit
  const handleFormSubmit = async (newMember) => {
    await useFamily.dispatchCreateFamilyMember(useFamily.getFamilyId, newMember)
    .then((res) => {
      console.log(res)
      if (res.success) {
        const message = `${newMember.firstName} added successfully as ${newMember.role}!`
        useAlert.dispatchShowModalAlertSuccess(message)
      } else {
        const message = "Failed to Add member!"
        useAlert.dispatchShowModalAlertFailure(message)
      }
    }).catch((error) => {
      console.error(error)
    })
  }


</script>

<template>
    <!-- Alert component -->
    <div class="main-alert">
        <AlertComponent
            :alert-message="useAlert.alertMessage"
            :show-alert-success="useAlert.showMainAlertSuccess"
            :show-alert-warning="useAlert.showMainAlertWarning"
            :show-alert-failure="useAlert.showMainAlertFailure"
        />
    </div>

    <!-- Modal Component -->
    <modalComponent v-model="showModal"
    >
        <template #form>
            <MemberForm  @submit="handleFormSubmit"/>
        </template>
    </modalComponent>

    <!-- Add member button -->
    <div v-if="useFamily.hasFamily && useFamily.familyMembersLoaded" class="flex items-center gap-8 flex-wrap add-member">
        <VaButton round icon="va-plus" size="large" @click="showModal = true"/>
    </div>

    <!-- The family tree component -->
    <div v-if="isLoading">
      Loading...
    </div>
    <div v-else-if="useFamily.hasFamily && useFamily.familyMembersLoaded">
        <TreeComponent />
    </div>
    <div v-else>
      <div v-if="currentUser.createdFamilies.length > 0">
        Here are the families you created
      </div>
      <div v-else>
        Create a Family tree now!
      </div>
    </div>
</template>

<style scoped>
.add-member{
    position: fixed;
    right: 70px;
    bottom: 50px;
    z-index: 100;
}

.va-modal{
    opacity: 0;
}

.main-alert{
  position: fixed;
  z-index: 1;
  left: 35%;
  right: 35%;
  width: 30%;
  top: 90%;
  align-items: center;
  animation: swell 2s  infinite ease-in-out;
}
@keyframes swell {
  0%, 100% {
    transform: scale(1); /* Start and end at normal size */
  }

  50% {
    transform: scale(1.1); /* At the midpoint of the animation, increase the size */
  }
}


</style>

  