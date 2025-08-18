from rest_framework.serializers import ModelSerializer

from .models import UserTicket

class UserTicketSerializer(ModelSerializer):
    class Meta:
        model = UserTicket
        fields = '__all__'
