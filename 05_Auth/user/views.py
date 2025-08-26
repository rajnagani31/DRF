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
from .utils import SerlizerValidation,EmailUtils
import re
# Create your views here.
class UserRegisterView(APIView ,SerlizerValidation ,EmailUtils):

    " registrtion API with TOKEN JWT"
    serializer_class = UserRegisterSerializer
    def post(self,request):
        try:
            serializer = UserRegisterSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                data = serializer.data
                access_token = AccessToken.for_user(serializer.instance)
                email = data.get('email')
                username = request.data.get('first_name')
                print(email  , username)
                EmailUtils.welcom_email(email,username)

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
            data_= serializer.is_valid(raise_exception=True)
            serializer.validated_data
            email = request.data.get('email')
            password = request.data.get('password')
            print(f"Email:{email} {password}")

            user_cheak = UserDetails.objects.filter(email= email ,is_delete = False).first()
            if not user_cheak:
                return self.return_response(status.HTTP_401_UNAUTHORIZED,'first register to login')
                # return Response({"message":"first register to login","status":status.HTTP_401_UNAUTHORIZED})

            access_token = AccessToken.for_user(user_cheak)
            data_ = {
                "data":
                    {   
                        "user_id":user_cheak.id,
                        "message":"login successful",
                        "status": status.HTTP_200_OK,
                        "jwt_token":str(access_token),}
            }
            # return Response({"message":"login successfull","status":status.HTTP_200_OK ,"data":data_})
            # return self.return_response(status.HTTP_200_OK , "Login successful.",data=data_)
            return self.custom_response(status.HTTP_200_OK ,"login successfull",**data_)
        except Exception as e:
            return Response({"message":str(e)})

from django.contrib.auth.hashers import make_password

class ChangePassword(APIView,SerlizerValidation):
    permission_classes =[IsAuthenticated]
    def post(self, request ,pk=None):

        user_id = pk

        print(user_id)
        new_password= request.data.get('new_password')
        confirm_password = request.data.get('confirm_password')

        if not all([new_password,confirm_password]):
            return self.return_response(status.HTTP_400_BAD_REQUEST , "Plese enter a both field")
        
        password_pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#^~+=\(\)\-])[A-Za-z\d@$!%*?&#^~+=\(\)\-]{8,25}$")
        if not password_pattern.match(new_password):
            return self.return_response(status.HTTP_400_BAD_REQUEST ,"password must be 8-25 characters long , contain at least one uppercase letter one lowercase letter and one digit are required")
        
        if confirm_password != new_password:
            return self.return_response(status.HTTP_400_BAD_REQUEST ,"password and Confir password do not match !")
        
        if user_id:
            new = new_password
            data=UserDetails.objects.filter(pk=user_id , is_delete = False).first()
            if not data:
                return Response({"message":"Id not found"} ,status.HTTP_404_NOT_FOUND)
            data.password = make_password(new)
            data.save()
            print(data)
            # data.save()
            return Response({'message':'password changed',"status":status.HTTP_200_OK})
        return Response({"error":"invalid data","status":status.HTTP_400_BAD_REQUEST})

    def delete(self,request):

        user_id = request.query_params.get('user_id')
        if not user_id:
            return self.return_response(status.HTTP_400_BAD_REQUEST ,"User id is None")
        user = UserDetails.objects.filter(pk=user_id ,is_delete = False).first()
        if not user:
            return self.return_response(status.HTTP_400_BAD_REQUEST ,"This user in not exsist")
        # user.delete()
        user.is_delete = True
        user.save()
        return self.return_response(status.HTTP_200_OK,"Your account succesfully deleted")