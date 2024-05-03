<script setup>
  import { nextTick, onMounted, ref, watch} from 'vue';
  import { VueDraggableNext as draggable } from 'vue-draggable-next';
  import memberCard from './memberCard.vue';

  
  const container = ref(null);
  onMounted(() => {
    adjustHeight();
  });

  const family = defineModel({required:true})

// Handles Child member removal
  const deleteChildMember = (index) => {
    family.value.children.splice(index, 1)    
  }

// handles parent Member removal
const deleteParentMember = (role) => {
  delete family.value[role];
}

  // Watches for changes in the length of the children value
  watch(
    () => family.value.children.length,
    () => nextTick(() => {
        adjustHeight()
    })
  )

  // Adjusts the height of the children stem line
  // based on the number of children
  async function adjustHeight() {
    const cards = container.value.querySelectorAll('.children-card');
    const lastCard = cards[cards.length -1];
    const rectContainer = container.value.getBoundingClientRect();
    const rectLastCard = lastCard.getBoundingClientRect();
    const height = rectContainer.height - (rectLastCard.height / 2);
    container.value.style.setProperty('--dynamic-height', `${height}px`);
  }
</script>


<template>
    <div class="tree-container">
        <div class="parent-card-container" >
            <div v-for="(person, role) in family" :key="role" class="parent-card"
                :class="{'father': role === 'father', 'mother': role === 'mother'}">
                <memberCard v-if="role != 'children'" v-bind="person" @removeMember="deleteParentMember(role)"/>
            </div>
        </div>
        <div class="children-container" ref="container">
            <draggable v-model="family.children" class="dragArea"
            group="description"
              >
                <TransitionGroup type="transition" name="flip-list">
                    <div v-for="(person, index) in family.children" :key="index" class="children-card"
                        :class="{'left':index % 2 === 0, 'right':index % 2 === 1} ">
                        <memberCard  v-bind="person" @removeMember="deleteChildMember(index)"/>
                    </div>
                </TransitionGroup>
            </draggable>
        </div>
    </div>
</template>

<style scoped>

.flip-list-move {
  transition: transform 0.5s;
}
.no-move {
  transition: transform 0s;
}

.ghost {
  opacity: 0.5;
  background: #c8ebfb;
}

.tree-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 90%;
  height: 90%;
  margin: auto;
}

.parent-card-container::after {
  content: "";
  position: absolute;
  top: 50%;
  bottom: 0;
  left: 50%;
  border-left: 1px solid black;
}


.parent-card-container::before,
.parent-card-container::after {
  content: "";
  /* flex: 1; */
}

.parent-card-container {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  position: relative;
  width: 100%;
}

.parent-card {
  margin: 10px;
  position: relative;
}

.parent-card.father {
  margin-right: 5rem;
}

.parent-card.mother {
  margin-left: 5rem;
}

.parent-card.father::after {
  content: "";
  position: absolute;
  top: 50%;
  right: -10.4rem;
  width: 10.4rem;
  border-top: 1px solid black;
}

.parent-card.mother::before {
  content: "";
  position: absolute;
  top: 50%;
  left: -10.4rem;
  width: 10.4rem;
  border-top: 1px solid black;
}


.children-container{
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  position: relative;
  /* width: inherit; */
}

.children-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 0.5em;
  width: auto;
  position: relative;
}

.children-card.left {
  align-self: flex-start;
  right: 10rem;
}

.children-card.right {
  align-self: flex-end;
  left: 10rem;
}

.children-container::before {
  content: "";
  position: absolute;
  top: 0;
  bottom: calc(100% - var(--dynamic-height));
  left: 50%;
  border-left: 1px solid black;
}

.children-card.right::before {
  content: "";
  position: absolute;
  top: 50%;
  left: -4rem;
  width: 4rem;
  border-top: 1px solid black;
}
.children-card.left::after {
    content: "";
    position: absolute;
    top: 50%;
    right: -4.1rem;
    width: 4.1rem;
    border-top: 1px solid black;
}
</style>