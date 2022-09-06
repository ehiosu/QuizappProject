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
from Quizzes.serializer import QuizSerializer,QuestionSerializer,AnswerSerializer
from rest_framework.views import APIView
from Quizzes.models import Quiz

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

class CreateQuiz(APIView):
    def post(self,request):
        Quiz=QuizSerializer(data=request.data)
        if Quiz.is_valid():
           
            Quiz=Quiz.save()
            print(Quiz.id)
            resp={"Quiz ID":Quiz.id,"Quiz Name":Quiz.Quiz_name}
            # resp=JsonResponse(resp)
            print(Quiz)
            # resp= JsonResponse({"id":Quiz.data['id'],"name":Quiz.data["Quiz_name"]})
            # resp = JsonResponse({"message":"done"})
            return Response(data=resp,status=status.HTTP_201_CREATED)
        else:
            return Response(Quiz.errors,status=status.HTTP_400_BAD_REQUEST)

class getQuizById(APIView):
    def get(self,request,pk):
        result =Quiz.objects.filter(Organizer=pk).prefetch_related('Questions').all().values()
        print(result)
        if (result):
            return Response(data={"Quizes":result},status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class CreateQuestion(APIView):
    def post(self,request):
        Question=QuestionSerializer(data=request.data)
        if Question.is_valid():
           
            Question=Question.save()
          
            resp={"quiz_id":request.data["quiz_id"],"Question":Question.question,"Question_ID":Question.id}
       
            # resp=JsonResponse(resp)
           
            # resp= JsonResponse({"id":Quiz.data['id'],"name":Quiz.data["Quiz_name"]})
            # resp = JsonResponse({"message":"done"})
            return Response(data=resp,status=status.HTTP_201_CREATED)
        else:
            return Response(Quiz.errors,status=status.HTTP_400_BAD_REQUEST)