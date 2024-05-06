import http from '../api'


//get a member family tree
/**
 * 
 * @param {*} memberId 
 * @returns 
 */
const getFamily = async (memberId) => {
    return await http.get(`/family/${memberId}`)
}

//creates a family
const createFamily = async (input) => {
    return await http.post('/family', input)
}

// update family info
const updateFamily = async(familyId, input) => {
    return await http.put(`/family/${familyId}`, input)
}

// delete family
const deleteFamily = async (familyId) => {
    return await http.delete(`/family/${familyId}`)
}

//get family member
// create  family Member
const getFamilyMember = async(memberId) => {
    return await http.get(`/family/${memberId}`)
}
// create  family Member
const createFamilyMember = async(familyId, input) => {
    return await http.post(`/family/${familyId}/create-member`, input)
}
// Deletefamily  Member
const deleteFamilyMember = async (familyId, memberId) => {
    return await http.delete(`/family/${familyId}/${memberId}`)
}

// Update family Member
const updateFamilyMember = async (memberId, input) => {
    return await http.put(`/family/${memberId}`, input)
}

// getfamily members
const getFamilyMembers = async (familyId) => {
    return await http.get(`/familys/${familyId}`)
}

// delete family members
const deleteFamilyMembers = async (familyId) => {
    return await http.delete(`/family/${familyId}`)
}
//get ancestors of a member
const getAncestors = async (memberId) => {
    return await http.get(`/family/ancestors/${memberId}`)
}

// get decendants of a member
const getDecendants = async (memberId) => {
    return await http.get(`/family/decendants/${memberId}`)
}


export default {
    getFamily,
    createFamily,
    updateFamily,
    deleteFamily,
    getFamilyMember,
    createFamilyMember,
    updateFamilyMember,
    deleteFamilyMember,
    getFamilyMembers,
    deleteFamilyMembers,
    getAncestors,
    getDecendants
}