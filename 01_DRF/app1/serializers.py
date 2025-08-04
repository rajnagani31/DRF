from rest_framework import  serializers
from .models import UserDetails

class UserDetaSerializers(serializers.HyperlinkedModelSerializer):
    user_id= serializers.ReadOnlyField(source='id')
    class Meta:
        model = UserDetails
        fields = '__all__'

        