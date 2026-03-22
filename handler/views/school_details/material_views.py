from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status 
from django.shortcuts import get_object_or_404
from ...models import Material, Topic
from ...serializers import MaterialSerializer
from ..users import IsTeacher

@api_view(['GET'])
def all_materials(requests, tp_id):
    materials = Material.objects.filter(topic=tp_id)
    if materials:
        serializer = MaterialSerializer(materials, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'error': 'No materials in the DB'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsTeacher])
def create_materials(request, course_id,tp_id):
    topic = get_object_or_404(
        Topic,
        id=tp_id,
        course_id=course_id
    )

    serializer = MaterialSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save(topic=topic)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_material(request, tp_id,mat_id):
    material = get_object_or_404(
        Material,
        id=mat_id,
        topic_id = tp_id
    )
    if material:
        serializer = MaterialSerializer(material)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'error':'Material Not Exist'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PATCH'])
@permission_classes([IsTeacher])
def update_material(request, tp_id,mat_id):
    material = get_object_or_404(
        Material,
        id=mat_id,
        topic_id = tp_id
    )
    if material:
        serializer = MaterialSerializer(material, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'error': 'Material not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsTeacher])
def delete_material(request, tp_id,mat_id):
    material = get_object_or_404(
        Material,
        id=mat_id,
        topic_id=tp_id
    )
    if material:
        material.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    return Response({'error': 'Material not found'}, status=status.HTTP_404_NOT_FOUND)

    