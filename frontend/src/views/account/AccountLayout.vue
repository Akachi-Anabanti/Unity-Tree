<script setup>
 import {useAuthStore} from '@/stores/auth'
 import router  from '@/router'

 const authStore = useAuthStore()
 if (authStore.isAuthenticated) {
    router.push('/');
 }

</script>

<template>
    <div class="auth-container">
        <div class="auth-container-left">
            Contains other info graphics
        </div>
        <div class="auth-container-right">
            <RouterView />
        </div>
    </div>
</template>

<style scoped>
    .auth-container {
        display: grid;
        grid-template-columns: 1.9fr 1.1fr;
        gap: 0;
        position: relative;
        height: 100vh;
    }
    .auth-container-right{
        background-color: aqua;
        height: 50%;
       
    }
    .auth-container-left{
        background-color: brown;
    }
    @media (max-width: 600px){
        .auth-container {
            grid-template-columns: 1fr;
        }
    }
</style>