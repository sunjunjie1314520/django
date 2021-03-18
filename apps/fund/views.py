
from rest_framework.views import APIView
from django.db.models import Q
from utils.Response import SuccessResponse, ErrorResponse

from . import models

import requests
import datetime

from .fn import *
from utils.Random import get_noncestr
from rest_framework import serializers


class IndexView(APIView):
    """
    模块首页
    """
    @classmethod
    def get(cls, request, *args, **kwargs):
        return SuccessResponse(msg='FUND MODULE')


class SearchListView(APIView):
    """
    基金历史净值
    """
    @classmethod
    def post(self, request):
        print(request.data)
        code = request.data.get('code')
        try:
            r = requests.get(f'http://fund.eastmoney.com/pingzhongdata/{code}.js??v={get_noncestr(8)}')
            if r.status_code == 200:
                section = strHandle(r.text)
                result = section[len(section) - 60:]
                result.reverse()
                for item in result:
                    dateArray = datetime.datetime.fromtimestamp(item['x'] / 1000)
                    timer = dateArray.strftime("%Y-%m-%d")
                    item['time'] = timer
                # print(result)
        except BaseException as e:
            print(e)
        return SuccessResponse(msg='基金历史净值', data=result)


class RealtimeListView(APIView):
    """
    基金实时信息
    """
    @classmethod
    def post(self, request):
        code = request.data.get('code')
        try:
            r = requests.get(f'http://fundgz.1234567.com.cn/js/{code}.js')
            if r.status_code == 200:
                result = loads_jsonp(r.text)
                models.Future.objects.filter(code__code=result['fundcode']).update(today=result['gszzl'])
            else:
                return ErrorResponse(msg='基金代码有误', code=404)
        except BaseException as e:
            print(e)
            return ErrorResponse(msg=f'{code}-基金没有实时信息', code=500)
        return SuccessResponse(msg='基金实时信息', data=result)


class User(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = models.User
        fields = '__all__'


class GoodsListSerializer1(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = models.FundAll
        fields = '__all__'


class GoodsListSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    update_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    code = GoodsListSerializer1()
    checked = serializers.SerializerMethodField()

    def get_checked(self, instance):
        return False

    class Meta:
        model = models.Future
        fields = '__all__'


class SortView(APIView):
    def post(self, request):
        order = request.data.get('order_by')
        code = request.data.get('code')
        # print(code, order)
        queryset = models.Future.objects.filter(Q(code__code__contains=code) | Q(code__name__contains=code), code__status=True).order_by(f'-{order}', '-create_time')[:100]
        serializer = GoodsListSerializer(instance=queryset, many=True)
        return SuccessResponse(msg='热门基金排行', data=serializer.data)


class GoodsListSerializer2(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    fund = GoodsListSerializer()
    checked = serializers.SerializerMethodField()

    def get_checked(self, instance):
        return True

    class Meta:
        model = models.Collection
        exclude = ['user']


class Optional(APIView):
    def post(self, request):
        uid = request.data.get('uid')
        queryset = models.Collection.objects.filter(user_id=uid).order_by('-fund__today')
        serializer = GoodsListSerializer2(instance=queryset, many=True)
        return SuccessResponse(msg='用户自选', data=serializer.data)


class SetTopView(APIView):
    def post(self, request):
        id = request.data.get('id')
        checked = request.data.get('checked')
        uid = request.data.get('uid')
        query = models.User.objects.filter(pk=uid).exists()
        if not query:
            return ErrorResponse(msg='无法自选，请与管理员联系！')
        if checked:
            models.Collection.objects.create(fund_id=id, user_id=uid)
            msg = f'{id}-设置成功'
        else:
            models.Collection.objects.filter(fund_id=id).delete()
            msg = f'{id}-取消成功'
            models.Future.objects.filter(pk=id).update(today=0)
        return SuccessResponse(msg=msg)
