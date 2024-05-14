<template>
    <div>
         Family Profile Page
        {{ props.familyId }}
    </div>
</template>

<script setup>
const props = defineProps({familyId:{type: String}})
</script>