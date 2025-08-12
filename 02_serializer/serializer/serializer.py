from rest_framework import serializers
from .models import company, Companydata

class companySerializer(serializers.ModelSerializer):
    class Meta:
        model = company
        fields = "__all__"

    def validate_company_name(self, value):

        data = [c.strip() for c in value.split(",") if c.strip()]
        print(data)
        if len(data) < 2:
            print('yes')
            return value
        else:
            print("yes else")
            raise serializers.ValidationError("Enter only One Company Name Not more then one!!!")
        
    def validate(self,value):
        print('yes id',value)
        cheak_id_get= company.objects.count()
        # print()
        print(cheak_id_get)
        return value
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
        
