import http from '../api'

// login user
const login = async (credentials) => {
  return await http.post('/login', credentials)
}

const register = async (info) => {
  return await http.post('/register', info)
}

const logout = async () => {
  return await http.post('/logout')
}

export default {
  login,
  register,
  logout
}
