from django.urls import path
from ..views import assesments as assessments_views

urlpatterns = [
    path('analytics/performance', assessments_views.performance_view),
    path('analytics/progress_view', assessments_views.progress_view)
]