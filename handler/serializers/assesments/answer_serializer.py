from rest_framework import serializers
from ...models import Answer, Option

class AnswerSerializer(serializers.ModelSerializer):
    selected_option = serializers.PrimaryKeyRelatedField(queryset=Option.objects.all(), write_only=True)
    class Meta:
        model = Answer
        fields = ['id', 'is_correct', 'selected_option']
