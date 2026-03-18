from django.urls import path
from ..views import assesments as assessments_view

urlpatterns = [
    path('', assessments_view.option_list_create),
    path('create/', assessments_view.option_list_create),
    path('<int:option_id>/', assessments_view.option_detail),
    path('<int:option_id>/update/', assessments_view.option_detail),
    path('<int:option_id>/delete/', assessments_view.option_detail),
]