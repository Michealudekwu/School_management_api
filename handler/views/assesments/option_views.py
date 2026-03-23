from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ...models import Option, Question
from ...serializers import OptionSerializer

@api_view(['GET', 'POST'])
def option_list_create(request, exam_id,question_id, course_id):
    question = get_object_or_404(
            Question,
            id = question_id,
            exam_id = exam_id,
            exam__course_id = course_id
        )

    if request.method == 'GET':
        options = Option.objects.filter(question=question)
        serializer = OptionSerializer(options, many=True)
        return Response(serializer.data)

    elif request.method == 'POST' and request.user.role == 'teacher':
        serializer = OptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(question=question)  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def option_detail(request, question_id,option_id, exam_id, course_id):
    option = get_object_or_404(
            Option,
            id = option_id,
            question_id = question_id,
            question__exam_id = exam_id,
            question__exam__course_id = course_id
        )

    if request.method == 'GET':
        serializer = OptionSerializer(option)
        return Response(serializer.data)

    elif request.method == 'PATCH' and request.user.role == 'teacher':
        serializer = OptionSerializer(option, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE' and request.user.role == 'teacher':
        option.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
