from django.shortcuts import render

from django.http import JsonResponse

from utils.Response import BasicView
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import serializers
from rest_framework import status
from utils.Validator import phone_validator

def Index(req):
    return JsonResponse({'title': '用户模块'})

################### 登录 #####################
class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(label="手机号", validators=[phone_validator,])
    phone = serializers.CharField(label="手机号", validators=[phone_validator,])
    code = serializers.CharField(label="临时凭据", min_length=5, max_length=10, required=True, error_messages={
        'min_length': '凭据不能小于5',
        'max_length': '凭据不能大于10',
    })

class LoginView(APIView, BasicView):
    serializer_class = LoginSerializer

    def get(self, request, *args, **kwargs):
        print(request.data)
        return Response({'abc':'1564165456'})

    def success(self, serializer):
        print('success')

