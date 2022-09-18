import axios from 'axios'
import { createContext, useState, useEffect } from 'react'
import jwt_decode from 'jwt-decode'
import { useNavigate } from 'react-router-dom'

const AuthContext = createContext()

export default AuthContext
let userr = null
export const AuthProvider = ({ children }) => {
  const nav = useNavigate()
  let [authtoken, setauthtoken] = useState('')
  const [user, setUser] = useState(null)
  let token = ''
  const login = async (username, password) => {
    let loggedin = true
    console.log(username, password)
    const response = await axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/api/Users/auth/Login',
      data: {
        username: username,
        password: password,
      },
    }).then((resp) => {
      if (resp.status === 200) {
        console.log(resp.data)
        setauthtoken(resp.data.jwt)
        console.log(authtoken)
        console.log(jwt_decode(resp.data.jwt))
        token = resp.data.jwt
        const details = jwt_decode(resp.data.jwt)
        console.log(details.first_name)
        setUser(details)
        loggedin = true
        console.log(user)
      } else {
        alert('something    went    wrong')
        loggedin = false
      }
    })
    return token
  }
  let contextdata = {
    login: login,
    user: user,
    authtoken: authtoken,
  }
  return (
    <AuthContext.Provider value={contextdata}>{children}</AuthContext.Provider>
  )
}
