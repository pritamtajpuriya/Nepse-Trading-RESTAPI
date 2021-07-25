from django.db.models import fields
from rest_framework import serializers
from .models import *

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model= Company
        exclude=['id','trade']
        


class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Trade
        exclude=['id'] 

        