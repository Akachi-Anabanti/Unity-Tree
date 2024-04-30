<script setup>
import { ref } from 'vue'
import PersonCard from './UserComponents/PersonCard.vue'

const props = defineProps({
  InitialCount: Number
})

const message = ref('Welcome to Body')
let count = ref(0)
count.value = props.InitialCount
</script>

<template>
  <div class="">
    <h3>{{ message }}</h3>
    <button @click="count++">Count {{ count }}</button>
    <h4>{{ InitialCount }}</h4>
  </div>
  <PersonCard />
</template>
