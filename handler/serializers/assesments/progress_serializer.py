from rest_framework import serializers
from ...models import Progress, User, Course

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = ['id', 'completed_topics', 'total_topics', 'progress_percentage']