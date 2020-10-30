
from rest_framework.views import APIView
from rest_framework import serializers

from utils.Response import SuccessResponse, SerializerErrorResponse, ErrorResponse
from utils.Validator import phone_validator
from utils.Auth import GenerateToken, GeneralAuthentication

from . import models

################### 首页 ###################
class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return SuccessResponse(msg='用户模块')

################### 用户登录 #####################

class LoginSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(label="手机号", validators=[phone_validator,], error_messages={
        'required': '手机号必填'
    })

    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    code = serializers.CharField(label="验证码", min_length=6, max_length=6, write_only=True, error_messages={
        'required': '验证码必填',
        'min_length': '验证码为6位数字',
        'max_length': '验证码为6位数字',
    })

    def validate_code(self, value):
        if not value.isdecimal():
            raise serializers.ValidationError('验证码只能为数字')

    class Meta:
        model = models.Users
        fields = ['id', 'phone', 'name', 'password', 'md5_password', 'create_time', 'code']
        read_only_fields = ['md5_password']
        extra_kwargs = {'name': {'write_only': True}}


class LoginView(APIView):
    def post(self, request, *args, **kwargs):

        vate_serializer = LoginSerializer(data=request.data)
        if not vate_serializer.is_valid():
            
            return SerializerErrorResponse(vate_serializer)

        print(vate_serializer.data)

        phone = vate_serializer.validated_data.get('phone')
        query = models.Users.objects.filter(phone=phone).first()

        if not query:
            return ErrorResponse(msg='账号或者密码错误')

        serializer = LoginSerializer(instance=query)

        token = GenerateToken(serializer.data).get_token()

        return SuccessResponse(msg='登录成功', data=token)

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