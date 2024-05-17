<script setup>
import { useFamilyStore } from '@/stores/family';

const useFamily = useFamilyStore();

</script>

<template>
  <div class="siblings-container">
      <div v-for="sibling in useFamily.getSiblingInfo" class="sibling-card">
        <div>
          <RouterLink :to="{ name: 'view', params: { _Id: sibling.id} }">
            <VaAvatar class="member-avatar"
              :src="sibling.img? sibling.img: 'https://randomuser.me/api/portraits/men/2.jpg'"
              size="large"
              />
          </RouterLink>
        </div>
        <p>{{ sibling.first_name }} {{ sibling.last_name }}</p>
      </div>
  </div>
</template>

<style scope>
.siblings-container {
  display: flex;
  justify-content: space-evenly;
}
</style>
