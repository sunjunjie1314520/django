from rest_framework.views import APIView

from utils.Response import SuccessResponse

from . import tasks

class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return SuccessResponse(msg='API MODULE')
