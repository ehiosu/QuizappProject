from django.contrib import admin
from django.urls import path
from Users.views import CreateTeacher,CreateStudent,getTeachers,CreateQuiz,getQuizById,CreateQuestion,GetQuizAndQuestionsbyID,CreateAnswer,GetAnswers,GetCorrectAnswersByQuestion,GetEntireQuiz,SubmitQuiz,getResposesForQuizT,RegisterTeacher,checkUser,Login,Logout,enroll,GetEnrolledTeeachers
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
urlpatterns = [
    path("CreateTeacher/", RegisterTeacher.as_view()),
    path("CreateStudent/",CreateStudent.as_view()),
    path("getTeachers/",getTeachers.as_view()),
    path("createquiz/",CreateQuiz.as_view()),
    path("getQuiz/<int:pk>",getQuizById.as_view()),
    path("CreateQuestion/",CreateQuestion.as_view()),
    path("GetQuizandQuestions/<int:pk>",GetQuizAndQuestionsbyID.as_view()),
    path("CreateAnswer/",CreateAnswer.as_view()),
    path("GetAnswers/<int:pk>",GetAnswers.as_view()),
    path("GetCorrectAnswers/<int:pk>",GetCorrectAnswersByQuestion.as_view()),
     path("GetQuiz/<int:pk>",GetEntireQuiz.as_view()),
     path("Submit/",SubmitQuiz.as_view()),
     path("responses/<int:id>",getResposesForQuizT.as_view()),
     path("auth/Login",Login.as_view()),
     path("auth/refresh-token",TokenRefreshView.as_view()),
     path("auth/User",checkUser.as_view()),
     path("auth/Logout",Logout.as_view()),
     path("auth/enroll",enroll.as_view()),
     path("auth/get",GetEnrolledTeeachers.as_view())
]
