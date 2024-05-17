import http from '../api'

//get a member family tree
/**
 *
 * @param {*} _Id
 * _Id can be family Id or MemberId
 * @returns
 */
const getFamily = async (_Id) => {
  return await http.get(`/family/${_Id}`)
}

//creates a family
const createFamily = async (input) => {
  if (input.member == true) {
    /**
     * if the current logged in user is a member
     * of the family being created then call the user create family endpoint
     * to create the family of the user
     */
    return await http.post('/user/family', input)
  }
  return await http.post('/family', input)
}

// update family info
const updateFamily = async (familyId, input) => {
  return await http.put(`/family/${familyId}`, input)
}

// delete family
const deleteFamily = async (familyId) => {
  return await http.delete(`/family/${familyId}`)
}

//get family member
// create  family Member
const getFamilyMember = async (memberId) => {
  return await http.get(`/family/member/${memberId}`)
}
// create  family Member
const createFamilyMember = async (familyId, input) => {
  return await http.post(`/family/member/${familyId}`, input)
}
// Deletefamily  Member
const deleteFamilyMember = async (familyId, memberId) => {
  return await http.delete(`/family/member/${familyId}/${memberId}`)
}

// Update family Member
const updateFamilyMember = async (memberId, input) => {
  return await http.put(`/family/member/${memberId}`, input)
}

// getfamily members
const getFamilyMembers = async (familyId) => {
  return await http.get(`/family/members/${familyId}`)
}

// delete family members
const deleteFamilyMembers = async (familyId) => {
  return await http.delete(`/family/members/${familyId}`)
}
//get ancestors of a member
const getAncestors = async (memberId) => {
  return await http.get(`/family/ancestors/${memberId}`)
}

// get decendants of a member
const getDecendants = async (memberId) => {
  return await http.get(`/family/decendants/${memberId}`)
}

const getSibilings = async (memberId) => {
  return await http.get(`/family/member/get-siblings/${memberId}`)
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
  getDecendants,
  getSibilings
}
