from rest_framework import serializers
from ...models import Student, Department, Level, User
from ..school_details import LevelSerializer, DepartmentSerializer
from .user_serializer import UserSerializer

class StudentSerializer(serializers.ModelSerializer):
    level = LevelSerializer(read_only=True)
    department = DepartmentSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    department_name = serializers.SlugRelatedField(slug_field = 'name', queryset=Department.objects.all(), write_only=True, source='department')
    level_name = serializers.SlugRelatedField(slug_field = 'name', queryset=Level.objects.all(), write_only=True, source= 'level')
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    first_name = serializers.CharField(write_only=True, required=False)
    last_name = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Student
        fields = ['id', 'user', 'department', 'level', 'department_name', 'level_name', 'username', 'password', 'email', 'first_name', 'last_name', 'matric_number']

    def create(self, validated_data):
        user_data = {
            'username': validated_data.pop('username'),
            'password': validated_data.pop('password'),
            'email': validated_data.pop('email'),
            'first_name': validated_data.pop('first_name', ''),
            'last_name': validated_data.pop('last_name', ''),
            'role': 'student'
        }

        user = User.objects.create_user(**user_data)
        student = Student.objects.create(user=user, **validated_data)

        return student

    def update(self, instance, validated_data):
        user_data = {
            "username" : validated_data.pop('username', None),
            "email" : validated_data.pop('email', None),
            "password" : validated_data.pop('password', None),
            "firstname" : validated_data.pop('firstname', None),
            "lastname" : validated_data.pop('lastname', None)
        }

        user = instance.user
        if user_data:
            for attr,value in user_data.items():
                if value is not None:
                    if attr == "password":
                        user.set_password(value)
                    else:
                        setattr(user, attr, value)
            user.save()
            
        if 'department' in validated_data:
            instance.department = validated_data.pop('department')
        if 'level' in validated_data:
            instance.level = validated_data.pop('level')
        
        for attr,value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance



