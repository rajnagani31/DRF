from rest_framework import serializers
from .models import company, Companydata,BookData

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

        
def run_and_call_openai():
    pass        
class BookSerializer(serializers.ModelSerializer):
    "validate is custom created error cheaker "
    # validate = serializers.CharField(validators = [runHey, Cortana. _and_call_openai])
    # read = serializers.CharField(read_only=True)
    # date_time = serializers.DateTimeField(read_only=True)
    class Meta:
        model = BookData 
        "Use any one of them __all__ & exclude"
        # fields = "__all__"
        fields =['title','author','price']
        # exclude = ['isbn']
        # read_only_fields = ['read','date_time']
        extra_kwargs ={
            # "title":{"required":False},
            "price":{"read_only":True},
            "read":{"read_only":True},
            "date_time":{"read_only":True}
            }
    
    def validate(self, data):
        " Object level validation"
        title = data.get('title')
        author = data.get('author')

        if title.lower() == 'admin' or author.lower() == 'admin':
            raise serializers.ValidationError('You does not Use Admin username ..')
        return data