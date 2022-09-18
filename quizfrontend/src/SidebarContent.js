import SchoolIcon from '@mui/icons-material/School'
import ChatIcon from '@mui/icons-material/Chat'
import PersonIcon from '@mui/icons-material/Person'
import { TiGroup } from 'react-icons/ti'
import { BsFillChatRightDotsFill } from 'react-icons/bs'
import { GiTeacher } from 'react-icons/gi'
export const content = [
  {
    title: 'Rooms',
    icon: <TiGroup />,
    to: '/Home',
  },
  {
    title: 'Chat',
    icon: <BsFillChatRightDotsFill />,
    to: '/Chat',
  },
  {
    title: 'Teachers',
    icon: <GiTeacher />,
    to: '/Teachers',
  },
]
