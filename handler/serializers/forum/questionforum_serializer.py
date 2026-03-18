from rest_framework import serializers
from ...models import QuestionForum

class QuestionFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionForum
        fields = ['id', 'user', 'course', 'title', 'body', 'created_at']