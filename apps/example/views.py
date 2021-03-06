from rest_framework.views import APIView

from utils.Response import SuccessResponse, ErrorResponse, SerializerErrorResponse
from utils.Paginator import PaginatorData
from utils.Auth import Authentication, Permission
from django.utils.decorators import method_decorator

from . import models
from .serializer import NewsModelSerializer
from users.serializers import UsersSerializer

class BookListView(APIView):
    serializer_class = UsersSerializer

    def get(self, request, *args, **kwargs):
        """
        查询所有用户
        """
        queryset = models.User.objects.all()
        return PaginatorData(self, request, queryset, 3)

    def post(self, request):
        """
        添加书箱
        """
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return SerializerErrorResponse(serializer)
        serializer.save()
        return SuccessResponse(msg='保存成功', data=serializer.data)


class BookDetailView(APIView):
    def get(self, request, pk):
        """
        获取详情
        """
        book = models.User.objects.filter(id=pk).first()
        if not book:
            return ErrorResponse(code=2, msg='详情不存在')
        serializer = UsersSerializer(instance=book)
        return SuccessResponse(msg='详情获取成功', data=serializer.data)

    def put(self, request, pk):
        """
        修改一本书籍
        """
        book = models.User.objects.filter(id=pk).first()
        if not book:
            return ErrorResponse(code=2, msg='详情不存在')
        book_data = request.data
        serializer = UsersSerializer(instance=book, data=book_data)
        if not serializer.is_valid():
            return SerializerErrorResponse(serializer)
        serializer.save()
        return SuccessResponse(msg='详情修改成功', data=serializer.data)

    def delete(self, request, pk):
        """
        删除一本书籍
        """
        book = models.User.objects.filter(id=pk).first()
        if not book:
            return ErrorResponse(code=2, msg='详情不存在')
        book.delete()
        return SuccessResponse(msg='删除成功')


class AuthView(APIView):
    @method_decorator(Authentication)
    def post(self, request, *args, **kwargs):

        queryset = models.User.objects.all()
        serializer = UsersSerializer(instance=queryset, many=True)

        return SuccessResponse(msg='测试登录成功', data=serializer.data)


class NewsDetailView(APIView):
    @method_decorator(Authentication)
    # @method_decorator(Permission)
    def get(self, request, pk):
        news = models.News.objects.filter(id=pk).first()
        if not news:
            return ErrorResponse(code=2, msg='动态不存在')
        serializer = NewsModelSerializer(instance=news, context={'request': request})
        return SuccessResponse(msg='动态详情获取成功', data=serializer.data)
