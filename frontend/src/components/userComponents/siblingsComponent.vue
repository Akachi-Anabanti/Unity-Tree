<script setup>
import { onMounted } from 'vue'
onMounted(async () => {})
</script>

<template>
  <VaCard square>
    <VaCardContent class="siblings-section">
      <VaAvatar class="member-avatar"></VaAvatar>
    </VaCardContent>
  </VaCard>
</template>

<style scope>
.siblings-section {
  display: flex;
  justify-content: space-evenly;
}
</style>
