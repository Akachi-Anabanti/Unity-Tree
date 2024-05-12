<script setup>
    import TreeComponent from '@/components/TreeComponent.vue';
    import modalComponent from '@/components/modalComponent.vue';
    import MemberForm from '@/components/MemberForm.vue';
    import { ref } from 'vue';
    import { useAlertStore } from '@/stores/alert';
    import { useFamilyStore } from '@/stores/family';


    const useAlert = useAlertStore()
    const useFamily = useFamilyStore()

    const showModal = ref(false);


// Function to handle Modal Form Submit
    const handleFormSubmit = async (newMember) => {
        await useFamily.dispatchCreateFamilyMember(useFamily.getFamilyId, newMember)
        .then((res) => {
        console.log(res)
        if (res.success) {
            const message = `${newMember.firstName} added successfully as ${newMember.role}!`
            useAlert.dispatchShowModalAlertSuccess(message)
        } else {
            const message = "Failed to Add member!"
            useAlert.dispatchShowModalAlertFailure(message)
        }
        }).catch((error) => {
        console.error(error)
        })
    }

</script>

<template>
    <modalComponent v-model="showModal">
        <template #form>
            <MemberForm  @submit="handleFormSubmit"/>
        </template>
    </modalComponent>

    <!-- Add member button -->
    <div class="flex items-center gap-8 flex-wrap add-member">
        <VaButton round icon="va-plus" size="large" @click="showModal = true"/>
    </div>
    <TreeComponent />
</template>

<style scoped>
.add-member{
    position: fixed;
    right: 70px;
    bottom: 50px;
    z-index: 100;
}

.va-modal{
    opacity: 0;
}
</style>