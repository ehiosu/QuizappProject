from django.contrib import admin
from django.urls import path
from Users.views import CreateTeacher,CreateStudent,getTeachers,CreateQuiz,getQuizById,CreateQuestion
urlpatterns = [
    path("CreateTeacher/", CreateTeacher.as_view()),
    path("CreateStudent/",CreateStudent.as_view()),
    path("getTeachers/",getTeachers.as_view()),
    path("createquiz/",CreateQuiz.as_view()),
    path("getQuiz/<int:pk>",getQuizById.as_view()),
    path("CreateQuestion/",CreateQuestion.as_view())
]
