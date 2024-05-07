import http from '../api'


// login user
const login = async (credentials) => {
    return await http.post('/auth/login/', credentials)
}

export default {
    login
}