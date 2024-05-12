<script setup>

import {useUserStore} from '@/stores/user'
import { onBeforeMount, reactive} from 'vue';

const userStore = useUserStore()
let families = reactive([])

onBeforeMount(()=>{
    families = userStore.getFamily() 
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
</template>


<style scoped>

.fam-cards{
    display: flex;
    justify-content: space-around;
    align-items: center;
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