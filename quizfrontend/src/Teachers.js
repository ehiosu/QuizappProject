import { Sidebar } from "./sidebar/sidear"
import { useEffect,useState } from "react"
import jwt_decode from 'jwt-decode'
import Cookies from 'universal-cookie'
import axios from 'axios'
import { motion } from 'framer-motion'
import { content } from './SidebarContent'
import { Avatar } from '@mui/material'
import { BiSearchAlt } from 'react-icons/bi'
import { AiOutlineArrowRight } from 'react-icons/ai'
const cookies = new Cookies()
export const Teachers=(props)=>{
  const [user,setuser]=useState("")
  const [loading,setLoading]=useState(false)
  const [teachers,SetTeachers]=useState(null)
  let teach = []
    useEffect(()=>{
    const token = cookies.get('token')
    console.log(token)
    let usr = jwt_decode(token)
    console.log(usr.first_name)
    console.log(usr.role)
    console.log(usr)
    if (usr) {
      if (usr.role !== "TEACHER")
      {
        axios({
          method:'post',
          url:'http://127.0.0.1:8000/api/Users/getTeachers/',
         
          data:{
            token:token,
          }
        
        }).then((response)=>{
          console.log()
          SetTeachers(response.data.data)
          teach = response.data.data
          setLoading(true)
        }).catch((error)=>{
            console.log(error)
            setLoading(true)
        })
      }
      setuser(usr)
      
    }
    },[])
    return(
      loading?
        <>
            <div className="landing-container">
                <div>
                    <Sidebar user={user} content={content}/>
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
              <h3 className="title">Teachers</h3>
              <span></span>
            </div>
          {teachers.map((teacher,index)=>{
            return(
              <RoomComp room={teacher} key={index}/>
            )
          })}
          </div>
        </div>
            </div>
        </>:<><h1>loading</h1></>
    )
}

const RoomComp = ({ room, index }) => {
  const imageurl= room.profile?room.profile:"https://www.anitawatkins.com/wp-content/uploads/2016/02/Generic-Profile-1600x1600.png"
  const apply=()=>{
    axios({
      method:'put',
      url:'http://127.0.0.1:8000/api/Users/auth/enroll',
     
      data:{
        token:cookies.get('token'),
        Teachers:[room.id]
      }
    
    }).then((response)=>{
      console.log(response)
   
    }).catch((error)=>{
        console.log(error)
       
    })
  }
  return (
    <motion.div
      className="room-container"
      initial={{ opacity: 0, translateY: -100 }}
      animate={{ opacity: 1, translateY: 0 }}
      transition={{ duration: 0.5, delay: index + 0.05 }}
    >
      <img src={imageurl} alt="A picture of a cat" className="room-img"/>
      <div className="text-info">
        <p className="organizer">
          Organizer
          <AiOutlineArrowRight className="icon" /> {room.username}{' '}
        </p>
        <h2 className="room-name">{room.email}</h2>

        <div className="bottom-panel">
          <button className="btn" onClick={apply}>Apply</button>
        </div>
      </div>
    </motion.div>
  )
}