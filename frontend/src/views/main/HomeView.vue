<script setup>
  import { onMounted, ref } from 'vue'
  import { useUserStore } from '@/stores/user';

  import AddFamily from "@/components/utilities/createFamilyButton.vue"
  import ShowFamily from "@/components/utilities/ShowFamilyComponent.vue"
  import Spinner from "@/components/utilities/spinnerComp.vue"
// import { storeToRefs } from 'pinia';


  const isLoading = ref(true)
  
  onMounted(async()=>{
    await userStore.dispatchGetFamiliesCreated()
    isLoading.value = false
  })

  const userStore = useUserStore();
</script>

<template>

    <div v-if="isLoading">
      <Spinner />
    </div>
    <div v-else-if="!userStore.isNumberFamiliesCreatedZero">
    <!-- The family tree component -->
        <ShowFamily />
    </div>
    <div v-else>
        <AddFamily v-bind="showPopover"/>
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

  