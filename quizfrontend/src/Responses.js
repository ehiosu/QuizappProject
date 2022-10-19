import axios from "axios"
import { useEffect,useState } from "react"
import { useNavigate, useParams } from "react-router-dom"
import { BiSearchAlt } from "react-icons/bi"
import svg from './undraw_team_up_re_84ok.svg'
import { Sidebar } from "./sidebar/sidear"
import jwt_decode from 'jwt-decode'
import { content } from './SidebarContent'
import { Avatar } from '@mui/material'
import {data} from './testdata'
import Cookies from "universal-cookie"
export const Response=()=>{
const [responses,setresponse]=useState([])
const [loading,setloading]=useState(true)
let {id}= useParams()
const cookies=new Cookies()
const navigate = useNavigate()
const token = cookies.get('token')
console.log(token)
let usr = jwt_decode(token)
useEffect(()=>{

axios(
    {
        method:'get',
        url:`http://127.0.0.1:8000/api/Users/auth/Quiz/${id}`
    }
).then((response=>{
    console.log(response)
    if (response.data.Quiz.length>0){
        axios({
            method:"get",
            url:`http://127.0.0.1:8000/api/Users/responses/${id}`
            
        }).then((response)=>{
            console.log(response.data)
            setresponse(response.data)
            setloading(false)
        })
    }
   
})).catch((err)=>{
    navigate("/Home")
})

},[])
    return(
        loading?
        <>
        <h2>loading</h2>
        
        
        </>:
       <div className="container-fluid ">
       <div className="row row-container">
        <div className="col-3">
        <Sidebar content={content} user={usr} />
        </div>
     <div className="col scores-section">
        <div className="row">
            <div className="profile-section-resp">
            <Avatar style={{ color: ' color: #645da5' }}>
                  {usr.first_name[0]}
                </Avatar> 
            <div className="inner-text">
              <h4>
                Hi,these are the responses to your Quiz.
              </h4>
              <p></p>
              <div className="search">
              <input type="search" name="" id="" />
              <BiSearchAlt className="icon" />
            </div>
            </div>
          
            </div>
        </div>
     <div className="scores-container p-3">
     <div className="row gap-3 myrow ">
       {data.map((resp,index)=>{
        console.log(resp.username["first_name"])
           return(
               <ScoreComp key ={index}score={resp.score} first_name={resp.username.first_name} last_name={resp.username.last_name} username={resp.username.username}/>
           )
       }
       )}
       
       </div>
     </div>
     </div>
       </div></div>
    )
}

const ScoreComp=(props)=>{
    
    console.log(props)
    return(
        <div className="col-3 score-container card p-2 " style={{"width": "18rem"}}>
            <img src={svg} class="card-img-top" alt="..."></img>
            <div className="card-body">
                
            <p className="score card-text">
                
            Score: { props.score}
            </p>
            <p className="score card-text">
                
             Name: { props.first_name} {props.last_name}
            </p>
            <p className="score card-text">
                 
            username: { props.username}
            </p>
            </div>
        </div>
    )
}