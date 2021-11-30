from stock.models import Stack
from rest_framework import serializers

class StockSerializer(serializers.ModelSerializer):
     class Meta:
         model= Stack
         fields ='__all__'


