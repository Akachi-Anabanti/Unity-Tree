import http from '../api'

// get a single user
const getUser = async (id) => {
    return await http.get(`user/${id}`)
}

//delete user
const deleteUser = async (id)=> {
    return await http.delete(`user/${id}`)
}

// create user
const createUser = async (input) => {
    return await http.put('user', input)
}

//update a user
const updateUser = async(id, input) => {
    return await http.put(`user/${id}`, input)
}

export default{
    getUser,
    deleteUser,
    createUser,
    updateUser
}