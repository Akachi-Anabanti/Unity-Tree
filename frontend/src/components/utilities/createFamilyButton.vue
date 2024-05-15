<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

function addFam() {
  router.push({ name: 'create-family' })
}
</script>

<template>
  <div class="add-card">
    <h2>Add New Family</h2>
    <VaButton class="add-button" @click="addFam">+</VaButton>
  </div>
</template>

<style scoped>
.add-card {
  width: 200px;
  height: 200px;
  border: 1px solid var(--va-background-border);
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: var(--va-background-secondary);
  color: var(--va-text-primary);
}
.add-card:hover {
  box-shadow: 0 0 10px var(--va-shadow);
}
.add-button {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  border: none;
  background-color: var(--va-primary);
  color: var(--va-on-primary);
  font-size: 30px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}
</style>
