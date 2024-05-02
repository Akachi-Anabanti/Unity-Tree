<template>
  <VaCard :bordered="false">
    <VaIcon name="delete" size="large" @click="null" color="danger"/>
    <div class="card-avatar">
      <VaAvatar :src="person.img" size="large"/>
    </div>
    <VaCardTitle class="mb-4">{{ person.name }}</VaCardTitle>
    <VaCardContent>{{ person.address }}</VaCardContent>
  </VaCard>
</template>

<script setup>
 const person = defineProps({
  img: {type: String, required: true},
  name: {type: String, required:true},
  address: { type: String, required: true}
 })
</script>

<style scoped>
.va-card {
  width: 150px;
  height: auto;
  padding: 20px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.15);
  margin-bottom: 20px;
  position: relative;
}

.va-avatar {
  margin: 0.5rem;
  height: 100px;
  width: 100px;
  align-self: center;
  border: solid 1px blue;
}
.card-avatar{
  display: flex;
  justify-content: center;
  align-items: center;
} 
.va-card-actions {
  display: flex;
  justify-content: space-between;
}
.va-icon {
  position: absolute;
  right: 0;
  top: 0;
}
</style>