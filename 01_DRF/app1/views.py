from django.shortcuts import render
from rest_framework import viewsets
from .models import UserDetails
from .serializers import UserDetaSerializers
# Create your views here.
# class UserDetailsViewSet(viewsets.ModelViewSet):
#     queryset= UserDetails.objects.all()
#     serializer_class = UserDetaSerializers

class UserDetailsViewSet(viewsets.ModelViewSet):
    queryset = UserDetails.objects.all()
    serializer_class = UserDetaSerializers
