<script setup>
  import { nextTick, onUpdated, onMounted, ref, watch, watchEffect} from 'vue';
  import { VueDraggableNext as draggable } from 'vue-draggable-next';
  import memberCard from './memberCard.vue';
  import { useAlertStore } from '@/stores/alert';
  import { useFamilyStore } from '@/stores/family';
  import adjustHeight from '@/_helpers';


  const useAlert = useAlertStore()
  const useFamily = useFamilyStore()

  //memberId

  const container = ref(null);
  const familyMembers = ref({})
  familyMembers.value = useFamily.familyMembers

  const showConfirmModal = ref(false)
  const modalRemovePerson = ref({})
  const modalRemovePersonFamId = ref("")
  const confirmModalDelete = ref(false)

  //options for the modal button
  const modalButtonOptions = ref({
    color:"danger",
    hoverMaskColor:"#ffff"
  })

  onMounted(() => {
    if (useFamily.familyMembersLoaded && useFamily.numberOfChildren != 0){
      adjustHeight(container);
    }
  });

  const handleModalOk = async (hide) => {
    // set modeldelte value
    confirmModalDelete.value = true
    hide()
  }

  // Handles Child member removal
  const promptDelete = (person) => {
    modalRemovePerson.value = person
    modalRemovePersonFamId.value = useFamily.familyData.id
    showConfirmModal.value = true

  }

  // watches for the change in value of confirmModal.delte value
  // and sends the dispatches
  watchEffect(()=>{
    if (confirmModalDelete.value){
      useFamily.dispatchDeleteFamilyMember(modalRemovePersonFamId.value, modalRemovePerson.value.id)
      .then((res) =>{
        if(res.success) {
          const message = `${modalRemovePerson.value.name} removed!`;
          useAlert.dispatchShowMainAlertSuccess(message);
        }else if (!res.success && res.status === 401){
          useAlert.dispatchShowMainAlertFailure('Server did not return any response!')

        } else {
          useAlert.dispatchShowMainAlertFailure("failed to remove member! :(");
        }
      })
      .catch((error) => {
        console.error(error);
        useAlert.dispatchShowMainAlertFailure("failed to remove member! :(")
      });

      confirmModalDelete.value = !confirmModalDelete.value
    }
  });

  //tries to recalulate height
  onUpdated(() => {
    adjustHeight(container)
  })

  // Watches for changes in the length of the children value
  watch(
    () => useFamily.numberOfChildren,
    () => nextTick(() => {
        adjustHeight(container)
    })
  )

  async function getMemberFamily (memberId) {
    // Fetch the new family data based on memberId
    await useFamily.dispatchGetFamily(memberId)
    .then(() =>{
    }).catch((error) =>{
      console.error(error)
    })

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
            <div v-for="(person, role) in familyMembers" :key="role" class="parent-card"
                :class="{'father': role === 'father', 'mother': role === 'mother'}">
                <memberCard v-if="role != 'children'" v-bind="person" @removeMember="promptDelete(person)"/>
            </div>
        </div>
        <div class="children-container" ref="container">
            <draggable v-model="familyMembers.children" class="dragArea"
            group="description"
              >
                <TransitionGroup type="transition" name="flip-list">
                    <div v-for="(person, index) in familyMembers.children" :key="index" class="children-card"
                        :class="{'left':index % 2 === 0, 'right':index % 2 === 1} ">
                        <memberCard  v-bind="person" @removeMember="promptDelete(person)"
                          @cardClick="getMemberFamily"/>
                    </div>
                </TransitionGroup>
            </draggable>
        </div>
    </div>
</template>

<style scoped>
@import '@/assets/tree.css';
</style>