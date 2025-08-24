from rest_framework import serializers 
from .models import UserDetails
import re
from django.contrib.auth.hashers import make_password


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = UserDetails
        fields = ['id', 'email', 'password', 'firstname', 'lastname','id']


    def validate(self, attrs):
        if UserDetails.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({"email": "Email is already exists."})
        
        password_pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d@$!%*?&#^~+=\(\)\-]{8,25}$")
        if not password_pattern.match(attrs['password']):
            raise serializers.ValidationError({"password": "Password must be 8-25 characters long, contain at least one uppercase letter, one lowercase letter, and one digit."})
        
        attrs['password'] = make_password(attrs['password'])
        return attrs