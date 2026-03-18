from django.urls import path
from ..views import assesments as assessments_views

urlpatterns=[
    path('start_exam/',assessments_views.start_exam_view, name="record-start"),
    path('begin_exam/', assessments_views.submit_attempt, name="questoins"),
    path('stop_exam/', assessments_views.submit_attempt, name="submit-exam"),
    path('results/', assessments_views.view_results)
]
