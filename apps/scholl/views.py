from utils.Response import SuccessResponse, ErrorResponse, SerializerErrorResponse
from rest_framework.views import APIView

from rest_framework import serializers
from . import models
from django.forms.models import model_to_dict

class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return SuccessResponse(msg='学校首页')


class SubmitSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = models.Info
        fields = '__all__'


class SubmitView(APIView):
    def post(self, request, *args, **kwargs):

        print(request.data)
        serializer = SubmitSerializer(data=request.data)

        if not serializer.is_valid():
            return SerializerErrorResponse(serializer)

        info = serializer.save()

        examine_name = request.data.get('examine_name')
        examine_opinion = request.data.get('examine_opinion')

        import datetime
        new_time = datetime.datetime.now() + datetime.timedelta(minutes=15)

        models.Examine.objects.create(name=examine_name, opinion=examine_opinion, info=info, create_time=new_time)

        return SuccessResponse(msg='提交成功', data=serializer.data)


class SubmitSerializer1(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    status_text = serializers.CharField(source='get_status_display', read_only=True)

    examine = serializers.SerializerMethodField()

    def get_examine(self, obj):
        res = models.Examine.objects.filter(info=obj).first()
        if not res:
            return None
        res.create_time = res.create_time.strftime('%Y-%m-%d %H:%M:%S')
        return model_to_dict(res, fields=['id', 'name', 'opinion', 'info', 'create_time'])


    class Meta:
        model = models.Info
        fields = '__all__'

class BookDetailView(APIView):
    def get(self, request, pk):
        """
        获取
        """
        book = models.Info.objects.filter(pk=pk).first()
        if not book:
            return ErrorResponse(code=2, msg='ID不存在')
        serializer = SubmitSerializer1(instance=book)
        return SuccessResponse(msg='获取成功', data=serializer.data)

    def put(self, request, pk):
        """
        修改
        """
        book = models.Info.objects.filter(pk=pk).first()
        if not book:
            return ErrorResponse(code=2, msg='ID不存在')
        book_data = request.data
        serializer = SubmitSerializer(instance=book, data=book_data)
        if not serializer.is_valid():
            return SerializerErrorResponse(serializer)
        serializer.save()
        return SuccessResponse(msg='修改成功', data=serializer.data)

    def delete(self, request, pk):
        """
        删除
        """
        book = models.Info.objects.filter(pk=pk).first()
        if not book:
            return ErrorResponse(code=2, msg='ID不存在')
        book.delete()
        return SuccessResponse(msg='删除成功')
