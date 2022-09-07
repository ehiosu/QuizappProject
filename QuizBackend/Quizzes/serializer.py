from  rest_framework import serializers
from Quizzes.models import Quiz,Answer,Question,response



class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model=Quiz
        fields="__all__"
      
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Answer
        fields= "__all__"
        
        
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Question
        fields="__all__"
        depth = 1
class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model=response
        fields="__all__"

