<script setup>
import { ref } from 'vue'
import MemberForm from './MemberForm.vue'

const showModal = ref(false);

</script>
<template>

    <!-- <VaCarousel
    :items="items"
    stateful
    infinite
    swipable
    :indicators="false"
    height= "25px"
    /> -->
    <VaModal 
        v-model="showModal"
        ok-text="Done"
        size="auto"
        close-button
        max-height="500px"
        max-width=" 500px"
        disable-attachment
        allow-body-scroll
        no-outside-dismiss
        overlay-opacity=70
        stateful
    >
    <h3 class="va-h3" style="text-align: center;">
        Add member
    </h3>
    <MemberForm />
    </VaModal>
    <div class="flex items-center gap-8 flex-wrap add-member">
        <VaButton round icon="va-plus" size="large" @click="showModal = true"/>
    </div>

</template>

<style scoped>
.add-member{
    position: fixed;
    right: 70px;
    bottom: 50px;
}
</style>

  