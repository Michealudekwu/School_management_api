from rest_framework import serializers
from ...models import Course, Teacher
from ..users import TeacherSerializer
from .department_serializer import DepartmentSerializer 
from .level_serializer import LevelSerializer

class CourseDetailsSerializer(serializers.ModelSerializer):
    teacher_id = serializers.PrimaryKeyRelatedField(source='teacher', queryset= Teacher.objects.all(), write_only=True)
    teacher = TeacherSerializer(read_only=True)

    department = DepartmentSerializer(read_only = True)
    level = LevelSerializer(read_only = True)

    class Meta:
        model = Course
        fields = ['id', 'code','title', 'semester','department', 'level', 'teacher', 'teacher_id']