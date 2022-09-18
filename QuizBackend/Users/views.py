from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from django.http import JsonResponse
import jwt
from rest_framework_simplejwt import authentication
import datetime
import uuid
from  rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken
from rest_framework.decorators import api_view, permission_classes
from Users.serializer import TeacherSerializer,StudentSerializer,UserSerializer,TeacherRegistrationSerializer,StudentRegistrationSerializer,UserProfileSerializer,StudentProfileSerializer,studentteacherserializer
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
        student=StudentRegistrationSerializer(data=request.data)
        
        if student.is_valid():
            student.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(student.errors,status=status.HTTP_400_BAD_REQUEST)

class getTeachers(APIView):
    def get(self,request):
        token = request.COOKIES.get('jwt')
        if not token:
            print("not token")
            raise AuthenticationFailed('Unauthenticated')
        try:
            payload =jwt.decode(token,'secret',algorithms=['HS256'])
            print(payload)
           
        except:
            raise AuthenticationFailed('Unauthenticated')

        users=User.objects.filter(role=User.Role.TEACHER).values('id','username','email')
        return  JsonResponse({"data":list(users)})

class CreateQuiz(APIView):
    def post(self,request):
        token = request.COOKIES.get('jwt')
        if not token:
            print("not token")
            raise AuthenticationFailed('Unauthenticated')
        try:
            payload =jwt.decode(token,'secret',algorithms=['HS256'])
            print(payload['id'])
           
        except:
            raise AuthenticationFailed('Unauthenticated')
        _user=User.objects.get(id=payload['id'])
         #new_user=UserSerializer(_user).data
        new_Quiz=Quiz.objects.create(Name=request.data["Name"],teacher=_user)

        if new_Quiz:
            new_Quiz.save()
            quizobj=QuizSerializer(new_Quiz)
            teacher=User.objects.get(id=payload["id"])
            teacherOBJ=UserSerializer(teacher).data
            teacher={"teacherID":teacherOBJ["id"],"teacherEmail":teacherOBJ["email"],"teacherusername":teacherOBJ["username"]}
            resp = {"QuizID":quizobj.data["id"],"QuizName":quizobj.data["Name"],"Teacher":teacher}
            return(Response(data=resp,status=status.HTTP_201_CREATED))
        else:
            return(Response(status=status.HTTP_400_BAD_REQUEST))
          
          
class getQuizById(APIView):
    def get(self,request,pk):
        token = request.COOKIES.get('jwt')
        if not token:
            print("not token")
            raise AuthenticationFailed('Unauthenticated')
        try:
            payload =jwt.decode(token,'secret',algorithms=['HS256'])
            print(payload)
           
        except:
            raise AuthenticationFailed('Unauthenticated')
        result =Quiz.objects.filter(teacher=pk).values()
        data=[]
       

        print(result)
        if (result):
            return Response(data={"Quizes":result},status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class CreateQuestion(APIView):
    def post(self,request):
        token = request.COOKIES.get('jwt')
        if not token:
            print("not token")
            raise AuthenticationFailed('Unauthenticated')
        try:
            payload =jwt.decode(token,'secret',algorithms=['HS256'])
            print(payload)
           
        except:
            raise AuthenticationFailed('Unauthenticated')
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
         token = request.COOKIES.get('jwt')
         if not token:
            print("not token")
            raise AuthenticationFailed('Unauthenticated')
         try:
            payload =jwt.decode(token,'secret',algorithms=['HS256'])
            print(payload)
           
         except:
            raise AuthenticationFailed('Unauthenticated')
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
        token = request.COOKIES.get('jwt')
        if not token:
            print("not token")
            raise AuthenticationFailed('Unauthenticated')
        try:
            payload =jwt.decode(token,'secret',algorithms=['HS256'])
            print(payload)
           
        except:
            raise AuthenticationFailed('Unauthenticated')
        _answer=AnswerSerializer(data=request.data)
        if _answer.is_valid():
            _answer=_answer.save()
            return Response(data={"id":_answer.id,"Answer":_answer.answer,"iscorrect":_answer.IsCorrect},status=status.HTTP_201_CREATED)
        else:
            return Response(_answer.errors,status=status.HTTP_400_BAD_REQUEST)
            
class GetAnswers(APIView):
    def get(self,request,pk):
         token = request.COOKIES.get('jwt')
         if not token:
            print("not token")
            raise AuthenticationFailed('Unauthenticated')
         try:
            payload =jwt.decode(token,'secret',algorithms=['HS256'])
            print(payload)
           
         except:
            raise AuthenticationFailed('Unauthenticated')
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
         token = request.COOKIES.get('jwt')
         if not token:
            print("not token")
            raise AuthenticationFailed('Unauthenticated')
         try:
            payload =jwt.decode(token,'secret',algorithms=['HS256'])
            print(payload)
           
         except:
            raise AuthenticationFailed('Unauthenticated')
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
         token = request.COOKIES.get('jwt')
         if not token:
            print("not token")
            raise AuthenticationFailed('Unauthenticated')
         try:
            payload =jwt.decode(token,'secret',algorithms=['HS256'])
            print(payload)
           
         except:
            raise AuthenticationFailed('Unauthenticated')
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
         token = request.COOKIES.get('jwt')
         if not token:
            print("not token")
            raise AuthenticationFailed('Unauthenticated')
         try:
            payload =jwt.decode(token,'secret',algorithms=['HS256'])
            print(payload)
           
         except:
            raise AuthenticationFailed('Unauthenticated')
         resp=ResponseSerializer(data=request.data)
         if  resp.is_valid():
            resp.save()
            return Response(status=status.HTTP_200_OK)
         else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class getResposesForQuizT(APIView):
    def get(self,request,id):
         token = request.COOKIES.get('jwt')
         if not token:
            print("not token")
            raise AuthenticationFailed('Unauthenticated')
         try:
            payload =jwt.decode(token,'secret',algorithms=['HS256'])
          
         except:
            raise AuthenticationFailed('Unauthenticated')
         users=response.objects.filter(quiz=id).values()
       
         _response=[]
         for user in users:
            username=Student.objects.filter(id=user['student_id']).values('username','first_name','last_name').first()
            resp ={"username":username,"score":user["score"]}
            _response.append(resp)
         if _response:
            return Response(data=_response,status=status.HTTP_200_OK)
         else:
            return Response(status=status.HTTP_204_NO_CONTENT)

class RegisterTeacher(generics.GenericAPIView):
    serializer_class=TeacherRegistrationSerializer

    def post(self,request):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data={"uuid":str(uuid.uuid4()),"message":"User Created Successfully.","user":serializer.data},status=status.HTTP_201_CREATED)
        else:
            return Response(data={"errors":serializer.errors},status=status.HTTP_400_BAD_REQUEST)

class RegisterStudent(generics.GenericAPIView):
    serializer_class=StudentRegistrationSerializer

    def post(self,request):
        studentserialized=self.get_serializer(data=request.data)
        if studentserialized.is_valid(raise_exception=True):
            test=studentserialized.save()
            print("serializer valid")
            return Response(data={"uuid":str(uuid.uuid4()),"message":"User Created Successfully.","user":studentserialized.data},status=status.HTTP_201_CREATED)
        else:
            print("serializer invalid")
            return Response(data={"errors":serializer.errors},status=status.HTTP_400_BAD_REQUEST)    
            

class checkUser(APIView):
    def get(self,request):
        token = request.COOKIES.get('jwt')
        if not token:
            print("not token")
            raise AuthenticationFailed('Unauthenticated')
        try:
            payload =jwt.decode(token,'secret',algorithms=['HS256'])
            print(payload)
           
        except:
            raise AuthenticationFailed('Unauthenticated')
        user = payload['id']
        user=User.objects.get(id=user)
        if user:
            user=UserProfileSerializer(user).data
            resp={"user":user}
            return Response(data=resp,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class Login(APIView):
    def post(self, request):
        email = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=email).first() 

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow(),
            "username":user.username,
            "first_name":user.first_name,
            "last_name":user.last_name,
            "role":user.role
        }
        print(payload)
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        
        return response
    
class Logout(APIView):
    def post(self,request):
        resp = Response()
        resp.delete_cookie('jwt')
        resp.data={
            'message':"success"
        }
        return resp
class enroll(APIView):
    def put(self,request):
        token = request.COOKIES.get('jwt')
        if not token:
            print("not token")
            raise AuthenticationFailed('Unauthenticated')
        try:
            payload =jwt.decode(token,'secret',algorithms=['HS256'])
            print(payload)
           
        except:
            raise AuthenticationFailed('Unauthenticated')
        user = payload['id']
        user=Student.objects.get(id=user)
        
        teacher=request.data['Teachers']
        print(teacher)
        if user:
            for teacher in request.data["Teachers"]:
                teacherobj=Teacher.objects.get(id=teacher)
                if  teacherobj:
                    print("Teacher Object")
                    user.Teachers.add(teacherobj)
            user.save()
        
            return Response(data={"teachers":teachers},status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class GetEnrolledTeeachers(APIView):
    def get(self,request):
         token = request.COOKIES.get('jwt')
         if not token:
            print("not token")
            raise AuthenticationFailed('Unauthenticated')
         try:
            payload =jwt.decode(token,'secret',algorithms=['HS256'])
            print(payload)
           
         except:
            raise AuthenticationFailed('Unauthenticated')
         user = payload['id']
         user= Student.objects.get(id=user) 
         Teachers=studentteacherserializer(user).data["Teachers"]
         if user:
                teachers=[]
                for teacher in Teachers:
                    teacherobj=Teacher.objects.get(id=teacher)
                    teacherobj=UserProfileSerializer(teacherobj).data
                    teachers.append(teacherobj)

                return Response(data={"Teachers":teachers},status=status.HTTP_200_OK)
         else:
             return Response(status=status.HTTP_400_BAD_REQUEST)


