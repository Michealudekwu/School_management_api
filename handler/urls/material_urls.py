from django.urls import path
from ..views import school_details as school_views

urlpatterns = [
    path('topic/<int:tp_id>/materials/', school_views.all_materials),
    path('course/<int:course_id>/topic/<int:tp_id>/material/create/', school_views.create_materials),
    path('topic/<int:tp_id>/material/<int:mat_id>/', school_views.get_material),
    path('topic/<int:tp_id>/material/<int:mat_id>/update/', school_views.update_material),
    path('topic/<int:tp_id>/material/<int:mat_id>/delete/', school_views.delete_material)
]