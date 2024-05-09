import http from '../api'

// get a single user
const getUser = async () => {
    return await http.get(`user/`)
}

//delete user
const deleteUser = async (id)=> {
    return await http.delete(`user/${id}`)
}
//update a user
const updateUser = async(id, input) => {
    return await http.put(`user/${id}`, input)
}

export default{
    getUser,
    deleteUser,
    updateUser
}