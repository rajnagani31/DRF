from rest_framework import generics
from rest_framework.views import APIView
from .models import User, Email, product, profile
from rest_framework.response import Response


class UserCreateAPIView(APIView):
    def post(self, request):
        username = 'raj'
        email = 'raj@gmail.com'
        password = 'raj123'
        user = User.objects.create(username=username, email=email, password=password)
        user.save()
        user_delete = Email.objects.filter(is_sended= False)
        user_delete.delete()
        return Response({'message': 'User created successfully'})
    



    

    