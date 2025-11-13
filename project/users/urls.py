from django.urls import path
from . import views


urlpatterns = [
    path('', views.hello, name='greeting'),
    path('create/', views.CreateUser.as_view(), name = 'create-user'),
    path('list/', views.listUser.as_view(), name='ListUsers'),
    path('update/', views.UpdateUser.as_view(), name = 'Update-user')
]