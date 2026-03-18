from rest_framework import serializers
from ...models import Performance
from ..school_details.course_serializer import CourseDetailsSerializer
from ..users.student_serializer import StudentSerializer

class PerformanceSerializer(serializers.ModelSerializer):
    course = CourseDetailsSerializer(read_only=True)
    student = StudentSerializer(read_only=True)
    
    class Meta:
        model = Performance
        fields = ['id', 'student','course', 'average_score', 'total_attempts', 'best_score', 'last_attempt_date']