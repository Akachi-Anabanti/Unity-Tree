<script setup>
  import { onBeforeMount, ref } from 'vue'
  import { useUserStore } from '@/stores/user';

  import AddFamily from "@/components/utilities/createFamilyButton.vue"
  import ShowFamily from "@/components/utilities/ShowFamilyComponent.vue"


  const isLoading = ref(true)
  const userStore = useUserStore();
  const showModal = ref(true)
  showModal.value = true;
    

  onBeforeMount(async()=>{
    await userStore.dispatchGetFamiliesCreated()
    isLoading.value = false
  })


</script>

<template>

    <!-- Modal Component -->


    <!-- The family tree component -->
    <div v-if="isLoading">
      Loading...
    </div>
    <div v-else>
      <div v-if="userStore.numberOfFamiliesCreated > 0">
        <ShowFamily />
      </div>
      <div v-else>
        <!-- Display a modal here -->
        <AddFamily />
      </div>
    </div>
</template>

<style scoped>


.main-alert{
  position: fixed;
  z-index: 1;
  left: 35%;
  right: 35%;
  width: 30%;
  top: 90%;
  align-items: center;
  animation: swell 2s  infinite ease-in-out;
}
@keyframes swell {
  0%, 100% {
    transform: scale(1); /* Start and end at normal size */
  }

  50% {
    transform: scale(1.1); /* At the midpoint of the animation, increase the size */
  }
}


</style>

  