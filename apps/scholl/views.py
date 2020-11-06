from utils.Response import SuccessResponse, ErrorResponse, SerializerErrorResponse
from rest_framework.views import APIView

from rest_framework import serializers
from . import models
from users.models import UsersData

from django.forms.models import model_to_dict
from utils.Auth import GeneralAuthentication

from django.db.models import F

class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return SuccessResponse(msg='学校首页')


class SubmitSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    matter = serializers.CharField(max_length=200, error_messages={'required': '出校事由必填', 'blank': '出校事由不能为空'})
    phone = serializers.CharField(max_length=100, error_messages={'required': '联系方式必填', 'blank': '联系方式不能为空'})
    instructor = serializers.CharField(max_length=200, error_messages={'required': '辅导员必填', 'blank': '辅导员不能为空'})

    lxsj = serializers.CharField(max_length=100, error_messages={'required': '出校日期必填', 'blank': '出校日期不能为空'})
    cxqs = serializers.CharField(max_length=100, error_messages={'required': '起始时间必填', 'blank': '起始时间不能为空'})
    cxjs = serializers.CharField(max_length=100, error_messages={'required': '结束时间必填', 'blank': '结束时间不能为空'})

    xingdong = serializers.CharField(max_length=100, error_messages={'required': '出校行动轨迹必填', 'blank': '出校行动轨迹不能为空'})

    guiji = serializers.BooleanField(error_messages={'required': '轨迹必选', 'invalid': '请选择轨迹'})
    fanxiao = serializers.BooleanField(error_messages={'required': '返校必选', 'invalid': '请选择返校'})

    class Meta:
        model = models.Info
        fields = '__all__'


class SubmitView(APIView):
    def post(self, request, *args, **kwargs):

        auth = GeneralAuthentication(request)
        if not auth.is_auth():
            return ErrorResponse(**auth.is_auth_data())

        ud = UsersData.objects.filter(users=auth.get_object()).first()

        if ud.money < 1:
            return ErrorResponse(msg='余额不足')

        serializer = SubmitSerializer(data=request.data)

        if not serializer.is_valid():
            return SerializerErrorResponse(serializer)

        count = models.Examine.objects.count()

        info = serializer.save()
        info.beian = '000{id}'.format(id=(17000 + count))
        info.users = auth.get_object()
        info.save()

        instructor = request.data.get('instructor')
        examine_opinion = request.data.get('examine_opinion')

        import datetime
        new_time = datetime.datetime.now() + datetime.timedelta(minutes=15)

        models.Examine.objects.create(name=instructor, opinion=examine_opinion, info=info, create_time=new_time)

        ud.money = F('money') - 1
        ud.save()

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
        return model_to_dict(instance=res, fields=['id', 'name', 'opinion', 'info', 'create_time'])

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


class RecordListlView(APIView):

    def get(self, request, *args, **kwargs):
        auth = GeneralAuthentication(request)
        if not auth.is_auth():
            return ErrorResponse(**auth.is_auth_data())

        queryset = models.Info.objects.filter(users=auth.get_object())
        serializer = SubmitSerializer1(instance=queryset, many=True)

        return SuccessResponse(msg='获取成功', data=serializer.data)

