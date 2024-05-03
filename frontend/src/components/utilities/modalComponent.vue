<script setup>
import { ref } from 'vue';
import AlertComponent from './AlertComponent.vue';

// Modal properties
defineProps({
    showAlertFailure: {type:Boolean},
    showAlertSuccess: {type: Boolean},
    showAlertWarning: {type: Boolean},
    alertMessage: {type:String}
})

// enables close
const isCloseableAlertVisible = ref(true)

// two way model link
const showModal = defineModel({required:true})

const handleClose = (hide) => {
    isCloseableAlertVisible.value = false
    hide()
}
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
       :before-close="handleClose"

   >
        <template #header>
            <AlertComponent
                :showAlertSuccess="showAlertSuccess"
                :showAlertFailure="showAlertFailure"
                :showAlertWarning="showAlertWarning"
                :alertMessage="alertMessage"
                v-model="isCloseableAlertVisible"
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