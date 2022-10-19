from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN="ADMIN",'Admin'
        STUDENT="STUDENT",'student'
        TEACHER="TEACHER",'Teacher'
    base_role=Role.ADMIN

    role=models.CharField(max_length=50,choices=Role.choices,blank=True)
    profile=models.TextField(max_length=1000,blank=True)


    def save(self,*arg,**kwargs):
        if not self.pk:
            self.role=self.base_role

 
           
            
            # self.set_password(self, *arg["password"])
            return super().save(*arg,**kwargs)



class TeacherManager(UserManager):
    def get_queryset(self,*args,**kwargs):
        result = super().get_queryset(*args,**kwargs)
        return result.filter(role=User.Role.TEACHER)

class Teacher(User):
    base_role=User.Role.TEACHER
    teacher= TeacherManager()

    class Meta:
        proxy:True
class Student(User):
    base_role=User.Role.STUDENT
    Teachers = models.ManyToManyField(Teacher)
class StudentManager(UserManager):
     def get_queryset(self,*args,**kwargs):
        result = super().get_queryset(*args,**kwargs)
        return result.filter(role=User.Role.STUDENT)


class Room(models.Model):
    RoomName=models.CharField(max_length=250)
    RoomDescription=models.TextField(max_length=1000)
    Owner=models.OneToOneField(Teacher,  on_delete=models.CASCADE)
    Students=models.ManyToManyField(Student)

    def __str__(self):
        return self.RoomName
    
# Create your models here.
