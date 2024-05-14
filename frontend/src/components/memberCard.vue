<script setup>
import { useAuthStore } from '@/stores/auth';
import { useFamilyStore } from '@/stores/family';
import { useRouter } from 'vue-router';

const router = useRouter()

const authStore = useAuthStore()
const useFamily = useFamilyStore()

 const person = defineProps({
  id:{type:String},
  img:{},
  first_name: {type: String, required:true},
  last_name:{},
  date_of_birth: { required: true},
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

    router.push({ name: 'profile', params: { userId: person.id } })
  }



</script>



<template>
  <VaCard :bordered="false" @click="handleCardClick">
    <VaIcon name="delete" size="large" @click.stop="handleRemove" color="danger" v-if="authStore.getCurrentUserId === useFamily.getCreatorId"/>
    <div class="card-avatar">
      <VaAvatar :src="person.img ? person.img : 'https://randomuser.me/api/portraits/men/1.jpg'" size="large" @click.stop="handleProfileClick"/>
    </div>
    <VaCardTitle class="mb-4">{{ person.first_name }} {{ person.last_name }}</VaCardTitle>
    <VaCardContent>{{ person.date_of_birth }}</VaCardContent>
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