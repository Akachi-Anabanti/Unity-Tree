import http from '../api'


// get all users
const getUsers = async (params) => {

    return await http.get('users/', {params})
}


// get a single user
const getUser = async (id) => {
    return await http.get(`users/${id}`)
}


//delete user
const deleteUser = async (id)=> {
    return await http.delete(`users/${id}`)
}

// create user
const createUser = async (input) => {
    return await http.put('users', input)
}

//update a user
const updateUser = async(id, input) => {
    return await http.put(`users/${id}`, input)
}

export default{
    getUsers,
    getUser,
    deleteUser,
    createUser,
    updateUser
}