import http from '../api'


/**
 * @description returns the members' parents
 * from the api
 * @param {*} memberId 
 * @returns 
 */
const getParents = async (memberId, params) =>{
    return await http.get(`parents/${memberId}/`, {params})
}

export default {
    getParents,
}