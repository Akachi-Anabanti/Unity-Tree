<script setup>

// Alert component properties
defineProps({
    showAlertSuccess:{type:Boolean},
    showAlertFailure:{type:Boolean},
    showAlertWarning : {type:Boolean},
    alertMessage: {type:String},
})
const isCloseableAlertVisible= defineModel()
</script>

<template>
    <!-- Success alert -->
    <VaAlert v-if="showAlertSuccess" color="primary"
        closeable
        v-model="isCloseableAlertVisible"
        
        >
        <template #icon>
            <VaIcon name="check" />
        </template>
        {{ alertMessage }}
    </VaAlert>

    <!-- Failure Alert -->
    <VaAlert v-if="showAlertFailure" color="danger"
        closeable
        close-icon
        v-model="isCloseableAlertVisible"
    >
        <template #icon>
            <VaIcon name="error" />
        </template>
    </VaAlert>

    <!-- Warning Alert -->
    <VaAlert v-if="showAlertWarning" color="warning"
        closeable
        close-icon
        v-model="isCloseableAlertVisible"
    >
        <template #icon>
            <VaIcon name="warning" />
        </template>
    </VaAlert>
</template>