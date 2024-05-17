<script setup>
import { onMounted, watch, ref } from 'vue'
import marqueeComponent from './marqueeComponent.vue'
import siblingsComponent from './siblingsComponent.vue'
import { useFamilyStore } from '@/stores/family'
import SpinnerComp from '../utilities/spinnerComp.vue'
import { storeToRefs } from 'pinia'

const isLoading = ref(true)

const props = defineProps({
  _Id: { type: String }
})

const useFamily = useFamilyStore()

onMounted(async () => {
  await useFamily.dispatchGetFamilyMember(props._Id)
  await useFamily.dispatchGetSiblings(props._Id)
  isLoading.value = false
})

watch(
  () => props._Id,
  async (newVal, oldVal) => {
    if (newVal !== oldVal) {
      await useFamily.dispatchGetFamilyMember(newVal)
      await useFamily.dispatchGetSiblings(newVal)
    }
  }
)

const userInfo = storeToRefs(useFamily.memberInfo)

// user avatar configuration
const avatarSizeConfig = {
  sizes: {
    large: 150
  }
}

// static user info

function calculateAge(dateOfBirth) {
  let today = new Date()
  let birthDate = new Date(dateOfBirth)
  let age = today.getFullYear() - birthDate.getFullYear()
  let monthDifference = today.getMonth() - birthDate.getMonth()

  // Adjust age if birth date has not occurred yet this year
  if (monthDifference < 0 || (monthDifference === 0 && today.getDate() < birthDate.getDate())) {
    age--
  }

  return age
}
</script>
<template>
  <div v-if="isLoading">
    <SpinnerComp />
  </div>

  <div v-else>
    <div class="header-section">
      <VaAvatar
        size="large"
        :sizes-config="avatarSizeConfig"
        :src="
          useFamily.memberInfo.img
            ? useFamily.memberInfo.img
            : 'https://randomuser.me/api/portraits/women/4.jpg'
        "
      />

      <div class="right-header">
        <h2 v-if="useFamily.memberInfo.first_name">
          {{ useFamily.memberInfo.first_name }} {{ useFamily.memberInfo.last_name }}
        </h2>
        <h2 v-else>No name</h2>
        <p>Born: {{ useFamily.memberInfo.date_of_birth }}</p>
        <p>Age: {{ calculateAge(useFamily.memberInfo.date_of_birth) }}</p>
      </div>
    </div>

    <div class="gallery-section">
      <h3>Memories</h3>
      <marqueeComponent />
    </div>
    <div class="siblings">
      <h3>Siblings</h3>
      <siblingsComponent :member-id="props._Id" />
    </div>
    <div class="info-section">
      <p>nickname: {{ useFamily.memberInfo.nickname }}</p>
      <p>ethnicity: {{ useFamily.memberInfo.ethnicity }}</p>
      <p>gender: {{ useFamily.memberInfo.gender }}</p>
      <p>genotype: {{ useFamily.memberInfo.genotype }}</p>
      <p>height: {{ useFamily.memberInfo.height }}</p>
      <p>hobbies: {{ useFamily.memberInfo.hobbies }}</p>
      <p>nationality: {{ useFamily.memberInfo.nationality }}</p>
      <p>occupation: {{ useFamily.memberInfo.occupation }}</p>
      <p>ethnicity: {{ useFamily.memberInfo.ethnicity }}</p>
      <p>Skin Color: {{ useFamily.memberInfo.skin_color }}</p>
      <p>State of Origin: {{ useFamily.memberInfo.state_of_origin }}</p>
      <p>Race: {{ useFamily.memberInfo.race }}</p>
      <p>Marital Status: {{ useFamily.memberInfo.marital_status }}</p>
    </div>
  </div>
</template>

<style scoped lang="scss">
//header section styles
.header-section {
  display: grid;
  grid-template-columns: 1fr 2fr;
  column-gap: 20px;
  justify-items: center;
  align-items: center;
  margin: auto;
  width: 50%;
  height: auto;
  padding-bottom: 50px;
  border-bottom: solid 1px black;

  .right-header {
    width: 100%;
    p {
      padding: 0;
      margin: 0;
    }
  }

  .glow {
    -webkit-animation: glow 1s ease-in-out infinite alternate;
    -moz-animation: glow 1s ease-in-out infinite alternate;
    animation: glow 1s ease-in-out infinite alternate;
  }
  @keyframes glow {
    from {
      box-shadow:
        0 0 10px #00ff00,
        0 0 20px #00ff00,
        0 0 30px #00ff00,
        0 0 40px #00ff00;
    }
    to {
      box-shadow:
        0 0 20px #00ff00,
        0 0 30px #ff00de,
        0 0 40px #ff00de,
        0 0 50px #ff00de,
        0 0 60px #ff00de;
    }
  }
}

.gallery-section {
  margin: auto;
  width: 75%;
  padding-bottom: 20px;
  border-bottom: solid 1px black;
}

.siblings {
  margin: auto;
  width: 75%;
}

.description-section {
  background-color: red;
}

.autobiography-section {
  background-color: chartreuse;
}

@media (max-width: 600px) {
  .header-section {
    grid-template-columns: 1fr;
    align-items: center;
    row-gap: 10px;
  }
}
</style>
