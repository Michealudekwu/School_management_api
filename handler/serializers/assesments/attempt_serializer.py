from rest_framework import serializers
from ...models import Attempt
from ...models import User, Exam

class AttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attempt
        fields = ['id', 'score', 'start_time', 'end_time', 'is_submitted']
