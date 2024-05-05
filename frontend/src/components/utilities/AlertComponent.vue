<script setup>

    import { ref } from 'vue';

// Alert component properties
    defineProps({
        showAlertSuccess:{type:Boolean},
        showAlertFailure:{type:Boolean},
        showAlertWarning : {type:Boolean},
        alertMessage: {type:String},
    })
    const isCloseableAlertVisible= ref(true)
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
        v-model="isCloseableAlertVisible"
    >
        <template #icon>
            <VaIcon name="error" />
        </template>
        {{ alertMessage }}
    </VaAlert>

    <!-- Warning Alert -->
    <VaAlert v-if="showAlertWarning" color="warning"
        closeable
        v-model="isCloseableAlertVisible"
    >
        <template #icon>
            <VaIcon name="warning" />
        </template>
        {{ alertMessage }}
    </VaAlert>
</template>