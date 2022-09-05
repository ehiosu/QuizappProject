from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from django.http import JsonResponse
import jwt
import datetime
from  rest_framework import serializers
# from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes

from Users.serializer import TeacherSerializer,StudentSerializer
from Users.models import Teacher,User
from rest_framework.views import APIView

class CreateTeacher(APIView):
    def post(self,request):
        teacher=TeacherSerializer(data=request.data)
        if teacher.is_valid():
            teacher.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(teacher.errors,status=status.HTTP_400_BAD_REQUEST)
# Create your views here.

class CreateStudent(APIView):
    def post(self,request):
        student=StudentSerializer(data=request.data)
        print(student)
        if student.is_valid():
            student.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(student.errors,status=status.HTTP_400_BAD_REQUEST)

class getTeachers(APIView):
    def get(self,request):
        
        users=User.objects.filter(role=User.Role.TEACHER).values('id','username','email')
        
        
        return  JsonResponse({"data":list(users)})