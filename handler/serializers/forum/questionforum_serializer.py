from rest_framework import serializers
from ...models import QuestionForum
from ..users import UserSerializer

class QuestionFormSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = QuestionForum
        fields = ['id', 'user','title', 'body', 'created_at']