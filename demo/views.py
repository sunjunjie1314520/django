from utils.Response import SuccessResponse, ErrorResponse
from rest_framework.views import APIView


class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return SuccessResponse(msg='首页')
