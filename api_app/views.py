from django.shortcuts import render

from stock.models import Stack
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import StockSerializer


class Stock_api(APIView):
    def get(self,request):
        context={}
        stock_list=Stack.objects.all()
        slist=StockSerializer(stock_list,many=True)
        print(slist.data)
        context['list']= slist.data
        context['count']= len(slist.data)
        return Response(context)
