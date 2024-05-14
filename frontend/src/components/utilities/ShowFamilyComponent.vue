<script setup>

import {useUserStore} from '@/stores/user'
import { onBeforeMount} from 'vue';
import AddFamily from './createFamilyButton.vue';

const userStore = useUserStore()
let families
onBeforeMount(()=>{
    families = userStore.getFamily
})

</script>
<template>
    <div class="fam-cards">
        <div v-for="family in families" 
                :key="family.id" class="fam-card">
            <VaCard :bordered="false" stripe :to="{name:'tree', params:{familyId: family.id} }">
                <VaCardTitle>{{ family.name }}</VaCardTitle>
                <VaCardContent>
                    {{ family.created_at }}
                </VaCardContent>
            </VaCard>
        </div>
    </div>
    <AddFamily />
</template>


<style scoped>

.fam-cards{
    display: flex;
    flex-wrap: wrap;
}
.fam-card{
    margin: 5px;
    transition: transform 0.3s ease-in-out;
}
.fam-card:hover{
    transform: scale(1.05);
}
</style>