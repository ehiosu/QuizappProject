from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Base_User(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    Profile_Pic= models.URLField(blank=True)


    def __str__(self):
        return self.user.username

class Teacher(models.Model):
    user = models.OneToOneField(Base_User, on_delete=models.CASCADE) 
    def __str__(self):
        return self.user.user.username
    

class Student(models.Model):
    user = models.OneToOneField(Base_User(),  on_delete=models.CASCADE)
    Registered_Teachers=models.ManyToManyField(Teacher,blank=True)
    
    def __str__(self):
        return self.user.user.username
    