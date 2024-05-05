<script setup>
  import { nextTick, onMounted, reactive, ref, watch, watchEffect} from 'vue';
  import { VueDraggableNext as draggable } from 'vue-draggable-next';
  import memberCard from './memberCard.vue';
  import { useAlertStore } from '@/stores/alert';
  import { useFamilyStore } from '@/stores/family';
// import { storeToRefs } from 'pinia';

  const useAlert = useAlertStore()
  const useFamily = useFamilyStore()

  //Delete events
  // const emit = defineEmits(['childDeleted', 'parentDeleted'])

  const container = ref(null);
  const family = reactive({})
  family.value = useFamily.familyData ///BEGIN DEBUGING HERE

  const showConfirmModal = ref(false)
  const modalRemovePerson = ref({})
  const confirmModalDelete = ref(false)

  //options for the modal button
  const modalButtonOptions = ref({
    color:"danger",
    hoverMaskColor:"#ffff"
  })

  onMounted(() => {
    adjustHeight();
  });

  const handleModalOk = async (hide) => {
    // set modeldelte value
    confirmModalDelete.value = true
    hide()
  }

// Handles Child member removal
  const promptDelete = (person) => {
    modalRemovePerson.value = person
    showConfirmModal.value = true

  }
// watch for the confirmation of delete
watchEffect(() => {
  if (confirmModalDelete.value ) {
      if (modalRemovePerson.value.role === 'child') {
          const res = useFamily.dispatchDeleteChild(modalRemovePerson.value)
          if (res.success){
            const message = `${modalRemovePerson.value.name} removed!`
            useAlert.dispatchShowMainAlertSuccess(message)
          } else if (!res.success && res.status === 401){
            useAlert.dispatchShowMainAlertFailure("Server did not return any response!")
          } else {
            useAlert.dispatchShowMainAlertFailure("Something went wrong! :(")
          }
        
      } else {
          const res = useFamily.dispatchDeleteParent(modalRemovePerson.value)

          if (res.success){
            const message = `${modalRemovePerson.value.name} removed!`
            useAlert.dispatchShowMainAlertSuccess(message)
          } else if (!res.success && res.status === 401) {
            useAlert.dispatchShowMainAlertFailure("Server did not return any response!")
          } else {
            useAlert.dispatchShowMainAlertFailure("Something went wrong! :(")
          }
      }

    confirmModalDelete.value = false

  } 
})
  // Watches for changes in the length of the children value
  watch(
    () => useFamily.numberOfChildren,
    () => nextTick(() => {
        adjustHeight()
    })
  )

  // Adjusts the height of the children stem line
  // based on the number of children
function adjustHeight() {
    const cards = container.value.querySelectorAll('.children-card');
    const lastCard = cards[cards.length -1];
    const rectContainer = container.value.getBoundingClientRect();
    const rectLastCard = lastCard.getBoundingClientRect();
    const height = rectContainer.height - (rectLastCard.height / 2);
    container.value.style.setProperty('--dynamic-height', `${height}px`);
  }
</script>


<template>
    <VaModal
      v-model="showConfirmModal"
      size="auto"
      okText="Yes"
      cancelText="No"
      :child:okButton="modalButtonOptions"
      :beforeOk="handleModalOk"
     >
     Remove <em>{{ modalRemovePerson.name }}</em> from family?
     </VaModal>
    <div class="tree-container">
        <div class="parent-card-container" >
            <div v-for="(person, role) in family" :key="role" class="parent-card"
                :class="{'father': role === 'father', 'mother': role === 'mother'}">
                <memberCard v-if="role != 'children'" v-bind="person" @removeMember="promptDelete(person)"/>
            </div>
        </div>
        <div class="children-container" ref="container">
            <draggable v-model="family.children" class="dragArea"
            group="description"
              >
                <TransitionGroup type="transition" name="flip-list">
                    <div v-for="(person, index) in family.children" :key="index" class="children-card"
                        :class="{'left':index % 2 === 0, 'right':index % 2 === 1} ">
                        <memberCard  v-bind="person" @removeMember="promptDelete(person)"/>
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