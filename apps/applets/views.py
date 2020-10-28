from rest_framework.views import APIView

from utils.Response import SuccessResponse, ErrorResponse
from utils.Format import to_JSON_Format

from utils.WXBizDataCrypt import WXBizDataCrypt

import requests

class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return SuccessResponse(msg='applets MODULE')


class Authorize(APIView):
    """
    微信小程序-授权
    """
    def get(self, request, *argw, **kwargw):
        return ErrorResponse(msg='只能用POST请求方法')

    def post(self, request, *argw, **kwargw):
        to_JSON_Format(request.data)
        code = request.data.get('code')
        url = 'https://api.weixin.qq.com/sns/jscode2session'
        data = {
            'appid': 'wxe6e14e059548fa6f',
            'secret': 'a19f011d7f44eb9e621e9bfd96a4abf5',
            'js_code': code,
            'grant_type': 'authorization_code',
        }
        r = requests.get(url=url, params=data)
        if r.status_code == 200:
            return SuccessResponse(msg='授权成功', data=r.json())
        return ErrorResponse(msg='jscode2session获取失败')

class LoginView(APIView):
    """
    微信小程序-登录
    """
    def get(self, request, *args, **kwargs):
        return ErrorResponse(msg='只能用POST请求方法')
    
    def post(self, request, *argw, **kwargw):
        
        to_JSON_Format(request.data)

        appId = 'wxe6e14e059548fa6f'
        sessionKey = request.data.get('sessionKey')
        encryptedData = request.data.get('encryptedData')
        iv = request.data.get('iv')

        pc = WXBizDataCrypt(appId, sessionKey)
        data = pc.decrypt(encryptedData, iv)
        if not data:
            return ErrorResponse(msg='登录失败')
        return SuccessResponse(msg='登录成功', data=data)