import http from '../api'


//get a member family tree
/**
 * 
 * @param {*} memberId 
 * @returns 
 */
const getFamily = async (memberId) => {
    return await http.get(`/show-tree/${memberId}`)
}

const createFamily = async (input) => {
    return await http.post('/tree', input)
}

//get ancestors of a member
/**
 * @description This is ta wo way recursive call to get parents
 * @param {*} memberId 
 * @returns 
 */
const getAncestors = async (memberId) => {
    return await http.get(`/show-tree/ancestors/${memberId}`)
}

// get decendants of a member
/**
 * @description This is a two way recursive call to get parent
 * @param {*} memberId 
 * @returns 
 */
const getDecendants = async (memberId) => {
    return await http.get(`/show-tree/decendants/${memberId}`)
}


export default {
    getFamily,
    createFamily,
    getAncestors,
    getDecendants
}