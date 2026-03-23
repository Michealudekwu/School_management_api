from rest_framework import serializers
from ...models import Teacher, Department, Level, User
from ..school_details import LevelSerializer, DepartmentSerializer
from .user_serializer import UserSerializer

class TeacherSerializer(serializers.ModelSerializer):
    level = LevelSerializer(read_only=True, many=True)
    department = DepartmentSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    department_name = serializers.SlugRelatedField(slug_field='name', queryset=Department.objects.all(), write_only=True, source= "department")
    level_name = serializers.SlugRelatedField(slug_field='name', queryset=Level.objects.all(), write_only=True, source = "level", many=True)
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    first_name = serializers.CharField(write_only=True, required=False)
    last_name = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Teacher
        fields = ['id', 'staff_id','user', 'department_name', 'level_name', 'department', 'level', 'username', 'password', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        # print(validated_data)
        user_data = {
            'username': validated_data.pop('username'),
            'password': validated_data.pop('password'),
            'email': validated_data.pop('email'),
            'first_name': validated_data.pop('first_name', ''),
            'last_name': validated_data.pop('last_name', ''),
            'role': 'teacher'
        }

        user = User.objects.create_user(**user_data)
        levels = validated_data.pop('level', [])
        teacher = Teacher.objects.create(user=user, **validated_data)
        if levels:
            teacher.level.set(levels)
        return teacher
    
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

        level = validated_data.pop('level', None)
        if 'department' in validated_data:
            instance.department = validated_data.pop('department')
        if level is not None:
            instance.level.set(level)
        
        for attr,value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance