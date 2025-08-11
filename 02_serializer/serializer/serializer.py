from rest_framework import serializers
from .models import company, Companydata

class companySerializer(serializers.ModelSerializer):
    class Meta:
        model = company
        fields = "__all__"

class CompanydataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companydata
        fields = "__all__"

    def validate_team_manager(self, value):

        data = [m.strip() for m in value.split(",") if m.strip()]
        print(data)
        if len(data) <= 2:
            print('yes')
            return value
        else:
            print('else yes')
            raise serializers.ValidationError("Select any 2 or less then 2 manager")
        
