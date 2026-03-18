from django.urls import path
from ..views import users as user_views


# User urls
urlpatterns = [
    # User registration and login
    path('users/register/student/', user_views.create_student, name='create_student'),
    path('users/register/teacher/', user_views.create_teacher, name='create_teacher'),
    path('users/login/', user_views.login, name='login'),
    
    # User details and management
    path('users/me/', user_views.get_user_details, name='get_user_details'),
    path('users/update/student/', user_views.update_student, name='update_student'),
    path('users/update/teacher/', user_views.update_teahcer, name='update_teacher'),
    path('users/delete/student/', user_views.delete_student, name='delete_student'),
    path('users/delete/teacher/', user_views.delete_teacher, name='delete_teacher'),

    #make admin
    path('users/<int:user_id>/makeadmin/', user_views.make_admin, name='make_admin')
]
