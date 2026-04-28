from django.urls import path
from . import views

urlpatterns = [
    path('user-create/', views.UserCreateAPIView.as_view()),
    path('product/', views.ProductAPIView.as_view()),
    path('product/<int:pk>/', views.ProductAPIView.as_view()),
]