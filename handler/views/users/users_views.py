from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from ...models import Student, Teacher, Performance, User
from ...serializers import StudentSerializer, TeacherSerializer, PerformanceSerializer
from .role_auth import IsStudent, IsTeacher, IsMe

@api_view(['POST'])
@permission_classes([AllowAny])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def create_teacher(request):
    serializer = TeacherSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsStudent])
@api_view(['PATCH'])
def update_student(request):
    student = Student.objects.get(user = request.user)

    serializer = StudentSerializer(student,data= request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsTeacher])
@api_view(['PATCH'])
def update_teahcer(request):
    teacher = Teacher.objects.get(user = request.user)

    serializer = TeacherSerializer(teacher, data= request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsStudent])
@api_view(['DELETE'])
def delete_student(request):
    student = Student.objects.get(user = request.user)
    student.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@permission_classes([IsTeacher])
@api_view(['DELETE'])
def delete_teacher(request):
    teacher = Teacher.objects.get(user = request.user)
    teacher.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_user_details(request):
    user = request.user
    if hasattr(user, 'student_profile'):
        student = user.student_profile
        # performace = Performance.objects.filter(student=student)
        # per_serializer = PerformanceSerializer(performace)
        stud_serializer = StudentSerializer(student)
        return Response(stud_serializer.data)
    elif hasattr(user, 'teacher_profile'):
        serializer = TeacherSerializer(user.teacher_profile)
        return Response(serializer.data)
    else:
        return Response({'error': 'User details not found'}, status=status.HTTP_404_NOT_FOUND)
    
@permission_classes([IsMe])
@api_view(['POST'])
def make_admin(request, user_id):
    user = get_object_or_404(
        User,
        id = user_id
    )
    user.is_staff = True
    user.save()

    return Response({'message' : f'User {user.username} made admin'}, status=status.HTTP_200_OK)
    
