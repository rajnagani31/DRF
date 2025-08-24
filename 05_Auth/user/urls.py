
from django.urls import path
from .views import UserRegisterView


urlpatterns = [
    path('user-register/',UserRegisterView.as_view(),name='user_register')
]
