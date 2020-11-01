from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from utils.Response import SuccessResponse, SerializerErrorResponse, ErrorResponse
from utils.Validator import phone_validator
from utils.Auth import GenerateToken, GeneralAuthentication
from utils.Sms import MD5

from django_redis import get_redis_connection
from . import models


################### 首页 ###################

class IndexView(APIView):

    def get(self, request, *args, **kwargs):
        return SuccessResponse(msg='用户模块')


class LoginSerializer(serializers.ModelSerializer):

    phone = serializers.CharField(label="手机号", validators=[phone_validator, ], error_messages={
        'required': '手机号必填',
        'blank': "手机号码不能为空",
    })

    password = serializers.CharField(label='密码', max_length=32, min_length=32, error_messages={
        'required': '密码必填',
        'blank': '密码不能为空',
        'min_length': '密码为32位的MD5',
        'max_length': '密码为32位的MD5',
    })

    code = serializers.CharField(label="验证码", min_length=6, max_length=6, write_only=True, error_messages={
        'required': '验证码必填',
        'blank': '验证码不能为空',
        'min_length': '验证码为6位数字',
        'max_length': '验证码为6位数字',
    })

    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    def validate_code(self, value):

        if not value.isdecimal():
            raise serializers.ValidationError('验证码只能为数字')

        phone = self.initial_data.get('phone')
        conn = get_redis_connection()
        code = conn.get(phone)

        if not code:
            raise serializers.ValidationError('验证码不存在')

        if value != code.decode('utf-8'):
            raise serializers.ValidationError('验证码错误')

        conn.delete('stamp_{phone}'.format(phone=phone))

        return value

    class Meta:
        model = models.Users
        fields = '__all__'

################### 用户登录 #####################

class LoginView(APIView):
    def post(self, request, *args, **kwargs):

        vate_serializer = LoginSerializer(data=request.data)
        if not vate_serializer.is_valid():
            return SerializerErrorResponse(vate_serializer)

        print(vate_serializer.data)

        phone = vate_serializer.validated_data.get('phone')
        password = vate_serializer.validated_data.get('password')
        query = models.Users.objects.filter(phone=phone, md5_password=password).first()

        if not query:
            return ErrorResponse(msg='账号或者密码错误')

        serializer = LoginSerializer(instance=query)

        token = GenerateToken(serializer.data).get_token()

        # 删除验证码
        conn = get_redis_connection()
        conn.delete(phone)

        return SuccessResponse(msg='登录成功', data=token)


################### 用户注册 #####################

class RegisterSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    phone = serializers.CharField(label="手机号", validators=[phone_validator, UniqueValidator(queryset=models.Users.objects.all(), message='该用户已注册')], error_messages={
        'blank': "手机号码不能为空",
    })

    password = serializers.CharField(label='密码', max_length=32, error_messages={
        'blank': "密码不能为空",
        'required': '密码必填项',
    })

    code = serializers.CharField(label="验证码", min_length=6, max_length=6, write_only=True, error_messages={
        'blank': '验证码不能为空',
        'min_length': '验证码为6位数字',
        'max_length': '验证码为6位数字',
    })

    def validate_code(self, value):

        if not value.isdecimal():
            raise serializers.ValidationError('验证码只能为数字')

        phone = self.initial_data.get('phone')
        conn = get_redis_connection()
        code = conn.get(phone)

        if not code:
            raise serializers.ValidationError('验证码不存在')

        if value != code.decode('utf-8'):
            raise serializers.ValidationError('验证码错误')

        conn.delete('stamp_{phone}'.format(phone=phone))

        return value

    def validate(self, attrs):
        attrs['md5_password'] = MD5(self.initial_data.get('password'))
        del attrs['code']

        return attrs

    class Meta:
        model = models.Users
        fields = '__all__'


class RegisterView(APIView):

    def post(self, request, *args, **kwargs):
        print(request.data)

        serializer = RegisterSerializer(data=request.data)
        if not serializer.is_valid():
            return SerializerErrorResponse(serializer)

        serializer.save()

        # 删除验证码
        conn = get_redis_connection()
        conn.delete(serializer.data.get('phone'))

        token = GenerateToken(serializer.data).get_token()

        return SuccessResponse(msg='注册成功', data=token)


################### 用户资料 #####################

class PersonalViewSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = models.Users
        # fields = ['name', 'phone']
        fields = '__all__'
        # exclude = ['md5_password', 'password']


class PersonalView(APIView):

    def get(self, request, *args, **kwargs):
        auth = GeneralAuthentication(request)
        if not auth.is_auth():
            return ErrorResponse(**auth.is_auth_data())

        serializer = PersonalViewSerializer(instance=auth.get_object())
        return SuccessResponse(msg='个人资料', data=serializer.data)
