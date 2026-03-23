from rest_framework import serializers
from ...models import Exam

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'exam_type','title', 'duration_mins', 'total_marks', 'created_at']