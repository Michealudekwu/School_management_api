from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ...models import Exam, Question, Course
from ...serializers import QuestionSerializer, ExamSerializer

@api_view(['GET', 'POST'])
def exam_list_create(request, level_id, department_id,course_id):
    try:
        course = get_object_or_404(
            Course,
            id = course_id,
            level_id = level_id,
            department_id = department_id
        )
        
    except Course.DoesNotExist:
        return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        exams = Exam.objects.filter(
            course=course
        )
        serializer = ExamSerializer(exams, many=True)
        return Response(serializer.data)

    elif request.method == 'POST' and request.user.role == 'teacher':
        serializer = ExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(course = course)  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def exam_detail(request, course_id,exam_id):
    exam = get_object_or_404(
            Exam,
            id = exam_id,
            course_id=course_id
        )

    if request.method == 'GET':
        serializer = ExamSerializer(exam)
        return Response(serializer.data)

    elif request.method == 'PUT' and request.user.role == 'teacher':
        serializer = ExamSerializer(exam, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE' and request.user.role == 'teacher':
        exam.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def exam_questions_list_create(request, course_id,exam_id):
    try:
        exam = get_object_or_404(
            Exam,
            id = exam_id,
            course_id = course_id
        )

    except Exam.DoesNotExist:
        return Response({"error": "Exam not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        questions = Question.objects.filter(exam=exam)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST' and request.user.role == 'teacher':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(exam=exam)  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PATCH', 'DELETE'])
def exam_question_detail(request, course_id, exam_id, question_id):
    try:
        question = get_object_or_404(
            Question,
            id = question_id,
            exam_id = exam_id,
            exam__course_id = course_id
        )
    except Question.DoesNotExist:
        return Response({"error": "Question not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    elif request.method == 'PATCH' and request.user.role == 'teacher':
        serializer = QuestionSerializer(question, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE' and request.user.role == 'teacher':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)