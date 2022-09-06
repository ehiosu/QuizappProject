from  rest_framework import serializers
from Quizzes.models import Quiz,Answer,Question



class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model=Quiz
        fields="__all__"
      
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Answer
        fields= "__all__"
        depth = 1
        
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields="__all__"
        depth = 1


