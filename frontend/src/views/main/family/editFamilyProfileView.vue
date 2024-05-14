<template>
    <div>
        Edit Family Page
        {{ props.familyId }}
    </div>
</template>

<script setup>
const props = defineProps({familyId:{type: String}})
</script>