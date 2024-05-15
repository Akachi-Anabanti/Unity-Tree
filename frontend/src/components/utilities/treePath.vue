<template>
  <div>
    <div v-for="(child, index) in node.children" :key="index">
      <button @click="navigateTo(child)">
        {{ child.name }}
      </button>
      <FamilyNode v-if="child.children" :node="child" />
    </div>
    <div>Current Path: {{ currentPath.join(' > ') }}</div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

let props = defineProps({
  node: Object
})

let node = ref(props.node)
let currentPath = ref([])

const navigateTo = (node) => {
  currentPath.value.push(node.name)
  node.value = node
}
</script>
