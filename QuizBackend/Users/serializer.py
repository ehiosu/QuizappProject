from  rest_framework import serializers
from Users.models import Teacher,Student,User

class TeacherSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(write_only=True)
    class Meta:
        model= Teacher
        fields=["id","password","password2","username","first_name","last_name","email","role"]
        extra_kwargs={
            'password':{'write_only':True}
        }

    def save(self):
        user=Teacher(
            email=self.validated_data['email'],
            password=self.validated_data['password'],
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name']
            
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']

        if password!=password2:
            raise serializers.ValidationError({"password":"passwords don't match"})
        
        user.set_password(password)
        user.save()
        return user
       
            

        
            
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Student
        fields=["id","password","username","first_name","last_name","email","role","Teachers"]
        depth=1
        extra_kwargs={
            'password':{'write_only':True}
        }

        def save(self):
            password2=self.validated_data.pop('confirm',None)
            user=Student(
                email=self.validated_data['email'],
                password=self.validated_data['password'],
                username=self.validated_data['username'],
                first_name=self.validated_data['first_name'],
                last_name=self.validated_data['last_name']
                
            )
            password=self.validated_data['password']
           
           
            user.set_password(password)
            user.save()
            return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"
        