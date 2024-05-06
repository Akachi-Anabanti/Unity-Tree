<script setup>
import AlertComponent from './AlertComponent.vue';
import { useAlertStore } from '@/stores/alert';

const useAlert = useAlertStore()



// two way model link
const showModal = defineModel({required:true})

</script>

<template>
    <VaModal 
       v-model="showModal"
       size="auto"
       ok-text="Done"
       close-button
       max-height="500px"
       max-width=" 500px"
       allow-body-scroll
       no-dismiss
       show-nested-overlay

   >
        <template #header>
            <AlertComponent 
                :showAlertSuccess="useAlert.showModalAlertSuccess"
                :showAlertFailure="useAlert.showModalAlertFailure"
                :showAlertWarning="useAlert.showModalAlertWarning"
                :alertMessage="useAlert.alertMessage"
            />
        </template>

        <template #default>
            <h3 class="va-h3" style="text-align: center;">
                Add member
             </h3>
            <slot name="form"></slot>
        </template>
   </VaModal>
</template>