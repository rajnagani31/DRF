from rest_framework import  serializers
from .models import UserDetails

class UserDetaSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = '__all__'

        