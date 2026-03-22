from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from ...serializers import AnswerForumSerializer, QuestionFormSerializer
from ...models import QuestionForum, AnswerForum, Course, Student

# Questions forum
@api_view(['GET'])
def get_questions(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    questions = QuestionForum.objects.filter(course=course)

    serializer = QuestionFormSerializer(questions, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_question(request, course_id):
    course = get_object_or_404(
        Course,
        id = course_id
    )
    serializer = QuestionFormSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save(user=request.user, course=course)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PATCH', 'DELETE'])
def question_manager(request, course_id, questfr_id):
    course = get_object_or_404(
        Course,
        id = course_id
    )
    question_asked = get_object_or_404(
        QuestionForum,
        id = questfr_id,
        course = course
    )

    if request.method == 'GET':
        serializer = QuestionFormSerializer(question_asked)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        user = request.user
        if not user == question_asked.user:
            return Response({'error':'You did not make this post'}, status=status.HTTP_403_FORBIDDEN)
         
        serializer = QuestionFormSerializer(question_asked , data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        user = request.user
        if not user == question_asked.user:
            return Response({'error':'You did not make this post'}, status=status.HTTP_403_FORBIDDEN)
        
        question_asked.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Anser Forum

@api_view(['GET'])
def get_answers(request, questfr_id):
    questions = get_object_or_404(
        QuestionForum,
        id = questfr_id
    )
    answer_forum = AnswerForum.objects.filter(question = questions)

    serializer = AnswerForumSerializer(answer_forum, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_answer(request, questfr_id):
    question = get_object_or_404(
        QuestionForum,
        id = questfr_id
    )
    serializer = AnswerForumSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save(user=request.user, question = question)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def answer_manager(request, questfr_id, ansfr_id):
    question_asked = get_object_or_404(
        QuestionForum,
        id = questfr_id
    )

    answer_forum = get_object_or_404(
        AnswerForum,
        id = ansfr_id,
        question = question_asked
    )

    if request.method == 'GET':
        serializer = AnswerForumSerializer(answer_forum)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        user = request.user
        if not user == answer_forum.user:
            return Response({'error':'You did not make this post'}, status=status.HTTP_403_FORBIDDEN)
         
        serializer = AnswerForumSerializer(answer_forum, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        user = request.user
        if not user == answer_forum.user:
            return Response({'error':'You did not make this post'}, status=status.HTTP_403_FORBIDDEN)
        
        answer_forum.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
