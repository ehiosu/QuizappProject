from django.db import models
from Users.models import Teacher
class Quiz(models.Model):
    Organizer= models.ForeignKey(Teacher, on_delete=models.CASCADE)
    
class Question(models.Model):
    question = models.TextField()
    quiz_id = models.ForeignKey(Quiz,on_delete=models.CASCADE)
    Image1 = models.URLField(blank=True)
    Image2 = models.URLField(blank=True)
    Image3 = models.URLField(blank=True)

    def __str__(self):
        return self.question

class Answer(models.Model):
    IsCorrect= models.BooleanField()
    QuestionID=models.ForeignKey(Question, on_delete=models.CASCADE)
    Answer=models.TextField(max_length=500)

    def __str__(self):
        return self.Answer
    



# Create your models here.
