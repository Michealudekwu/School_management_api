from rest_framework import serializers
from ...models import AnswerForum
from .questionforum_serializer import QuestionFormSerializer

class AnswerForumSerializer(serializers.ModelSerializer):
    question = QuestionFormSerializer(read_only=True)
    class Meta:
        model = AnswerForum
        fields = ['id', 'user', 'question', 'answer', 'created_at']