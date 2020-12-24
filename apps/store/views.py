
from rest_framework.views import APIView

from utils.Response import SuccessResponse
from .models import Type
from .serializers import TypeSerializer

class IndexView(APIView):
    @classmethod
    def get(cls, request, *args, **kwargs):
        return SuccessResponse(msg='Store Module')


class SourceCode(APIView):
    @classmethod
    def get(cls, request, *args, **kwargs):
        return SuccessResponse(msg='Code')


class TypesAll(APIView):
    @classmethod
    def get(cls, request, *args, **kwargs):
        queryset = Type.objects.all()
        serializer = TypeSerializer(instance=queryset, many=True)
        return SuccessResponse(msg='获取成功', data=serializer.data)
