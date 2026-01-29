from django.urls import path
from .views import create_task


urlpatterns = [
    path('createtask/', create_task.as_view(), name='create_task'),
]