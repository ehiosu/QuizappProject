from django.db import models
from Users.models import Teacher,Student,User

class Quiz(models.Model):
    Name=models.CharField(max_length=255,unique=True)
    teacher=models.ForeignKey(User, on_delete=models.CASCADE,default="15")
    
   
    
class Question(models.Model):
    question=models.TextField(max_length=500)
    Quiz=models.ForeignKey(User, on_delete=models.CASCADE,default="1")
    image1=models.URLField(null=True)
    image2=models.URLField(null=True)
    image3=models.URLField(null=True)

class Answer(models.Model):
    IsCorrect= models.BooleanField()
    QuestionID=models.ForeignKey(Question, on_delete=models.CASCADE)
    Answer=models.TextField(max_length=500)

    def __str__(self):
        return self.Answer
    



# Create your models here.
