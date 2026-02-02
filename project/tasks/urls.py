from django.urls import path
from .views import create_task, get_task


urlpatterns = [
    path('createtask/', create_task.as_view(), name='create_task'),
    path('get_all_task/', get_task.as_view(), name='get_task'),
]