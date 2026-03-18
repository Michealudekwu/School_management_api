from django.urls import path, include
from ..views import assesments as assessment_views

urlpatterns = [
    path('level/<int:level_id>/department/<int:department_id>/course/<int:course_id>/exam/', assessment_views.exam_list_create, name='view-exams'),
    path('level/<int:level_id>/department/<int:department_id>/course/<int:course_id>/exam/create/', assessment_views.exam_list_create, name='create-exam'),
    path('course/<int:course_id>/exam/<int:exam_id>/', assessment_views.exam_detail),
    path('course/<int:course_id>/exam/<int:exam_id>/questions/', assessment_views.exam_questions_list_create, name="get_questions"),
    path('course/<int:course_id>/exam/<int:exam_id>/question/create/', assessment_views.exam_questions_list_create, name="create_questions"),
    path('course/<int:course_id>/exam/<int:exam_id>/question/<int:question_id>/', assessment_views.exam_question_detail),
    path('course/<int:course_id>/exam/<int:exam_id>/question/<int:question_id>/update/', assessment_views.exam_question_detail),
    path('course/<int:course_id>/exam/<int:exam_id>/question/<int:question_id>/delete/', assessment_views.exam_question_detail),
    path('course/<int:course_id>/exam/<int:exam_id>/question/<int:question_id>/option/', include('handler.urls.options_urls')),
    path('course/<int:course_id>/exam/<int:exam_id>/start_stop/', include('handler.urls.submit_urls'))
]

