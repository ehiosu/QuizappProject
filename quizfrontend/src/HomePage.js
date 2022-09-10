import React from 'react'
import { useState } from 'react'

export const HomePage = () => {
  const [username, setusername] = useState('')
  const [password, setpassword] = useState('')
  const handlecvalues = (e) => {
    if (e.target.name === 'username') {
      setusername(e.target.value)
    } else if (e.target.name === 'password') {
      setpassword(e.target.value)
    }
  }
  const login = () => {
    console.log(username + password)
  }
  return (
    <div className="container">
      <div className="form-container">
        <div className="input-container">
          <div className="signin-signup">
            {/* SIGNINSECTION */}
            <div className="sign-in">
              <div className="sign-in-container">
                <h2 className="title">Sign In</h2>
                <div className="input-field">
                  <i className="fas fa-user"></i>
                  <input
                    type="text"
                    name="username"
                    onChange={handlecvalues}
                  ></input>
                  <span className="placeholder">Username</span>
                </div>
                <div className="input-field">
                  <i className="fas fa-lock"></i>
                  <input
                    type="password"
                    name="password"
                    onChange={handlecvalues}
                  ></input>
                  <span className="placeholder">Password</span>
                </div>
                <button
                  type="button"
                  className="btn-login"
                  placeholder="Login"
                  onClick={login}
                >
                  Login
                </button>

                <p className="text">Don't have an accpunt? Create One</p>
                <p className="forgot-password">Forgot your Password?</p>
              </div>
            </div>
            {/* SIGNINSECTIONEND */}
            <div className="sign-up">{/* SIGNUPSECTIONBEGIN */}</div>
          </div>
        </div>
      </div>
    </div>
  )
}
