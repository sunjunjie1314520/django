
import jwt
from utils.Response import SuccessResponse, ErrorResponse, SerializerErrorResponse
from django.forms.models import model_to_dict
from example.models import User

class GeneralAuthentication:

    status = None
    JWT_SALT = 'iv%x6xo7l7_u9bf_u!9#g#m*)*=ej@bek5)(@u3kh*72+unjv='
    auth_data = {}

    def __init__(self, request):
        token = request.META.get('HTTP_TOKEN', None)
        if not token:
            return ErrorResponse(code=3, msg='未登录')
        try:
            verified_payload = jwt.decode(token, self.JWT_SALT, algorithms=['HS256'])
            self.id = verified_payload.get('id')
            self.auth_data['data'] = verified_payload
            self.status = True
        except jwt.exceptions.ExpiredSignatureError:
            self.auth_data['msg'] = 'token已失效'
            self.auth_data['code'] = 2
        except jwt.DecodeError:
            self.auth_data['msg'] = 'token认证失败'
            self.auth_data['code'] = 3
        except jwt.InvalidTokenError:
            self.auth_data['msg'] = '非法的token'
            self.auth_data['code'] = 4

    def is_auth(self):
        return self.status

    def is_auth_data(self):
        return self.auth_data

    def get_object(self):
        obj = User.objects.get(pk=self.id)
        return obj
