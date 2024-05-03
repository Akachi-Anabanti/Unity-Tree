<script setup>
import { ref} from 'vue'
import MemberForm from './MemberForm.vue'
import TreeComponent from './utilities/TreeComponent.vue';
import modalComponent from './utilities/modalComponent.vue';
import AlertComponent from './utilities/AlertComponent.vue';

// Static data
const data = ref({
    "father": {
      "name": "C-3PO",
      "dateOfBirth": new Date(1877, 2, 14).toDateString(),
      "img": "https://randomuser.me/api/portraits/men/1.jpg",
      "role":"parent"
    },
    "mother": {
      "name": "Luke Skywalker",
      "dateOfBirth": new Date(1887, 1, 29).toDateString(),
      "img": "https://randomuser.me/api/portraits/women/5.jpg",
      "role": "parent"
    },
    "children": [
      {
        "name": "Obi-Wan Kenobi",
        "dateOfBirth": new Date(1987, 1, 29).toDateString(),
        "img": "https://randomuser.me/api/portraits/men/2.jpg",
        "role": "child"
      },
      {
        "name": "Jabba Desilijic Tiure",
        "dateOfBirth": new Date(1787, 1, 29).toDateString(),
        "img": "https://randomuser.me/api/portraits/women/4.jpg",
        "role": "child"
      },
      {
        "name": "Yoda",
        "dateOfBirth": new Date(1987, 1, 29).toDateString(),
        "img": "https://randomuser.me/api/portraits/men/5.jpg",
        "role": "child"
      },
      {
        "name": "Darth Vader",
        "dateOfBirth": new Date(1897, 1, 29).toDateString(),
        "img": "https://randomuser.me/api/portraits/men/6.jpg",
        "role": "child"
      },
      {
        "name": "Obi-Wan Kenobi",
        "dateOfBirth": new Date(1887, 1, 29).toDateString(),
        "img": "https://randomuser.me/api/portraits/men/2.jpg",
        "role": "child"
      },
    ]
  });

// Main Alert Modifiers
const showModal = ref(false);
const showAlertSuccess = ref(false)
const showAlertFailure= ref(false)
const showAlertWarning = ref(false)

// Modal Alert Modifiers
const showAlertSuccessModal= ref(false)
const showAlertFailureModal= ref(false)
const showAlertWarningModal = ref(false)

const alertMessage = ref("")
const isCloseableAlertVisible = ref(true)


// Function to handle Modal Form Submit
const handleFormSubmit = (newMember) => {

    if (newMember.dateOfBirth){
          newMember.dateOfBirth = newMember.dateOfBirth.toDateString()
      }

    if (newMember.role === 'child'){
    try {
        data.value.children.push(newMember);
        alertMessage.value = "Child added Successfully!"
        showAlertSuccessModal.value = true
    
    } catch (error) {
        alertMessage.value = "Failed to Add member!"
        showAlertFailureModal.value = true
    }
  }
}


</script>

<template>
    <!-- Alert component -->
    <div class="main-alert">
        <AlertComponent
            :alert-message="alertMessage"
            :show-alert-success="showAlertSuccess"
            :show-alert-warning="showAlertWarning"
            :show-alert-failure="showAlertFailure"
            v-model="isCloseableAlertVisible"
        />
    </div>

    <!-- Modal Component -->
    <modalComponent v-model="showModal" 
        :alert-message="alertMessage"
        :show-alert-failure="showAlertFailureModal"
        :show-alert-success="showAlertSuccessModal"
        :show-alert-warning="showAlertWarningModal"
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
    <div>
        <TreeComponent v-model="data"/>
    </div>
</template>

<style scoped>
.add-member{
    position: fixed;
    right: 70px;
    bottom: 50px;
    z-index: 1;
}

.va-modal{
    opacity: 0;
}

</style>

  