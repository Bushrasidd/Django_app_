from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
        TokenVerifyView,
    )


urlpatterns = [
    path('', views.hello, name='greeting'),
    path('create/', views.CreateUser.as_view(), name = 'create-user'),
    path('login/', views.Login.as_view(), name = 'user-login'),
    path('list/', views.listUser.as_view(), name='ListUsers'),
    path('update/', views.UpdateUser.as_view(), name = 'Update-user'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('logout/', views.logout.as_view(), name='user-logout'),
    path('delete/',views.DeleteUser.as_view(), name='delete-user'),
]