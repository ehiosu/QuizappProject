import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'

import reportWebVitals from './reportWebVitals'
import { HomePage } from './HomePage'
import { Landing } from './Landing'
import { Teachers } from './Teachers'
import { AuthProvider } from './context/Authcontext'
import {Response} from './Responses'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
const root = ReactDOM.createRoot(document.getElementById('root'))
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <AuthProvider>
        <Routes>
          <Route path="/" element={<HomePage />}></Route>
          <Route path="/Home" element={<Landing />}></Route>
          <Route path="/Chat" element={<Landing />}></Route>
          <Route path="/Teachers" element={<Teachers />}></Route>
          <Route path="/Home/Responses/:id" element={<Response />}></Route>

        </Routes>
      </AuthProvider>
    </BrowserRouter>
  </React.StrictMode>,
)

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals()
