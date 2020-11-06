from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from utils.Response import SuccessResponse, SerializerErrorResponse, ErrorResponse
from utils.Validator import phone_validator
from utils.Auth import GenerateToken, GeneralAuthentication
from utils.Sms import MD5

from django_redis import get_redis_connection
from . import models
from django.forms.models import model_to_dict
import random
from django.conf import settings

################### 首页 ###################
class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return SuccessResponse(msg='上传模块')

############## 上传图片 ##############

class ImageView(APIView):

    def post(self, request, *args, **kwargs):
        from django.core.files.uploadedfile import UploadedFile
        file = request.FILES.get('file')

        # file = request.FILES.values()[0]
        # wrapped_file = UploadedFile(file)
        upload = models.Image.objects.create(img=file)

        return SuccessResponse(msg='上传成功', data={'id': upload.id, 'img': settings.HTTP_URL + upload.img.url, 'size': upload.img.size, 'height': upload.img.height, 'width': upload.img.width})

