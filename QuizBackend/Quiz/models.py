from django.db import models
from Users.models import Teacher
# Create your models here.

class Quiz(models.Model):
    Name=models.CharField(max_length=100)
    Creator=models.ForeignKey(Teacher, on_delete=models.CASCADE)
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 
