from django.urls import path
from .views import create_task, get_task, update_task, delete_task


urlpatterns = [
    path('create/', create_task.as_view(), name='create_task'),
    path('get_all_task/', get_task.as_view(), name='get_task'),
    path('update/<int:task_id>/', update_task.as_view(), name='update_task'),
    path('delete/<int:task_id>/', delete_task.as_view(), name='delete_task')
]