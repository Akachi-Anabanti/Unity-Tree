<script setup>
defineProps({
  ImageUrl: {
    type: String,
    default: null
  },
  Age: Number,
  name: {
    type: String,
    required: true
  }
})
</script>
<template>
  <div class="person-card">
    <img :alt="name" :src="ImageUrl" class="image" />
    <h2 class="card-title">CARD INFORMATION</h2>
    <a href="#">Show Tree</a>
    <a href="#">Go to Profile page</a>
  </div>
</template>

<style scoped>
.person-card {
  height: 200px;
  width: 200px;
}

.card-title {
  text-wrap: balance;
  font: 300;
}
.image {
  height: 100px;
  width: 100px;
  border-radius: 50%;
  border-color: green;
}

.a {
  text-decoration: none;
}
</style>
