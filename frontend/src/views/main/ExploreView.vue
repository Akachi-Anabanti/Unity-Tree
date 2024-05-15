<template>
  <div>
    <va-input v-model="search" placeholder="Search..." clearable>
      <template #prepend>
        <va-icon name="search" />
      </template>
    </va-input>
    <va-card v-for="item in filteredData" :key="item.id">
      <va-card-title>{{ item.title }}</va-card-title>
      {{ item.content }}
    </va-card>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const search = ref('')
const data = ref([
  { id: 1, title: 'Item 1', content: 'Content 1' },
  { id: 2, title: 'Item 2', content: 'Content 2' }
  // Add more items as needed
])

const filteredData = computed(() => {
  if (!search.value) {
    return data.value
  } else {
    return data.value.filter((item) =>
      item.title.toLowerCase().includes(search.value.toLowerCase())
    )
  }
})
</script>
