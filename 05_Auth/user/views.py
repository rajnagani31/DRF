from django.shortcuts import render
from rest_framework import generics
from .models import UserDetails
from .serializer import UserRegisterSerializer ,LoginSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .utils import SerlizerValidation
# Create your views here.
class UserRegisterView(APIView ,SerlizerValidation):

    " registrtion API with TOKEN JWT"
    serializer_class = UserRegisterSerializer
    def post(self,request):
        try:
            serializer = UserRegisterSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                data = serializer.data
                access_token = AccessToken.for_user(serializer.instance)


                response_data =({
                    "status":status.HTTP_201_CREATED,
                    "message":"User registered successfully",
                    "Token":{
                        "TOkEN": str(access_token),
                    },
                    "user data":{
                        "email":request.data.get('email'),
                        "password":request.data.get('password'),
                        "created_date":request.data.get("created_date"),
                        "updated_date":request.data.get("updated_date"),
                        # "first name": data.get('firstname')
                    },
                    'data':{
                        "pass":data.get('password'),
                    }
                    })
                # response_data = {
                #     "status": status.HTTP_201_CREATED,
                #     "message": "User registered successfully",
                #     # "token": str(access_token),
                #     "user_data": {
                #         "email": data.get("email"),
                #         "first_name": data.get("firstname"),
                #         "username": data.get("password"),
                #     },
                # }
                # return self.custom_response(status.HTTP_201_CREATED,message="ok",**response_data)
                return self.return_response(status.HTTP_201_CREATED ,"User register successfully",response_data)
                # return Response(response_data , status.HTTP_201_CREATED)
            return self.return_response(status.HTTP_400_BAD_REQUEST,"Invalid Data",data=serializer.errors)
            # return Response(serializer.errors ,status.HTTP_400_BAD_REQUEST) 
        except Exception as e:
            return Response({"ERROR":str(e)} ,status = status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
        
class Login(APIView,SerlizerValidation):
    def post(self,request):
        try :
            serializer = LoginSerializer(data = request.data)
            serializer.is_valid(raise_exception=True)
            data = serializer.validated_data
            email = data.get('email')
            password = data.get('password')
            user_cheak = UserDetails.objects.filter(email= email ,is_delete = False).first()
            if user_cheak is None:
                pass
        except:
            pass    