from django.urls import path , include
from rest_framework import routers
from .views import UserDetailsViewSet

router = routers.DefaultRouter()
router.register(r'userdata',UserDetailsViewSet)

urlpatterns = [
    path('',include(router.urls)),
]

