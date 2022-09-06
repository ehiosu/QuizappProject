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

from Users.serializer import TeacherSerializer,StudentSerializer,UserSerializer
from Users.models import Teacher,User
from Quizzes.serializer import QuizSerializer,QuestionSerializer,AnswerSerializer
from rest_framework.views import APIView
from Quizzes.models import Quiz,Question,Answer

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
         _user=User.objects.get(pk=request.data['teacher'])
         #new_user=UserSerializer(_user).data
         new_Quiz=Quiz.objects.create(Name=request.data["Name"],teacher=_user)

         if new_Quiz:
            new_Quiz.save()
            quizobj=QuizSerializer(new_Quiz)
            teacher=User.objects.get(pk=request.data["teacher"])
            teacherOBJ=UserSerializer(teacher).data
            teacher={"teacherID":teacherOBJ["id"],"teacherEmail":teacherOBJ["email"],"teacherusername":teacherOBJ["username"]}
            resp = {"QuizID":quizobj.data["id"],"QuizName":quizobj.data["Name"],"Teacher":teacher}
            return(Response(data=resp,status=status.HTTP_201_CREATED))
         else:
            return(Response(status=status.HTTP_400_BAD_REQUEST))
          
          
class getQuizById(APIView):
    def get(self,request,pk):
        result =Quiz.objects.filter(teacher=pk).all()
        print(result)
        if (result):
            return Response(data={"Quizes":QuizSerializer(result,many=True).data},status=status.HTTP_200_OK)
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


class GetQuizAndQuestionsbyID(APIView):
    def get(self,request,pk):
        QuestionObjs=Question.objects.filter(quiz_id=pk).select_related('quiz_id').all()
        Data=QuestionSerializer(QuestionObjs,many=True)
        # instigatorObj=Quiz.objects.filter(pk=pk).values()
        #"Quiz":instigatorObj,
        QuestionObjs=({"Questions":list(Data.data)})
        print(QuestionObjs)
        if QuestionObjs:
            return Response(data=QuestionObjs,status=status.HTTP_201_CREATED)
        else:
            return Response(Quiz.errors,status=status.HTTP_400_BAD_REQUEST)
