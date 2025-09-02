from .models import nastahouse
from rest_framework import serializers

class NastahouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = nastahouse
        fields = '__all__'