from rest_framework import serializers
from ...models import QuestionForum
from ..users import UserSerializer
from ..school_details import CourseDetailsSerializer

class QuestionFormSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    course = CourseDetailsSerializer(read_only = True)
    class Meta:
        model = QuestionForum
        fields = ['id', 'user','title', 'body', 'course', 'created_at']