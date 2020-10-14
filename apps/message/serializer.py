

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django_redis import get_redis_connection
from utils.Validator import phone_validator, name_validator

from . import models

class SmsSerializer(serializers.Serializer):
    phone = serializers.CharField(label="手机号", validators=[phone_validator,], error_messages={
        'blank': "手机号不能为空",
    })

class SendSerializer(serializers.ModelSerializer):
    name = serializers.CharField(label="姓名", min_length=2, max_length=10, validators=[name_validator, ], error_messages={
        'required': "姓名为必填项",
        'blank': "姓名不能为空",
        'min_length': '姓名不能少于2个',
        'max_length': '姓名不能多于10个',
    })
    phone = serializers.CharField(label="手机号", validators=[phone_validator, ], error_messages={
        'blank': "手机号码不能为空",
    })
    textarea = serializers.CharField(label="留言内容", min_length=2, error_messages={
        'min_length': '留言内容不能少于2个字',
    })
    code = serializers.CharField(label="验证码", min_length=6, max_length=6, error_messages={
        'blank': '验证码不能为空',
        'min_length': '验证码为6位数',
        'max_length': '验证码为6位数',
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