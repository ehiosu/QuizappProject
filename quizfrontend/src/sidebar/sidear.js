import React, { useState } from 'react'
import { AnimatePresence, motion } from 'framer-motion'
import '../Landing.css'
import { FaBars } from 'react-icons/fa'
import { NavLink } from 'react-router-dom'
import { GrClose } from 'react-icons/gr'
import { Avatar } from '@mui/material'
export const Sidebar = ({ content, user }) => {
  const [collapsed, setcollapsed] = useState(false)
  const toggle = () => {
    setcollapsed(!collapsed)
  }
  console.log(user)

  return (
    <motion.div
      animate={{ width: collapsed ? '100px' : '300px' }}
      transition={{ duration: 0.5 }}
      className="sidebar"
    >
      <div className="top_section">
        {collapsed ? <></> : <h1 className="brand">QuizNow</h1>}
        <div className="bars">
          {collapsed ? (
            <FaBars onClick={toggle} />
          ) : (
            <GrClose onClick={toggle} />
          )}
        </div>
      </div>
      {collapsed ? (
        <Avatar className="avatar">{user.first_name[0]}</Avatar>
      ) : (
        <></>
      )}
      <main className="routes">
        {content.map((cont) => {
          const style =
            window.location.pathname === cont.to ? 'link active' : 'link'
          return collapsed ? (
            <NavLink className={style} to={cont.to} key={cont.title}>
              <div className="icon">{cont.icon}</div>
            </NavLink>
          ) : (
            <NavLink to={cont.to} key={cont.title} className={style}>
              <div className="icon">{cont.icon}</div>
              <AnimatePresence>
                {!collapsed && (
                  <motion.div className="text">{cont.title}</motion.div>
                )}
              </AnimatePresence>
            </NavLink>
          )
        })}
      </main>
    </motion.div>
  )
}
