
from django.urls import path,include
from .views import *
from rest_framework import routers
from .sse import *


urlpatterns = [
    path('user-register/',UserRegisterView.as_view(),name='user_register'),
    path('user-login/',Login.as_view(),name='login'),

    path('password/<int:pk>/',ChangePassword.as_view(), name='password'),
    path('delete/',ChangePassword.as_view(),name='delete'),
    # SSE
    path('getsse/',SSEAPI.as_view(),name='sseapi'),
    path('triger/',SSETriger.as_view(),name = 'triger'),
    
    # currency 
    path('currency/',Currencydata.as_view(),name='currencydata'),
    # AddList
    path('useraddlist/',UserAddListView.as_view(),name='useraddlist'),
    path('getlist/',Getist.as_view(),name='getlist'),
    path('getlist-limit/',LimitOffsetPaginationView.as_view(),name='getlist-limit'),

]
