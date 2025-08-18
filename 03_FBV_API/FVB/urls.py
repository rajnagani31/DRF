from django.urls import path
from .views import UserTicketAPI

urlpatterns = [
    path("user-data/",UserTicketAPI ,name ='user data'),

    path("user-data/<int:pk>/",UserTicketAPI ,name ='user data')
]
