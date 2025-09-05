from rest_framework import serializers 
from .models import UserDetails , Notification,Currency,UserAddList
import re
from django.contrib.auth.hashers import make_password


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    # firstname = serializers.CharField(required =True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = UserDetails
        fields = ['id', 'email', 'password', 'firstname', 'lastname']


    def validate(self, attrs):
        if UserDetails.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({"email": "Email is already exists."})
        
        password_pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d@$!%*?&#^~+=\(\)\-]{8,25}$")
        if not password_pattern.match(attrs['password']):
            raise serializers.ValidationError({"password": "Password must be 8-25 characters long, contain at least one uppercase letter, one lowercase letter, and one digit."})
        
        attrs['password'] = make_password(attrs['password'])
        return attrs
    

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required =True) 
    password = serializers.CharField(required = True) 

    class Meta:
        model = UserDetails
        fields =['email' , 'password']

class NotificationSerializer(serializers.ModelSerializer):
    message = serializers.CharField(required=True)
    class Meta:
        model = Notification
        fields = ['message']        

    def validate(self, data):
        if not data.get('message'):
            raise serializers.ValidationError({"message": "Message cannot be empty."})
        return data
    

class currencySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    class Meta:
        model = Currency
        fields = ['name']    

class userAddListSerializer(serializers.ModelSerializer):  
    user_id = serializers.IntegerField(required=False)  
    class Meta:
        model = UserAddList
        fields = ['user_id','Currency_accepted', 'Currency_of_payout']