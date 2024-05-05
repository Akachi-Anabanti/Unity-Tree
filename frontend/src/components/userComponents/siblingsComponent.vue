
<script setup>
    import {onMounted} from 'vue';
    import { useUserStore } from '@/stores/user';
    const userStore = useUserStore()

    onMounted(async() => {
        const {status, success} = await userStore.dispatchGetUsers();

        if (!success){
            alert('Something went wrong')
            console.log("API status -> ", status)

        }

    })

    const gotoNextPage = async () =>{
        const params = {page: userStore.currentPage + 1}
        const {status, success} = await userStore.dispatchGetUsers(params);
        if (!success){
            alert('Something went wrong')
            console.log("API status -> ", status)
        }
    }

    const gotoPreviousPage = async () =>{
        let page = userStore.currentPage
        page--
        const {status, success} = await userStore.dispatchGetUsers({page: page})
        if (!success){
            alert("Something went wrong")
            console.log('API status ->', status)
        }
    }

</script>

<template>

    <VaCard square>
        <VaCardContent class="siblings-section">
            <VaAvatar class="member-avatar" v-for="(user) in userStore.users.value" :key="user.id" :src="user.avatar" size="medium"/>
        </VaCardContent>
            <!-- {{ user }} -->
        <VaCardActions align="between">
            <VaButton @click="gotoPreviousPage" :disabled="!userStore.prevButton">&lt;&lt;</VaButton>
            <VaButton @click="gotoNextPage" :disabled="!userStore.nextButton">&gt;&gt;</VaButton>
        </VaCardActions>
    </VaCard>

</template>

<style scope>
    .siblings-section {
        display: flex;
        justify-content: space-evenly;
    }
</style>