import React from 'react'
import { useState, useEffect, useContext } from 'react'
// import svg from './undraw_content_team_re_6rlg.svg'
import svg from './undraw_good_team_re_hrvm.svg'
import loginimg from './undraw_reminder_re_fe15.svg'
import { useNavigate } from 'react-router-dom'
import AuthContext from './context/Authcontext'
import Cookies from 'universal-cookie'

export const HomePage = () => {
  const navigate = useNavigate()
  let { login, authtoken } = useContext(AuthContext)

  const OpenSignUpPage = () => {
    const container = document.querySelector('.Container')

    if (container.classList.contains('loginmode')) {
      container.classList.remove('loginmode')
      container.classList.add('signupmode')
    }
    container.classList.add('signupmode')
  }
  const OpenLoginPage = () => {
    const container = document.querySelector('.Container')
    if (container.classList.contains('signupmode')) {
      container.classList.remove('signupmode')
      container.classList.add('loginmode')
    }

    container.classList.add('loginmode')
  }
  const [username, setusername] = useState('')
  const [password, setpassword] = useState('')
  const handlecvalues = (e) => {
    if (e.target.name === 'username') {
      setusername(e.target.value)
    } else if (e.target.name === 'password') {
      setpassword(e.target.value)
    }
  }
  const handlelogin = async () => {
    const loggedin = await login(username, password)
    console.log(loggedin)
    if (loggedin) {
      console.log('Logged In')
      const cookies = new Cookies()
      cookies.set('token', loggedin, '/')
      navigate('/Home')
    } else {
      console.log('not Logged In')
    }
  }
  return (
    <div className="Container">
      <div>
        <div className="forms-container">
          <div className="signin-signup">
            {/* SIGNINSECTION */}
            <form className="sign-in-form">
              <h2 className="title">Sign In</h2>
              <div className="input-field">
                <i className="fas fa-user"></i>
                <input
                  type="text"
                  name="username"
                  onChange={handlecvalues}
                  disabled={false}
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
                className="btn solid"
                placeholder="Login"
                onClick={handlelogin}
              >
                Login
              </button>

              <p className="forgot-password">Forgot your Password?</p>
            </form>
            {/* SIGNINSECTIONEND */}

            <form className="sign-up-form">
              {/* SIGNUPSECTIONBEGIN */}
              <div className="sign-up-form">
                <div className="sign-in-container">
                  <h2 className="title">Sign Up</h2>
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
                  <div className="input-field">
                    <i className="fas fa-envelope"></i>
                    <input
                      type="text"
                      name="email"
                      onChange={handlecvalues}
                    ></input>
                    <span className="placeholder">Email</span>
                  </div>
                  <div className="input-field">
                    <i className="fas fa-user"></i>
                    <input
                      type="text"
                      name="fn"
                      onChange={handlecvalues}
                    ></input>
                    <span className="placeholder">First Name</span>
                  </div>
                  <div className="input-field">
                    <i className="fas fa-user"></i>
                    <input
                      type="text"
                      name="ln"
                      onChange={handlecvalues}
                    ></input>
                    <span className="placeholder">Last Name</span>
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
            </form>
          </div>
        </div>
      </div>
      <div className="panels-container">
        <div className="panel left-panel">
          <div className="content">
            <h3 className="text">New here?</h3>
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Mollitia
              ut omnis saepe, doloribus beatae cumque ex voluptates debitis quo
              facere consequuntur quas. Ipsum, voluptates fuga neque nihil
              aspernatur repudiandae deserunt!
            </p>
            <button
              className="btn transaprent"
              id="signupbtn"
              onClick={OpenSignUpPage}
            >
              Sign Up
            </button>
            <img src={svg} className="image" alt=""></img>
          </div>
        </div>
        <div className="panel right-panel">
          <div className="content">
            <h3 className="text">Already Have an account?</h3>
            <p>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Ut ab,
              facilis autem doloribus explicabo expedita veniam recusandae totam
              quibusdam sequi amet obcaecati, tempora sit aperiam, in quisquam
              consequuntur maxime unde.
            </p>
            <button
              className="btn transaprent"
              id="signinbtn"
              onClick={OpenLoginPage}
            >
              log In
            </button>
            <img src={loginimg} className="image" alt=""></img>
          </div>
        </div>
      </div>
    </div>
  )
}
