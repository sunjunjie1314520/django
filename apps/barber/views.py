


import requests

from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import JsonResponse
from django_redis import get_redis_connection
from django.forms.models import model_to_dict
from django.db.models import Sum

from utils.Response import BasicView, SuccessResponse, ErrorResponse, SerializerErrorResponse
from utils.Sms import SEND_SMS
from utils.Time import get_timestamp, NowTimeToUTC, get_ToDay_Type1, get_ToDay_Type2
from utils.Random import get_noncestr
from utils.Sign import sha1

from .serializer import PostSerializer
from . import models


########## barber module
class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'位置': 'barber module'}, status=200)

########## 列表与创建
class ListView(APIView):
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        
        curr_date = request.query_params.get('curr_date')

        queryset = models.Bill.objects.filter(curr_date=curr_date)[0: 10]

        serializer = self.serializer_class(instance=queryset, many=True)

        total = queryset.aggregate(nums=Sum('price'))['nums']

        data = {
            'wz': 0,
            'cb': 0,
            'total': 0,
            'record': serializer.data
        }
    
        if total:
            point = total - total * 0.3
            wz = point / 2
            cb = wz + total * 0.3

            data['total'] = round(total, 2)
            data['cb'] = round(cb, 2)
            data['wz'] = round(wz, 2)

        return SuccessResponse(data=data, msg="获取成功")

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            res = serializer.save()
            res.create_time = res.create_time.strftime('%H:%M:%S')
            return SuccessResponse(data=model_to_dict(res), msg="添加成功")
        return SerializerErrorResponse(serializer)