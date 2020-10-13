from django.shortcuts import render

from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

from django_redis import get_redis_connection

from utils.Response import BasicView, SuccessResponse, ErrorResponse, serializerErrorResponse
from utils.Validator import phone_validator
from utils.Sms import SEND_SMS
from utils.Time import getTimestamp, formatDate
from django.forms.models import model_to_dict

from . import models

########## message module
def Index(request):
    return Response({'postion': 'message api home'})


################### 发送验证码 #####################

class SmsSerializer(serializers.Serializer):
    phone = serializers.CharField(label="手机号", validators=[phone_validator,], error_messages={
        'blank': "手机号不能为空",
    })

class SmsView(APIView):

    serializer_class = SmsSerializer
    
    def post(self, request, *args, **kwargs):
        
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return serializerErrorResponse(serializer)

        phone = serializer.validated_data.get('phone')

        conn = get_redis_connection()
        
        stamp = conn.get('stamp_{phone}'.format(phone=phone))

        # 过期时间(秒)

        expired = 60

        if stamp:
            a = getTimestamp()
            b = int(stamp.decode('utf-8'))
            c = expired - (a - b)
            return ErrorResponse(code=2, msg='过于频繁,请稍候再试({0}s)!'.format(c))

        result = SEND_SMS(phone, debug=False)

        conn.set(result['phone'], result['code'], ex=5*60)
        stamp = getTimestamp()
        conn.set('stamp_{phone}'.format(phone=result['phone']), stamp, ex=expired)

        print(result)

        return SuccessResponse(msg='发送成功')

################### 表单提交 #####################
class SendSerializer(serializers.ModelSerializer):
    
    name = serializers.CharField(label="姓名", min_length=2, max_length=10, error_messages={
        'required': "姓名为必填项",
        'blank': "姓名不能为空",
        'min_length': '姓名不能小于2个',
        'max_length': '姓名不能大于10个',
    })

    phone = serializers.CharField(label="手机号", validators=[phone_validator, ], error_messages={
        'blank': "手机号不能为空",
    })

    textarea = serializers.CharField(label="留言内容", min_length=2, error_messages={
        'min_length': '留言内容不能少于2个字',
    })

    code = serializers.CharField(label="验证码", min_length=6, max_length=6, error_messages={
        'blank': '验证码不能为空',
        'min_length': '验证码不能小于6',
        'max_length': '验证码不能大于6',
    })

    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    def validate_code(self, value):

        if not value.isdecimal():
            raise ValidationError('验证码只能为数字')

        phone = self.initial_data.get('phone')
        conn = get_redis_connection()
        code = conn.get(phone)
        
        if not code:
            raise ValidationError('验证码不存在')
        
        if value != code.decode('utf-8'):
            raise ValidationError('验证码错误')
        
        return value

    def validate(self, attrs):
        del attrs['code']
        return attrs

    class Meta:
        model = models.Message
        fields = '__all__'

class SendView(APIView):
    serializer_class = SendSerializer

    def post(self, request, *argw, **kwargs):
        print(request.data.dict())

        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return serializerErrorResponse(serializer)
        
        phone = serializer.validated_data.get('phone')
        result = models.Message.objects.filter(phone=phone).exists()
        if not result:
            res = serializer.save()
            res.create_time = res.create_time.strftime('%Y-%m-%d %H:%M:%S')
            return SuccessResponse(data=model_to_dict(res), msg='保存成功')
        return ErrorResponse(code=2, msg='不能重复提交')
