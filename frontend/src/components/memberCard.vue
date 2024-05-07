<script setup>
import { useRouter } from 'vue-router';

const router = useRouter()

 const person = defineProps({
  id:{type:String},
  img: {type: String, required: true},
  name: {type: String, required:true},
  dateOfBirth: { type: String, required: true},
  role:{type: String, required:true}
  
 })

  const emit = defineEmits(['removeMember', 'cardClick'])
  const handleRemove = () => {
    emit('removeMember')
  }
  const handleCardClick = () => {
    emit('cardClick', person.id)
  }

  const handleProfileClick = () =>{

    router.push({ name: 'Profile', params: { id: person.id } })
  }



</script>



<template>
  <VaCard :bordered="false" @click="handleCardClick">
    <VaIcon name="delete" size="large" @click.stop="handleRemove" color="danger"/>
    <div class="card-avatar">
      <VaAvatar :src="person.img" size="large" @click.stop="handleProfileClick"/>
    </div>
    <VaCardTitle class="mb-4">{{ person.name }}</VaCardTitle>
    <VaCardContent>{{ person.dateOfBirth }}</VaCardContent>
  </VaCard>
</template>

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