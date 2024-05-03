<template>
  <VaCard :bordered="false">
    <VaIcon name="delete" size="large" @click="handleRemove" color="danger"/>
    <div class="card-avatar">
      <VaAvatar :src="person.img" size="large"/>
    </div>
    <VaCardTitle class="mb-4">{{ person.name }}</VaCardTitle>
    <VaCardContent>{{ person.dateOfBirth }}</VaCardContent>
  </VaCard>
</template>

<script setup>
 const person = defineProps({
  img: {type: String, required: true},
  name: {type: String, required:true},
  dateOfBirth: { type: String, required: true},
  role:{type: String, required:true}
  
 })

//  function formatDate(date) {
//   const options = { year: 'numeric', month: 'long', day: 'numeric' };
//   let formattedDate = date.toLocaleDateString('en-GB', options);
  
//   // Add the ordinal suffix
//   let day = date.getDate();
//   if (day % 10 == 1 && day != 11) {
//     formattedDate = formattedDate.replace(day, day + 'st');
//   } else if (day % 10 == 2 && day != 12) {
//     formattedDate = formattedDate.replace(day, day + 'nd');
//   } else if (day % 10 == 3 && day != 13) {
//     formattedDate = formattedDate.replace(day, day + 'rd');
//   } else {
//     formattedDate = formattedDate.replace(day, day + 'th');
//   }
  
//   return formattedDate;
// }

  const emit = defineEmits(['removeMember'])
  const handleRemove = () => {
    emit('removeMember')
  }
</script>

<style scoped>
.va-card {
  width: 150px;
  height: 200px;
  padding: 20px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.15);
  margin-bottom: 20px;
  position: relative;
}
.va-card__content{
  padding: 0;
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