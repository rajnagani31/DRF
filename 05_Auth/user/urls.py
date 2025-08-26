
from django.urls import path,include
from .views import UserRegisterView , Login ,ChangePassword
from rest_framework import routers


urlpatterns = [
    path('user-register/',UserRegisterView.as_view(),name='user_register'),
    path('user-login/',Login.as_view(),name='login'),

    path('password/<int:pk>/',ChangePassword.as_view(), name='password'),
    path('delete/',ChangePassword.as_view(),name='delete'),
]
