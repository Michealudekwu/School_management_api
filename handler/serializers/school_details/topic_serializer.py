from rest_framework import serializers
from ...models import Topic, Course
from .course_serializer import CourseDetailsSerializer

class TopicSerializer(serializers.ModelSerializer):
    course_details = CourseDetailsSerializer(read_only=True)

    class Meta:
        model = Topic
        fields = ['id', 'name', 'course_details']