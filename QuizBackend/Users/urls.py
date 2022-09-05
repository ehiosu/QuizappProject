from django.contrib import admin
from django.urls import path
from Users.views import CreateTeacher,CreateStudent,getTeachers
urlpatterns = [
    path("CreateTeacher/", CreateTeacher.as_view()),
    path("CreateStudent/",CreateStudent.as_view()),
    path("getTeachers/",getTeachers.as_view())
]
