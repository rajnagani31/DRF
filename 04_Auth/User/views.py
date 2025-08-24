from django.shortcuts import render
from rest_framework.decorators import APIView
from .serializer import UserRegisterSerializer
from rest_framework.response import Response
from rest_framework import status
class UserRegisterView(APIView):
    def post(self,request):
        try:
            serializer = UserRegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status": status.HTTP_201_CREATED,
                    "message": "User registered successfully.",
                    "data": serializer.data
                }, status=status.HTTP_201_CREATED)  
            return Response({"message":"Invalid data.", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": "An error occurred.", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)