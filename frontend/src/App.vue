<script setup lang="ts">
  import { ref } from 'vue'

  const showSidebar = ref(false)
  const page = ref('home')
 
</script>

<template>
  <VaLayout style="height: 500px;"
  :left="{fixed: true }"
  :top="{ fixed: true }">
    <template #top>
      <VaNavbar
        color="primary"
        class="py-2"
      >
        <template #left>
          <VaButton
            :icon="showSidebar ? 'menu_open' : 'menu'"
            @click="showSidebar = !showSidebar"
          />
        </template>
        <template #right>

          <RouterLink to="/profile">
            <div style="margin-right: 3rem;">
              <VaAvatar
            src="https://randomuser.me/api/portraits/women/5.jpg"
            @click="page='profile'"
            
          />
            </div>
     
        </RouterLink>

        </template>
        <template #center>
          <VaNavbarItem class="font-bold text-lg">
            LOGO
          </VaNavbarItem>
        </template>

      </VaNavbar>
    </template>

    <template #left>
      <VaSidebar v-model="showSidebar" class="py-2">
        <VaSidebarItem :active="page === 'home'" @click="page = 'home'">
          <RouterLink to="/">
            <VaSidebarItemContent>
            <VaIcon name="home" /> 
            <VaSidebarItemTitle>
              Home
            </VaSidebarItemTitle>
          </VaSidebarItemContent>
          </RouterLink>
        </VaSidebarItem>
        <VaSidebarItem :active="page === 'profile'" @click="page = 'profile'">
            <RouterLink to="/profile">
                <VaSidebarItemContent>
                    <VaIcon name="person" />
                    <VaSidebarItemTitle>
                        Profile
                    </VaSidebarItemTitle>
                </VaSidebarItemContent>
            </RouterLink>
        </VaSidebarItem>
        <VaSidebarItem :active="page === 'about'" @click="page = 'about'">
            <RouterLink to="/about">
                <VaSidebarItemContent>
                    <VaIcon name="info" />
                    <VaSidebarItemTitle>
                        About
                    </VaSidebarItemTitle>
                </VaSidebarItemContent>
            </RouterLink>
        </VaSidebarItem>
        
        <VaSidebarItem :active="page === 'settings'" @click="page = 'setting'">
            <VaSidebarItemContent>
              <VaIcon name="settings" />
                <VaSidebarItemTitle>
                      Settings
                  </VaSidebarItemTitle>
              </VaSidebarItemContent>
        </VaSidebarItem>

        <VaSidebarItem :active="page === 'explore'" @click="page = 'explore'">
            <VaSidebarItemContent>
              <VaIcon name="explore" />
                <VaSidebarItemTitle>
                    Discover
                  </VaSidebarItemTitle>
                </VaSidebarItemContent>
        </VaSidebarItem>

    </VaSidebar>
    </template>

    <template #content>
      <main class="main">
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
</style>