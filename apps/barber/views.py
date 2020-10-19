


import requests

from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import JsonResponse
from django_redis import get_redis_connection
from django.forms.models import model_to_dict

from utils.Response import BasicView, SuccessResponse, ErrorResponse, serializerErrorResponse
from utils.Sms import SEND_SMS
from utils.Time import get_timestamp, NowTimeToUTC
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
        data = models.Bill.objects.all()[0: 10]
        serializer = self.serializer_class(instance=data)
        print(serializer.data)
        
        return Response({'位置': 'barber module', '即时任务ID': 'dsfasdf', '定时任务ID': 'adfas564'}, status=200)

    def post(self, request, *args, **kwargs):
        return Response({'位置': 'barber module', '即时任务ID': '564644', '定时任务ID': 'adfas564'}, status=200)