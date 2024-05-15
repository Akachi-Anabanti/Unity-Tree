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
           <img src="@/assets/connect_teams.svg" width="80%" height="80%" style="margin-top: 40px;"/>
           <div class="info-text">
            <h3>Create, Discover and Share Family Connections</h3>
           </div>
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
            <div style="height: auto;">
                <img src="@/assets/unity-name.png" alt="" height="100%" width="100%"/>
            </div>
            <div style="height: 70%; overflow-y:auto;">
                <RouterView />
            </div>
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
        border-right: dashed 0.5px grey;
        
    }
    @media (max-width: 500px){
        .auth-container-left{
            display: none;
            transition: ease-out;
        }
        .auth-container {
            grid-template-columns: 1fr;

        }
    }

    .auth-container-left .info-text{
        width: 70%;
        margin: auto;
    }
    .auth-container-left h3{
        text-align: center;
        font-size: x-large;
        font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
        align-self: center;
        }
</style>