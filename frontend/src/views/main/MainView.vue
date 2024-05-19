<script setup>
import { onBeforeMount, ref } from 'vue'
import { useAuthStore } from '@/stores/auth'
import { useAlertStore } from '@/stores/alert'
import AlertComponent from '@/components/AlertComponent.vue'
import { useUserStore } from '@/stores/user'

const showSidebar = ref(false)
const page = ref('home')
const authStore = useAuthStore()
const userStore = useUserStore()
const useAlert = useAlertStore()

const logout = async () => {
  authStore.dispatchLogout()
}

onBeforeMount(async () => {
  // check if user has a family
  //  this sets the currentUserHasFamily value to either true or false
  // and it is used to display the tree sidebar item
  await userStore.dispatchGetUserFamily()
})
</script>

<template>
  <VaLayout style="height: 500px" :left="{ fixed: true }" :top="{ fixed: true }">
    <!-- Top navbar -->
    <template #top>
      <VaNavbar color="primary" class="py-2">
        <template #left>
          <VaButton
            :icon="showSidebar ? 'menu_open' : 'menu'"
            @click="showSidebar = !showSidebar"
          />
        </template>
        <template #right>
          <RouterLink
            :to="{
              name: 'view',
              params: { _Id: authStore.getCurrentUserId }
            }"
            v-if="authStore.isAuthenticated"
          >
            <div style="margin-right: 3rem">
              <VaAvatar
                src="https://randomuser.me/api/portraits/women/5.jpg"
                @click="page = 'profile'"
              />
            </div>
          </RouterLink>
        </template>

        <!-- Center of top navbar: Brand content -->
        <template #center>
          <VaNavbarItem class="font-bold text-lg"> Unity Tree </VaNavbarItem>
        </template>
      </VaNavbar>
    </template>
    <!-- Left sidebar of layout -->
    <template #left>
      <VaSidebar v-model="showSidebar" class="py-2">
        <VaSidebarItem :active="page === 'home'" @click="page = 'home'">
          <RouterLink to="/">
            <VaSidebarItemContent>
              <VaIcon name="home" />
              <VaSidebarItemTitle> Home </VaSidebarItemTitle>
            </VaSidebarItemContent>
          </RouterLink>
        </VaSidebarItem>
        <VaSidebarItem :active="page === 'profile'" @click="page = 'profile'">
          <RouterLink
            :to="{
              name: 'view',
              params: { _Id: authStore.getCurrentUserId }
            }"
            v-if="authStore.isAuthenticated"
          >
            <VaSidebarItemContent>
              <VaIcon name="person" />
              <VaSidebarItemTitle> Profile </VaSidebarItemTitle>
            </VaSidebarItemContent>
          </RouterLink>
        </VaSidebarItem>
        <VaSidebarItem
          :active="page === 'tree'"
          @click="page = 'tree'"
          v-if="userStore.currentUserHasFamily"
        >
          <RouterLink
            :to="{
              name: 'tree',
              params: { familyId: userStore.getUserFamilyId }
            }"
          >
            <VaSidebarItemContent>
              <VaIcon name="account_tree" />
              <VaSidebarItemTitle> My tree </VaSidebarItemTitle>
            </VaSidebarItemContent>
          </RouterLink>
        </VaSidebarItem>
        <VaSidebarItem :active="page === 'about'" @click="page = 'about'">
          <RouterLink to="/about">
            <VaSidebarItemContent>
              <VaIcon name="info" />
              <VaSidebarItemTitle> About </VaSidebarItemTitle>
            </VaSidebarItemContent>
          </RouterLink>
        </VaSidebarItem>

        <VaSidebarItem :active="page === 'settings'" @click="page = 'setting'">
          <VaSidebarItemContent>
            <VaIcon name="settings" />
            <VaSidebarItemTitle> Settings </VaSidebarItemTitle>
          </VaSidebarItemContent>
        </VaSidebarItem>

        <VaSidebarItem :active="page === 'explore'" @click="page = 'explore'">
          <RouterLink to="/discover" >
            <VaSidebarItemContent>
              <VaIcon name="explore" />
              <VaSidebarItemTitle> Discover </VaSidebarItemTitle>
            </VaSidebarItemContent>
          </RouterLink>
        </VaSidebarItem>

        <VaSidebarItem @click="logout" style="bottom: 0">
          <VaSidebarItemContent>
            <VaIcon name="logout" />
            <VaSidebarItemTitle> Logout </VaSidebarItemTitle>
          </VaSidebarItemContent>
        </VaSidebarItem>
      </VaSidebar>
    </template>

    <template #content>
      <main class="main">
        <div class="main-alert">
          <AlertComponent
            :alert-message="useAlert.alertMessage"
            :show-alert-success="useAlert.showMainAlertSuccess"
            :show-alert-warning="useAlert.showMainAlertWarning"
            :show-alert-failure="useAlert.showMainAlertFailure"
          />
        </div>

        <RouterView />
      </main>
    </template>
  </VaLayout>
</template>

<style scoped>
.main {
  min-height: 100vh;
  /* display: flex; */
  /* flex-direction: column; */
  align-items: center;
  justify-content: center;
  padding: 2rem;
}
.main-alert {
  position: fixed;
  z-index: 1;
  left: 35%;
  right: 35%;
  width: 30%;
  top: 90%;
  align-items: center;
  /* animation: swell 2s  infinite ease-in-out; */
}
@keyframes swell {
  0%,
  100% {
    transform: scale(1); /* Start and end at normal size */
  }

  50% {
    transform: scale(1.1); /* At the midpoint of the animation, increase the size */
  }
}
</style>
