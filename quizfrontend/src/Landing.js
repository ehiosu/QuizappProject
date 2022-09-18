import axios from 'axios'
import React from 'react'
import Cookies from 'universal-cookie'
import { useEffect, useState, useContext } from 'react'
import jwt_decode from 'jwt-decode'
import './Landing.css'
import { motion } from 'framer-motion'
import { content } from './SidebarContent'
import { Link } from 'react-router-dom'
import { Sidebar } from './sidebar/sidear'
import { Avatar } from '@mui/material'
import { BiSearchAlt } from 'react-icons/bi'
import { AiOutlineArrowRight } from 'react-icons/ai'
import { data } from './RoomData'
const cookies = new Cookies()
export const Landing = () => {
  // const [user, setUser] = useState({})
  const [loading, setLoading] = useState(false)
  const [user, setuser] = useState(null)
  const [quizes, setquizes] = useState([])

  useEffect(() => {
    const token = cookies.get('token')
    console.log(token)
    let usr = jwt_decode(token)
    console.log(usr.first_name)
    console.log(usr.role)
    if (usr) {
      setuser(usr)
      setLoading(true)
    }
  }, [])
  // const { user } = useContext(AuthContext)

  // return <div>{loading ? 'loading' : <StudentLandingHome user={user} />}</div>
  return (
    <div className="">
      {loading ? <MainComponent user={user} /> : <h2>Loading</h2>}
    </div>
  )
}

const StudentLandingHome = (user, quizes, collapsed) => {
  // console.log(user)

  // const { id, username, first_name, last_name, role } = user.user
  return (
    <>
      <div className="Landing-container">
        <Sidebar content={content} user={user} className="main-sidebar" />

        <div className="main-section">
          <h2 className="rooms">Rooms</h2>
        </div>
      </div>
    </>
  )
}

const QuizComp = (quiz) => {
  return <div>Landing</div>
}

const MainComponent = ({ user }) => {
  // console.log(user)
  return user.role === 'TEACHER' ? (
    <TeacherLandingHome user={user} />
  ) : (
    <StudentLandingHome user={user} />
  )
}

const TeacherLandingHome = ({ user }) => {
  return (
    <>
      <div className="landing-container">
        <div>
          <Sidebar content={content} user={user} className="aide" />
        </div>
        <div className="main-section">
          <div className="profile-section">
            <Avatar style={{ color: ' color: #645da5' }}>
              {user.first_name[0]}
            </Avatar>
            <div className="inner-text">
              <h2>
                Hi,
                {user.first_name} {user.last_name}
              </h2>
              <p></p>
            </div>
            <div className="search">
              <input type="search" name="" id="" />
              <BiSearchAlt className="icon" />
            </div>
          </div>

          <div className="room-section">
            <div className="room-title">
              <h3 className="title">Rooms</h3>
              <span></span>
            </div>
            {data.map((room, index) => {
              return <RoomComp key={room.id} room={room} index={index} />
            })}
          </div>
        </div>
      </div>
    </>
  )
}

const RoomComp = ({ room, index }) => {
  return (
    <motion.div
      className="room-container"
      initial={{ opacity: 0, translateY: -100 }}
      animate={{ opacity: 1, translateY: 0 }}
      transition={{ duration: 0.5, delay: index + 0.05 }}
    >
      <img src={room.url} alt={room.name} />
      <div className="text-info">
        <p className="organizer">
          Organizer
          <AiOutlineArrowRight className="icon" /> {room.organizer}{' '}
        </p>
        <h2 className="room-name">{room.name}</h2>
      </div>
    </motion.div>
  )
}
