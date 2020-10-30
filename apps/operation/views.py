from django.shortcuts import render

from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Address
from .serializer import AddressSerializer

def Index(request):
    return JsonResponse({'title': '管理模块'})


class AddressViewSet(APIView):

    def get(self, request):
        data = {
            'code': 0,
            'data': [],
            'msg': '收货地址',
            'total': 0
        }
        address = Address.objects.all()[:2]
        serializer = AddressSerializer(instance=address, many=True)

        data['data'] = serializer.data
        data['total'] = len(serializer.data)

        return Response(data, status=200)


    
    