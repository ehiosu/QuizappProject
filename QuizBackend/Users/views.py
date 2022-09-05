from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Users.serializer import TeacherSerializer,UserSerializer,BaseUserSerializer,StudentSerializer
from Users.models import Teacher,Student



class CreateTeacher(APIView):
    def post(self,request):
        print(request.data)
        _user=UserSerializer(data=request.data)
        
        #serializer=TeacherSerializer(data=request.data)
       
        
        if _user.is_valid():
            user=_user.save()
            user.set_password(user.password)
            print(user)
            _baseUser=BaseUserSerializer(data={"user":user.id,"Profile_pic":request.data["Profile_Pic"]})
            print(_baseUser)
            if _baseUser.is_valid():
                baseUser=_baseUser.save()
                print(baseUser)
                _teacher=TeacherSerializer(data ={"user":baseUser.id})
                if _teacher.is_valid():
                    teacher=_teacher.save()
                    print(teacher)
                    print("user above me")
                    return Response(status=status.HTTP_200_OK)
                else:
                    print("teacher invalid")
                    baseUser.delete()
                    user.delete()
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                print("base user invalid")
                user.delete()
                return Response(_baseUser.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(_user.errors,status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
class CreateStudent(APIView):
     def post(self,request):
        _user=UserSerializer(data=request.data)    
        if _user.is_valid():
            user=_user.save()
            user.set_password(user.password)
            print(user)
            _baseUser=BaseUserSerializer(data={"user":user.id,"Profile_pic":request.data["Profile_Pic"]})
            print(_baseUser)
            if _baseUser.is_valid():
                baseUser=_baseUser.save()
                print(baseUser)
                _student=StudentSerializer(data ={"user":baseUser.id})
                if _student.is_valid():
                    student=_student.save()
                    return Response(status=status.HTTP_200_OK)
                else:
                    print("teacher invalid")
                    baseUser.delete()
                    user.delete()
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                print("base user invalid")
                user.delete()
                return Response(_baseUser.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(_user.errors,status=status.HTTP_400_BAD_REQUEST)

class getTeachers(APIView):
    def get(self,request):
        _teachers = Teacher.objects.filter(pk=1)
        print(_teachers)
        teachers=TeacherSerializer(_teachers)
        return Response(teachers.data)