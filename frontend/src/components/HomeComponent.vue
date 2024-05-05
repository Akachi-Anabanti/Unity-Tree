<script setup>
import { ref } from 'vue'
import MemberForm from './MemberForm.vue'
import TreeComponent from './utilities/TreeComponent.vue';
import modalComponent from './utilities/modalComponent.vue';
import AlertComponent from './utilities/AlertComponent.vue';
import { useAlertStore } from '@/stores/alert';
import { useFamilyStore } from '@/stores/family';

const useAlert = useAlertStore()
const useFamily = useFamilyStore()


  const showModal = ref(false);


// Function to handle Modal Form Submit
const handleFormSubmit = (newMember) => {

    if (newMember.dateOfBirth){
          newMember.dateOfBirth = newMember.dateOfBirth.toDateString()
      }

    if (newMember.role === 'child'){
    try {
        useFamily.familyData.children.push(newMember);
        const message = "Child added Successfully!"
        useAlert.dispatchShowModalAlertSuccess(message)
    
    } catch (error) {
        const message = "Failed to Add member!"
        useAlert.dispatchShowModalAlertFailure(message)
    }
  }
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
            v-model="useAlert.isCloseableAlertVisible"
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
    <div class="flex items-center gap-8 flex-wrap add-member">
        <VaButton round icon="va-plus" size="large" @click="showModal = true"/>
    </div>

    <!-- The family tree component -->
    <div v-if="useFamily.hasFamily">
        <TreeComponent />
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

  