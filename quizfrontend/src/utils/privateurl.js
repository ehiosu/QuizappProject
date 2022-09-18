import { createContext, useState, useEffect } from 'react'

const AuthContext = createContext()

export default AuthContext

export const AuthProvider = ({ children }) => {
  ;<AuthContext.Provider value={{ name: 'test14' }}>
    {children}
  </AuthContext.Provider>
}
