<script setup>
 import {useAuthStore} from '@/stores/auth'
 import router  from '@/router'
 import AlertComponent from '@/components/AlertComponent.vue';
import { useAlertStore } from '@/stores/alert';

 const authStore = useAuthStore()
const alertStore = useAlertStore()

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
            <div class="main-alert">
                <AlertComponent
                    :alert-message="alertStore.alertMessage"
                    :show-alert-success="alertStore.showMainAlertSuccess"
                    :show-alert-warning="alertStore.showMainAlertWarning"
                    :show-alert-failure="alertStore.showMainAlertFailure"
                />
            </div>
            <RouterView />
        </div>
    </div>
</template>

<style scoped>
    .auth-container {
        display: grid;
        grid-template-columns: 3fr 2.5fr;
        gap: 0;
        position: relative;
        height: 100vh;
    }
    .auth-container-right{
        padding: 1rem;
        position: relative;
    }
    .auth-container-left{
        background-attachment: fixed;
        background-color: rgb(123, 123, 245);
        
    }
    @media (max-width: 600px){
        .auth-container {
            grid-template-columns: 1fr;
        }
    }
</style>