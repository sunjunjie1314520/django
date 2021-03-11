
from rest_framework.views import APIView

from utils.Response import SuccessResponse

from . import models

import requests
import datetime

from .fn import *
from utils.Random import get_noncestr

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
        print(request.data)
        code = request.data.get('code')
        try:
            r = requests.get(f'http://fundgz.1234567.com.cn/js/{code}.js')
            if r.status_code == 200:
                result = loads_jsonp(r.text)
                print(result)
        except BaseException as e:
            print(e)
        return SuccessResponse(msg='基金实时信息', data=result)