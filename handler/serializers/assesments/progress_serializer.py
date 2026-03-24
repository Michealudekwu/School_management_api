from rest_framework import serializers
from ...models import Progress
from ..school_details import CourseDetailsSerializer

class ProgressSerializer(serializers.ModelSerializer):
    course = CourseDetailsSerializer(read_only=True)
    class Meta:
        model = Progress
        fields = ['id', 'course','completed_topics', 'total_topics', 'progress_percentage']