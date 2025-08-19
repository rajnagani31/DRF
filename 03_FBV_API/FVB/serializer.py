from rest_framework.serializers import ModelSerializer

from .models import UserTicket ,Student

class UserTicketSerializer(ModelSerializer):
    class Meta:
        model = UserTicket
        fields = '__all__'

class StudentSerializer(ModelSerializer):
    # course = (many=True, read_only=True)
    class Meta:
        model = Student
        fields = ['id','name','roll','course']
        # read_only_fields = ['course']