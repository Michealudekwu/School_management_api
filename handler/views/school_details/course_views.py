from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from ..users import IsTeacher
from rest_framework import status
from django.shortcuts import get_object_or_404
from ...models import Course, Department, Level, Teacher, Enrollment, Student
from ...serializers import CourseDetailsSerializer, EnrollmentSerializer

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_courses(request,level_id, department_id):
    courses = Course.objects.filter(department = department_id, level = level_id)
    serializer = CourseDetailsSerializer(courses, many = True)
    return Response(serializer.data)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def enroll_in_course(request, course_id):
    course = get_object_or_404(
        Course,
        id = course_id
    )
    student = get_object_or_404(
        Student,
        user = request.user
    )
    if Enrollment.objects.filter(student = student).exists():
        return Response(
            {'error' : 'You are already enrolled'},
            status=status.HTTP_400_BAD_REQUEST
        )
    enrollment = Enrollment.objects.create(
        student=student,
        course=course
    )
    serializer = EnrollmentSerializer(enrollment)
    return Response(serializer.errors, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,IsTeacher])
def create_course(request, level_id, department_id):
    department = get_object_or_404(
        Department,
        id = department_id
    )
    level = get_object_or_404(
        Level,
        id = level_id
    )
    teacher = get_object_or_404(
        Teacher,
        user = request.user
    )

    if teacher.department != department:
        return Response({'detail': 'Forbidden.'}, status=status.HTTP_403_FORBIDDEN)    
    serializer = CourseDetailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(department=department, level=level)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_course(request,level_id, department_id, course_id):
    course = get_object_or_404(
        Course,
        id=course_id,
        level_id = level_id,
        department_id = department_id
    )

    serializer = CourseDetailsSerializer(course)
    return Response(serializer.data)
    
@api_view(['PATCH'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsTeacher])
def update_course(request,level_id, department_id, course_id):
    user = request.user
    department = get_object_or_404(
        Department,
        id = department_id
    )
    if user.teacher.department != department:
        return Response({'detail': 'Forbidden.'}, status=status.HTTP_403_FORBIDDEN)

    course = get_object_or_404(
        Course,
        id = course_id,
        department_id = department.id,
        level_id = level_id
    )
    serializer = CourseDetailsSerializer(course, data=request.data, partial = True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsTeacher])
def delete_course(request, level_id, department_id,course_id):
    user = request.user
    department = get_object_or_404(
        Department,
        id = department_id
    )
    if user.role != 'teacher' and user.teacher.department != department:
        return Response({'detail': 'Forbidden.'}, status=status.HTTP_403_FORBIDDEN)
    
    course = get_object_or_404(
        Course,
        id = course_id,
        department_id = department.id,
        level_id = level_id
    )
    course.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
