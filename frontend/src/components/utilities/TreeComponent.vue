<template>
    <div class="tree-container">
        <div class="parent-card-container" >
            <div v-for="(person, role) in family" :key="role" class="parent-card">
                <memberCard v-if="role != 'children'" v-bind="person"/>
            </div>
        </div>
        <draggable v-model="family.children" class="dragArea">
                <TransitionGroup type="transition" name="list">
                    <div v-for="(person, index) in family.children" :key="index" class="children-card">
                        <memberCard  v-bind="person"/>
                    </div>
                </TransitionGroup>
        </draggable>
    </div>
</template>

<script setup>
  import { ref } from 'vue';
  import { VueDraggableNext as draggable } from 'vue-draggable-next';
  import memberCard from './memberCard.vue';

  const family = ref({
    "father": {
      "name": "C-3PO",
      "address": "626 Carroll Street, Roulette, Ohio, 1477",
      "img": "https://randomuser.me/api/portraits/men/1.jpg"
    },
    "mother": {
      "name": "Luke Skywalker",
      "address": "644 Vermont Court, Freelandville, Kentucky, 2619",
      "img": "https://randomuser.me/api/portraits/women/5.jpg"
    },
    "children": [
      {
        "name": "Obi-Wan Kenobi",
        "address": "887 Winthrop Street, Tryon, Florida, 3912",
        "img": "https://randomuser.me/api/portraits/men/2.jpg"
      },
      {
        "name": "Jabba Desilijic Tiure",
        "address": "286 NW. Shore St.Longwood, FL 32777",
        "img": "https://randomuser.me/api/portraits/women/4.jpg"
      },
      {
        "name": "Yoda",
        "address": "353 NW. Shore St.Longwood, FL 32778",
        "img": "https://randomuser.me/api/portraits/men/5.jpg"
      },
      {
        "name": "Darth Vader",
        "address": "265 NW. Shore St.Longwood, FL 32779",
        "img": "https://randomuser.me/api/portraits/men/6.jpg"
      }
    ]
  });
</script>


<style scoped>
.tree-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex-wrap: wrap;
  justify-content: space-around;
  width: 90%; /* Adjust this to change the width of the component */
  height: 90%; /* Adjust this to change the height of the component */
  margin: auto; /*Centers the component on the page */
}

.parent-card-container {
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  position: relative;
}

.parent-card{
    margin: 1em;
}

.children-card {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 0.5em;
  width: 50%;
  position: relative;
}

.dragArea {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex-wrap: wrap;
  position: relative;
}

.dragArea .children-card:nth-child(even) {
  align-self: flex-end;
}

.dragArea::before {
  content: "";
  position: absolute;
  top: 0;
  bottom: 0;
  left: 50%;
  border-left: 1px solid black;
}

.children-card::before {
  content: "";
  position: absolute;
  top: 50%;
  left: 0;
  right: 0;
  border-top: 1px solid black;
}

</style>