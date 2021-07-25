from nepseAPI.serializers import CompanySerializer, TradeSerializer
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Company, Trade

class CompanyListedView(APIView):
   def get(self, request):

       company=Company.objects.all()
       list=[]
       serializer= CompanySerializer(company,many=True)
       for data in serializer.data:
        #    if data["market_price"]<500 and data['weeks_52_high']-data['market_price']>50 and data['sector']!='HydroPower':
            list.append(data)
       return Response({"length":str(len(list)),"data":list})


class liveTradeView(APIView):

    def get(self,request):
        trade= Trade.objects.all()
        serializer= TradeSerializer(trade,many=True)


        return Response(serializer.data)

       
        
     

            







    

