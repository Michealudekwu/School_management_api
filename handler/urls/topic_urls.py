from django.urls import path, include
from ..views import school_details as school_views

urlpatterns = [
    path('course/<int:course_id>/topics/', school_views.all_topics),
    path('course/<int:course_id>/topic/create/', school_views.create_topic),
    path('course/<int:course_id>/topic/<int:tp_id>/complete/', school_views.completed_topic),
    path('course/<int:course_id>/topic/<int:tp_id>/', school_views.get_topic),
    path('course/<int:course_id>/topic/<int:tp_id>/update/', school_views.update_topic),
    path('course/<int:course_id>/topic/<int:tp_id>/delete/', school_views.delete_topic)
]