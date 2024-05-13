<script setup>
  import { onMounted, ref, watchEffect} from 'vue';
  import { VueDraggableNext as draggable } from 'vue-draggable-next';
  import memberCard from './memberCard.vue';
  import { useAlertStore } from '@/stores/alert';
  import { useFamilyStore } from '@/stores/family';
import { useRouter } from 'vue-router';
import { storeToRefs } from 'pinia';


  const props = defineProps({
  familyId: {
    type: String,
    required: true
  }
})


  const useAlert = useAlertStore()
  const useFamily = useFamilyStore();

  const router = useRouter()

  const container = ref(null);
  const {familyMembers} = storeToRefs(useFamily)

  const showConfirmModal = ref(false)
  const modalRemovePerson = ref({})
  const modalRemovePersonFamId = ref("")
  const confirmModalDelete = ref(false)


  const isLoading = ref(true)


  const modalButtonOptions = ref({
    color:"danger",
    hoverMaskColor:"#ffff"
  })

  onMounted(async() => {
      await useFamily.dispatchGetFamilyMembers(props.familyId)
      isLoading.value = false
      if (!useFamily.isFamilyEmpty){
        // adjust the height if the family is not empty
      }
  });


  // Watches for changes in the length of the children value

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
  watchEffect(async()=>{
    if (confirmModalDelete.value){
      try {
          const {success} = await useFamily.dispatchDeleteFamilyMember(modalRemovePersonFamId.value, modalRemovePerson.value.id)
          if (success){
            const message = `${modalRemovePerson.value.name} removed!`;
            useAlert.dispatchShowMainAlertSuccess(message);
          } else {
            useAlert.dispatchShowMainAlertFailure("failed to remove member! try again :(");
          }
      } catch (error) {
        console.error(error)
      }

      confirmModalDelete.value = !confirmModalDelete.value
    }
  });
  
  function getMemberFamily (memberId) {
    router.push("/tree", {familyId:memberId})
}
// function adjustHeight() {
//     const cards = container.value.querySelectorAll('.children-card');
//     const lastCard = cards[cards.length -1];
//     const rectContainer = container.value.getBoundingClientRect();
//     const rectLastCard = lastCard.getBoundingClientRect();
//     const height = rectContainer.height - (rectLastCard.height / 2);
//     container.value.style.setProperty('--dynamic-height', `${height}px`);
//   }

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

     <div v-if="isLoading">
      Loading...
     </div>
     <div v-else>
      <div class="tree-container" v-if="!useFamily.isFamilyEmpty">
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
    <div v-else>
      Add Members to this Family
      <h4>
        {{ useFamily.getFamilyName}}
      </h4>
    </div>
     </div>

</template>

<style scoped>
@import '@/assets/tree.css';
</style>