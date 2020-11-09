from rest_framework.views import APIView

from utils.Response import SuccessResponse

from . import models
from .serializers import GoodsListSerializer


class IndexView(APIView):
    """
    模块首页
    """
    @classmethod
    def get(cls, request, *args, **kwargs):
        return SuccessResponse(msg='GOODS MODULE')


class GoodsListView(APIView):
    """
    产品列表
    """
    @classmethod
    def get(cls, request, *args, **kwargs):
        queryset = models.Goods.objects.all()[:6]
        serializer = GoodsListSerializer(instance=queryset, many=True)
        return SuccessResponse(msg='获取成功', data=serializer.data)
