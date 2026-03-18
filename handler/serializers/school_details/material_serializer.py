from rest_framework import serializers
from ...models import Material, Topic
from .topic_serializer import TopicSerializer

class MaterialSerializer(serializers.ModelSerializer):
    topic_details = TopicSerializer(read_only=True)
    class Meta:
        model = Material
        fields = ['id', 'title', 'file', 'is_downloadable', 'topic_details']