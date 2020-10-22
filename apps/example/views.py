from rest_framework.views import APIView

from utils.Response import SuccessResponse, ErrorResponse, SerializerErrorResponse

from . import models
from .serializer import BookModelSerializer

class BookListView(APIView):
    def get(self, request, *args, **kwargs):
        '''列表视图：查询所有书籍'''
        book = models.User.objects.all()
        serializer = BookModelSerializer(instance=book, many=True)
        return SuccessResponse(msg='列表获取成功', data=serializer.data)

    def post(self, request):
        serializer = BookModelSerializer(data=request.data)
        if not serializer.is_valid():
            return SerializerErrorResponse(serializer, debug=True)
        serializer.save()
        return SuccessResponse(msg='保存成功', data=serializer.data)

class BookDetailView(APIView):
    def get(self, request, book_id):
        book = models.User.objects.filter(id=book_id).first()
        if not book:
            return ErrorResponse(code=2, msg='详情不存在')
        serializer = BookModelSerializer(instance=book)
        return SuccessResponse(msg='详情获取成功', data=serializer.data)

    def put(self,request,book_id):
        '''修改一本书籍'''
        book = models.User.objects.filter(id=book_id).first()
        if not book:
            return ErrorResponse(code=2, msg='详情不存在')
        book_data = request.data
        serializer = BookModelSerializer(instance=book, data=book_data)
        if not serializer.is_valid():
            return SerializerErrorResponse(serializer, debug=True)
        serializer.save()
        return SuccessResponse(msg='详情修改成功', data=serializer.data)

    def delete(self,request,book_id):
        '''删除一本书籍'''
        book = models.User.objects.filter(id=book_id).first()
        if not book:
            return ErrorResponse(code=2, msg='详情不存在')
        book.delete()
        return SuccessResponse(msg='删除成功')