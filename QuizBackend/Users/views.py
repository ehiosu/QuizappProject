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
from Users.models import Teacher,User,Student
from Quizzes.serializer import QuizSerializer,QuestionSerializer,AnswerSerializer,ResponseSerializer
from rest_framework.views import APIView
from Quizzes.models import Quiz,Question,Answer,response

class CreateTeacher(APIView):
    def post(self,request):
        teacher=TeacherSerializer(data=request.data)
        if teacher.is_valid():
            teacher.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(teacher.errors,status=status.HTTP_400_BAD_REQUEST)
# Create your views here.

class CreateStudent(APIView):
    def post(self,request):
        student=StudentSerializer(data=request.data)
        print(student)
        if student.is_valid():
            student.save()
            return Response(status=status.HTTP_201_CREATED)
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
            return Response(data={"Quizes":QuizSerializer(result,many=True).data},status=status.HTTP_302_FOUND)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class CreateQuestion(APIView):
    def post(self,request):
        quiz=Quiz.objects.get(pk=request.data["Quiz"])
        question=Question.objects.create(Quiz=quiz,question=request.data["question"],image1=request.data["image1"],image2=request.data["image2"],image3=request.data["image3"])
        if question:
            

            resp={"quiz_id":request.data["Quiz"],"Question":question.question,"Question_ID":question.id}
            question.save()
            # resp=JsonResponse(resp)

            # resp= JsonResponse({"id":Quiz.data['id'],"name":Quiz.data["Quiz_name"]})
            # resp = JsonResponse({"message":"done"})
            return Response(data=resp,status=status.HTTP_201_CREATED)
        else:
            return Response(Quiz.errors,status=status.HTTP_400_BAD_REQUEST)


class GetQuizAndQuestionsbyID(APIView):
    def get(self,request,pk):
        QuestionObjs=Question.objects.filter(Quiz=pk).all()
        Data=QuestionSerializer(QuestionObjs,many=True)
        # instigatorObj=Quiz.objects.filter(pk=pk).values()
        #"Quiz":instigatorObj,
        QuestionObjs=({"Questions":list(Data.data)})
        print(QuestionObjs)
        if QuestionObjs:
            return Response(data=QuestionObjs,status=status.HTTP_302_FOUND)
        else:
            return Response(Quiz.errors,status=status.HTTP_400_BAD_REQUEST)

class CreateAnswer(APIView):
    def post(self,request):
        _answer=AnswerSerializer(data=request.data)
        if _answer.is_valid():
            _answer=_answer.save()
            return Response(data={"id":_answer.id,"Answer":_answer.answer,"iscorrect":_answer.IsCorrect},status=status.HTTP_201_CREATED)
        else:
            return Response(_answer.errors,status=status.HTTP_400_BAD_REQUEST)
            
class GetAnswers(APIView):
    def get(self,request,pk):
        answerobjs=Answer.objects.filter(QuestionID=pk)
        answers=[]
        for answer in answerobjs:
            _answer=AnswerSerializer(answer).data
            answers.append(_answer)

        if answers:
            return Response(data={"answers":answers},status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class GetCorrectAnswersByQuestion(APIView):
    def get(self,request,pk):
        questions=Question.objects.filter(Quiz=pk).values('id')
        answers=[]
        for question in questions:
            answers.append(Answer.objects.filter(QuestionID=question['id'],IsCorrect=True).values('id'))
      

        if answers:
            return Response(data={"answers":answers},status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class GetEntireQuiz(APIView):
    def get(self,request,pk):
        print(Question.objects.filter(Quiz=pk).values('id'))
        questions=Question.objects.filter(Quiz=pk).values('id','question','image1','image2','image3')
        quiz=[]
        for question in questions:
            answers = Answer.objects.filter(QuestionID=question['id']).values('id','answer','QuestionID')
            obj={"question":question,"answers":answers}
            quiz.append(obj)

        if quiz:
            return Response(data=quiz,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)

class SubmitQuiz(APIView):
    def post(self,request):
        resp=ResponseSerializer(data=request.data)
        if  resp.is_valid():
            resp.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class getResposesForQuizT(APIView):
    def get(self,request,id):
        users=response.objects.filter(quiz=id).values()
        print(users)
        _response=[]
        for user in users:
            username=Student.objects.filter(id=user['student_id']).values('username','first_name','last_name').first()
            resp ={"username":username,"score":user["score"]}
            _response.append(resp)
        if _response:
            return Response(data=_response,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
            
