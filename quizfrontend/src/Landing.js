import axios from 'axios'
import React from 'react'
import Cookies from 'universal-cookie'
import { useEffect, useState, useContext } from 'react'
import jwt_decode from 'jwt-decode'
import './Landing.css'
import { motion } from 'framer-motion'
import { content } from './SidebarContent'
import { Link, useNavigate } from 'react-router-dom'
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
  const [Teachers,SetTeacher]= useState([])

  useEffect(() => {
    const token = cookies.get('token')
    console.log(token)
    let usr = jwt_decode(token)
    console.log(usr.first_name)
    console.log(usr.role)
    if (usr) {
      if (usr.role !== "TEACHER")
      {
        axios.post('http://127.0.0.1:8000/api/Users/auth/get',{headers:{"Authorization" : `Bearer ${token}`},token:token}).then((response)=>{
          console.log(response.data.Teachers)
          
          let temp = []
          let i =0;
          for(i;i<response.data.Teachers.length;i++){
            temp.push(response.data.Teachers[i])
          }
          SetTeacher(temp)
        })
      }
      console.log(Teachers)
      setuser(usr)
      setLoading(true)
    }
  }, [])
  // const { user } = useContext(AuthContext)

  // return <div>{loading ? 'loading' : <StudentLandingHome user={user} />}</div>
  return (
    <div className="">
      {loading ? <MainComponent user={user} Teachers={Teachers}/> : <h2>Loading</h2>}
    </div>
  )
}

const StudentLandingHome = ({user,Teachers}) => {
  const [teachers,setteachers]= useState([])
  let tmp = []
  useEffect(()=>{
   
    for(let i =0;i<Teachers.length;i++)
    {
      tmp.push(Teachers[i])
    } 
    setteachers(Teachers)
  
  })
  
  const filter =(e)=>{
    console.log(e.target.value)
    let re = /[e.target.value]/
    if (e.target.value === ""){
      setteachers(Teachers)
    }
    else{
      let temp =Teachers.filter(teach=>teach.username.includes(e.target.value))
    
      setteachers(temp)
    }
  }
  // const { id, username, first_name, last_name, role } = user.user
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
              <Link to={''}>
              <h2>
                Hi,
                {user.first_name} {user.last_name}
              </h2>
              <p></p>
              </Link> 
            </div>
            <div className="search">
              <input type="search" name="" id="" onChange={filter} />
              <BiSearchAlt className="icon" />
            </div>
          </div>

          <div className="room-section">
            <div className="room-title">
              <h3 className="title">Teachers</h3>
              <span></span>
            </div>
            {teachers.map((teacher, index) => {
              return <RoomComp key={index} room={teacher} index={index} />
            })}
          </div>
        </div>
      </div>
    </>
  )
}

const QuizComp = (quiz) => {
  return <div>Landing</div>
}

const MainComponent = ({ user,Teachers }) => {

  // console.log(user)
  console.log(Teachers)
  return user.role === 'TEACHER' ? (
    <TeacherLandingHome user={user} />
  ) : (
    <StudentLandingHome user={user} Teachers={Teachers}/>
  )
}

const TeacherLandingHome = ({ user }) => {
  const [loading,setLoading]=useState(true)
  const [Quizzes,setQuizzes]=useState([])

  const filter =async(e)=>{
    if (e.target.value ===""){
      await axios({
        method:'get',
        url:`http://127.0.0.1:8000/api/Users/getQuiz/${user['id']}`,
      }).then((response)=>{
        console.log(response.data["Quizes"])
       
        setQuizzes(response.data["Quizes"])
        console.log(Quizzes)
       
      })
    }
    else{
      let temp =Quizzes.filter((quiz)=>
        quiz.Name.includes(e.target.value)
      )
      console.log(temp)
      setQuizzes(temp)
    }
   
  }
 useEffect(()=>{
  let token=cookies.get('token')
  console.log(token)
  axios({
    method:'get',
    url:`http://127.0.0.1:8000/api/Users/getQuiz/${user['id']}`,
  }).then((response)=>{
    console.log(response.data["Quizes"])
   
    setQuizzes(response.data["Quizes"])
    console.log(Quizzes)
    setLoading(false)
  })
 },[])
  return (
    loading?<><h2>Loading</h2></>:
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
              <input type="search" id="" name="search" onChange={filter} />
              <BiSearchAlt className="icon" />
            </div>
          </div>
          {Quizzes.map((quiz,index)=>{
            return(
              <QuizzesComp quiz={quiz} index={index} key={index} user={user}/>
            )
          
          })}
        
        </div>
      </div>
    </>
  )
}

const RoomComp = ({ room, index }) => {
  let imageurl = room.profile?room.profile:"https://www.anitawatkins.com/wp-content/uploads/2016/02/Generic-Profile-1600x1600.png"
  return (
    <motion.div
      className="room-container"
      initial={{ opacity: 0, translateY: -100 }}
      animate={{ opacity: 1, translateY: 0 }}
      transition={{ duration: 0.5, delay: index + 0.05 }}
    >
      
        
     
      <img src={imageurl} alt={room.username} />
      <div className="text-info">
        <p className="organizer">
          Organizer
          <AiOutlineArrowRight className="icon" /> {room.username}{' '}
        </p>
        <h2 className="room-name">{room.first_name} {room.last_name}</h2>
      </div>
    </motion.div>
  )
}
const QuizzesComp = ({ quiz, index,user }) => {
  const navigate = useNavigate()
  let imageurl = user.profile?user.profile:"https://www.anitawatkins.com/wp-content/uploads/2016/02/Generic-Profile-1600x1600.png"
  return (
    <motion.div
      className="room-container"
      initial={{ opacity: 0, translateY: -100 }}
      animate={{ opacity: 1, translateY: 0 }}
      transition={{ duration: 0.5, delay: index + 0.05 }}
    >
      
        
     
      <img src={imageurl} alt={quiz.Name} />
      <div className="text-info">
       
        <h2 className="room-name">{quiz.Name} </h2>
        <div className="bottom-panel">
          <button className="btn" onClick={()=>{navigate(`Responses/${quiz.id}`)}} >View Quiz</button>
        </div>
      </div>
    </motion.div>
  )
}
