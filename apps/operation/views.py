from django.shortcuts import render

from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Address
from .serializer import AddressSerializer

from utils.Response import BasicView



def Index(request):
    return JsonResponse({'title': '用户操作模块'})


class AddressViewSet(APIView, BasicView):

    serializer_class = AddressSerializer

    def get(self, request):
        data = {
            'code': 0,
            'data': [],
            'msg': '收货地址',
            'total': 0
        }
        address = Address.objects.all()[:2]
        serializer = self.serializer_class(address, many=True)

        data['data'] = serializer.data
        data['total'] = len(serializer.data)

        return Response(data)


    
    