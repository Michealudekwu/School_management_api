from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from ...models import Performance, Progress
from ...serializers import PerformanceSerializer, ProgressSerializer
from ..users import IsStudent

@permission_classes([IsStudent])
@api_view(['GET'])
def performance_view(request):
    performance = Performance.objects.filter(student=request.user.student_profile).select_related('course')
    serializer = PerformanceSerializer(performance, many=True)
    return Response(serializer.data)

@permission_classes([IsStudent])
@api_view(['GET'])
def progress_view(request):
    progress = Progress.objects.filter(user=request.user).select_related('course')
    serializer = ProgressSerializer(progress, many=True)
    return Response(serializer.data)