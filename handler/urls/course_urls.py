from django.urls import path, include
from ..views import school_details as school_views

urlpatterns=[
    path('',school_views.get_courses),
    path('create/',school_views.create_course),
    path('<int:course_id>/',school_views.get_course),
    path('<int:course_id>/update/',school_views.update_course),
    path('<int:course_id>/delete/',school_views.delete_course),
]