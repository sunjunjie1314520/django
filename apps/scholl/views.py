from utils.Response import SuccessResponse, ErrorResponse, SerializerErrorResponse
from rest_framework.views import APIView

from rest_framework import serializers
from . import models
from users.models import UsersData, Users

from utils.Validator import phone_validator, money_validator

from django.forms.models import model_to_dict
from utils.Auth import GeneralAuthentication

from django.db.models import F

from users.views import PersonalViewSerializer

from utils.Paginator import PaginatorData
from utils.Time import get_ToDay_Type1
from system.models import Config

import time


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

        # 查询上一次记录
        lastRecord = models.Info.objects.filter(users=auth.get_object(), status__lte=2)
        if lastRecord:
            return ErrorResponse(msg='请先结束上一次出校记录')

        serializer = SubmitSerializer(data=request.data)
        if not serializer.is_valid():
            return SerializerErrorResponse(serializer)

        config = Config.objects.get(pk=1)
        ud = UsersData.objects.filter(users=auth.get_object()).first()

        fanxiao = serializer.validated_data.get('fanxiao')

        if fanxiao:
            money = config.money
        else:
            money = config.not_money

        if ud.money < money:
            return ErrorResponse(msg='余额不足%s元' % money)
            # return ErrorResponse(msg='系统暂停服务,请联系客服!')

        count = models.Info.objects.all().order_by('-id').first()

        info = serializer.save()
        info.beian = '000{id}'.format(id=(202984 + count.id))
        info.users = auth.get_object()
        info.save()

        instructor = request.data.get('instructor')
        examine_opinion = request.data.get('examine_opinion')

        import datetime
        new_time = datetime.datetime.now() + datetime.timedelta(minutes=15)

        models.Examine.objects.create(name=instructor, opinion=examine_opinion, info=info, create_time=new_time)

        ud.money = F('money') - money
        ud.save()

        return SuccessResponse(msg='提交成功', data=serializer.data)


class SubmitSerializer1(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    status_text = serializers.CharField(source='get_status_display', read_only=True)

    examine = serializers.SerializerMethodField()

    judge = serializers.SerializerMethodField()

    @classmethod
    def get_examine(cls, obj):
        res = models.Examine.objects.filter(info=obj).first()
        if not res:
            return None
        res.create_time = res.create_time.strftime('%Y-%m-%d %H:%M:%S')
        return model_to_dict(instance=res, fields=['id', 'name', 'opinion', 'info', 'create_time'])

    @classmethod
    def get_judge(cls, obj):
        data = {
            'text': '未超时',
            'overtime': False
        }
        if obj.fanxiao:
            # 当日回校
            target = '{0} {1}'.format(obj.lxsj, obj.cxjs)
        else:
            # 非当日回校
            target = '{0} {1}'.format(obj.fxrq, obj.cxjs)

        local_time = time.strftime("%Y-%m-%d %H:%M", time.localtime())

        if obj.status == 2:
            if local_time > target:
                data['text'] = '已超时'
                data['overtime'] = True

        return data

    class Meta:
        model = models.Info
        fields = '__all__'


# 记录详情
class BookDetailView(APIView):
    def get(self, request, pk):
        """
        获取
        """
        auth = GeneralAuthentication(request)
        if not auth.is_auth():
            return ErrorResponse(**auth.is_auth_data())
        if pk == 0:
            book = models.Info.objects.filter(users=auth.get_object()).order_by('-id').first()
        else:
            book = models.Info.objects.filter(pk=pk, users=auth.get_object()).first()
        if not book:
            return ErrorResponse(code=2, msg='没有记录')
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

        if book.fanxiao:
            # 当日回校
            target = '{0} {1}'.format(book.lxsj, book.cxjs)
        else:
            # 非当日回校
            target = '{0} {1}'.format(book.fxrq, book.cxjs)

        local_time = time.strftime("%Y-%m-%d %H:%M", time.localtime())

        if book.status == 2:
            if local_time > target:
                return ErrorResponse(msg='超过返校时限', code=2)

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


# 出校记录
class RecordListlView(APIView):

    def get(self, request, *args, **kwargs):
        auth = GeneralAuthentication(request)
        if not auth.is_auth():
            return ErrorResponse(**auth.is_auth_data())

        queryset = models.Info.objects.filter(users=auth.get_object()).order_by('-id')
        serializer = SubmitSerializer1(instance=queryset, many=True)

        return SuccessResponse(msg='获取成功', data=serializer.data)


class RechargeViewSerializer(serializers.Serializer):
    phone = serializers.CharField(min_length=4, error_messages={
        'required': '手机号必填',
        'blank': '手机号不能为空',
        'min_length': '请输入手机号后四位',
    })
    money = serializers.CharField(validators=[money_validator, ], error_messages={
        'required': '金额必填',
        'blank': '金额不能为空',
    })

    def validate_phone(self, value):
        if not value.isdecimal():
            raise serializers.ValidationError('手机号只能是数字')

        return value


# 充值
class RechargeView(APIView):

    def post(self, request, *args, **kwargs):

        serializer = RechargeViewSerializer(data=request.data)
        if not serializer.is_valid():
            return SerializerErrorResponse(serializer)

        phone = serializer.validated_data.get('phone')
        money = serializer.validated_data.get('money')

        user = Users.objects.filter(phone__endswith=phone).first()

        if not user:
            return ErrorResponse(msg='账户不存在')

        data = UsersData.objects.get(users=user)
        data.money = F('money') + float(money)
        data.save()

        # 添加记录
        models.Record.objects.create(users=user, money=money)

        return SuccessResponse(msg='充值成功')


class ShowRechargeRecordSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    users = PersonalViewSerializer()

    class Meta:
        model = models.Record
        fields = '__all__'


# 充值记录
class ShowRechargeRecordView(APIView):
    serializer_class = ShowRechargeRecordSerializer

    def get(self, request):
        queryset = models.Record.objects.all().order_by('-id')
        return PaginatorData(self, request, queryset, 100)


# 统计
class PanelView(APIView):
    def get(self, request):
        from django.db.models import Sum
        today = get_ToDay_Type1()
        today_people = Users.objects.filter(create_time__range=today).count()
        today_output = models.Info.objects.filter(create_time__range=today).count()
        total = models.Record.objects.aggregate(sums=Sum('money'))
        total_registered = Users.objects.all().count()
        data = {
            'total': total['sums'] if total['sums'] else 0,
            'today_people': today_people,
            'today_output': today_output,
            'total_registered': total_registered,
        }
        return SuccessResponse(msg='获取成功', data=data)


class ConfigSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Config
        fields = '__all__'


# 配置项
class AppConfigView(APIView):
    @classmethod
    def get(cls, request):
        pid = request.query_params.get('id', 1)
        print(pid)

        queryset = Config.objects.get(pk=pid)
        serializer = ConfigSerializer(instance=queryset)

        return SuccessResponse(msg='获取成功', data=serializer.data)
