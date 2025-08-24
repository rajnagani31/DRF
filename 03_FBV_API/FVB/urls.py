from django.urls import path
from .views import UserTicketAPI ,GetStudentData ,Products,GetUserItemsData

urlpatterns = [
    path("user-data/",UserTicketAPI ,name ='user data'),

    path("user-data/<int:pk>/",UserTicketAPI ,name ='user data'),
    path("studentdata/<int:pk>/",GetStudentData ,name ="student data"),

    # product api
    path("product/<int:pk>/",Products,name="product data"),

    # orderd Book API
    path("GetUserItemsData/<int:pk>/",GetUserItemsData,name="Get User Items Data")
]
