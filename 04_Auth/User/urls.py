from django.urls import path, include
from  .views import UserRegisterView
urlpatterns = [
    path("userregister/",UserRegisterView.as_view(), name="user_register"),
]
