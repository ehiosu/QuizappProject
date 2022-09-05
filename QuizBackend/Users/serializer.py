from rest_framework import serializers
from Users.models import Teacher,Student,Base_User,User


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields="__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"

class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Base_User
        fields="__all__"

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields="__all__"