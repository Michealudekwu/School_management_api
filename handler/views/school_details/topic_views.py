from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from ..users import IsTeacher
from rest_framework.response import Response
from rest_framework import status 
from django.shortcuts import get_object_or_404
from ...models import Topic, Progress, Course
from ...serializers import TopicSerializer

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def all_topics(request, course_id):
    topics = Topic.objects.filter(course=course_id)
    if topics:
        Progress.objects.get_or_create(
            user=request.user,
            course_id=course_id,
            total_topics=topics.count(),
            completed_topics=0,
            progress_percentage=0.0
        )
        serializer = TopicSerializer(topics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'error': 'No topics in the DB'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def completed_topic(request, course_id, tp_id):
    try:
        progress = Progress.objects.get(user=request.user, course_id=course_id)
    except Progress.DoesNotExist:
        return Response({'error': 'Progress record not found'}, status=status.HTTP_404_NOT_FOUND)

    topic = get_object_or_404(
        Topic,
        id = tp_id,
        course_id=course_id
    )
    if topic in progress.completed_topics.all():
        return Response({'detail': 'Topic already marked as completed'}, status=status.HTTP_400_BAD_REQUEST)

    progress.completed_topics.add(topic)
    progress.progress_percentage = (progress.completed_topics.count() / progress.total_topics) * 100
    progress.save()

    return Response({'detail': 'Topic marked as completed', 'progress_percentage': progress.progress_percentage}, status=status.HTTP_200_OK)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsTeacher])
def create_topic(request, course_id):
    course = Course.objects.get(id=course_id)
    serializer = TopicSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save(course = course)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_topic(request, course_id,tp_id):
    Topic = get_object_or_404(
        Topic,
        id = tp_id,
        course_id = course_id
    )
    if Topic:
        serializer = TopicSerializer(Topic)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'error':'Topic Not Exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PATCH'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsTeacher])
def update_topic(request, course_id, tp_id):
    Topic = get_object_or_404(
        Topic,
        id = tp_id,
        course_id = course_id
    )
    if Topic:
        serializer = TopicSerializer(Topic, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'error': 'Topic not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated, IsTeacher])
def delete_topic(request, course_id,tp_id):
    Topic = get_object_or_404(
        Topic,
        id = tp_id,
        course_id = course_id
    )
    if Topic:
        Topic.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response({'error': 'Topic not found'}, status=status.HTTP_404_NOT_FOUND)

    