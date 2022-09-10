from django.db import models
from Users.models import Teacher,Student,User

class Quiz(models.Model):
    Name=models.CharField(max_length=255,unique=True)
    teacher=models.ForeignKey(User, on_delete=models.CASCADE,default="15")
    
   
    
class Question(models.Model):
    question=models.TextField(max_length=500)
    Quiz=models.ForeignKey(Quiz, on_delete=models.CASCADE,default="1")
    image1=models.URLField(blank=True,null=True)
    image2=models.URLField(blank=True,null=True)
    image3=models.URLField(blank=True,null=True)

class Answer(models.Model):
    IsCorrect= models.BooleanField()
    QuestionID=models.ForeignKey(Question, on_delete=models.CASCADE)
    answer=models.TextField(max_length=500)

    def __str__(self):
        return self.answer

class response(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    score=models.CharField(max_length=10)
    quiz=models.ForeignKey(Quiz, on_delete=models.SET_NULL,null=True,blank=True)
    



# Create your models here.
