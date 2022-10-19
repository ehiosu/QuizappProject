from  rest_framework import serializers
from Users.models import Teacher,Student,User

class TeacherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Teacher
        fields=["id","username","first_name","last_name","email","role"]
      

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
        fields=["id","username","first_name","last_name","email","role","Teachers"]
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
        
    
class TeacherRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50,min_length=6)
    username=serializers.CharField(max_length=50,min_length=3)
    password=serializers.CharField(max_length=150,write_only=True)
    class Meta:
        model=Teacher
        fields=["id","username","password","email","first_name","last_name"]

    def validate(self, attrs):
        email=attrs.get("email",None)
        password=attrs.get("password",None)
        username=attrs.get("username",None)

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email':"Email has already been registered"})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username':"Email has already been registered"})
        return super().validate(attrs)
    def create(self, validated_data):
        return Teacher.objects.create_user(**validated_data)

class StudentRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=50,min_length=6)
    username=serializers.CharField(max_length=50,min_length=3)
    password=serializers.CharField(max_length=150,write_only=True)

    teacher=serializers.CharField(max_length=4)
    class Meta:
        model=Student
        fields=["id","username","password","email","first_name","last_name","teacher"]

    def validate(self, attrs):
        email=attrs.get("email",None)
        password=attrs.get("password",None)
        username=attrs.get("username",None)

        if User.objects.filter(email=email).exists():
            print("error")
            raise serializers.ValidationError({'email':"Email has already been registered"})
        if User.objects.filter(username=username).exists():
            print("error")
            raise serializers.ValidationError({'username':"Email has already been registered"})
        return super().validate(attrs)

        #def create(self, validated_data):
        #    return Student.objects.create_user(**validated_data)

  

    def update(self, instance, validated_data):
        import pdb; pdb.set_trace()
        teachers= validated_data.pop('Teachers',[])
        instance=super(StudentRegistrationSerializer,self).update(instance, validated_data)
        for teacher in teachers:
            print("checking for teachers")
            teachibj=Teacher.objects.get(id=teacher)
            if teachibj.exists():
                teach=teachibj.first()
                instance.Teachers.add(teach)
        instance.save()
        return instance

    def save(self):
            user=Student(
                email=self.validated_data['email'],
                password=self.validated_data['password'],
                username=self.validated_data['username'],
                first_name=self.validated_data['first_name'],
                last_name=self.validated_data['last_name']
                
            )
         
            password=self.validated_data['password']
            teacher=self.validated_data["teacher"]
           
           
            user.set_password(password)
            user.save()
            if teacher:
                teacher=Teacher.objects.get(id=teacher)
                user.Teachers.add(teacher)
            return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["email","username","first_name","last_name","id","profile"]

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields="__all__"


class studentteacherserializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=["Teachers"]
        