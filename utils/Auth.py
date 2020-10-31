import jwt

from users.models import Users
import datetime
from django.conf import settings


class LoginError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


class GeneralAuthentication:
    status = None
    JWT_SALT = settings.SECRET_KEY
    auth_data = {}

    def __init__(self, request):
        token = request.META.get('HTTP_TOKEN', None)
        try:
            if not token:
                raise LoginError('未登录')

            verified_payload = jwt.decode(token, self.JWT_SALT, algorithms=['HS256'])
            self.id = verified_payload.get('id')
            self.auth_data['data'] = verified_payload
            self.status = True

        except LoginError:
            self.auth_data['msg'] = '用户未登录'
            self.auth_data['code'] = -99
        except jwt.DecodeError:
            self.auth_data['msg'] = 'token认证失败'
            self.auth_data['code'] = -98
        except jwt.exceptions.ExpiredSignatureError:
            self.auth_data['msg'] = 'token已过期'
            self.auth_data['code'] = -97
        except jwt.InvalidTokenError:
            self.auth_data['msg'] = '非法的token'
            self.auth_data['code'] = -96

    def is_auth(self):
        return self.status

    def is_auth_data(self):
        self.status = None
        self.auth_data.pop('data', '没有该键(key)')
        return self.auth_data

    def get_object(self):
        obj = Users.objects.get(pk=self.id)
        return obj


class GenerateToken:
    headers = {
        'typ': 'jwt',
        'alg': 'HS256',
    }

    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=10 * 60)
    }

    def __init__(self, payload):
        encoded_jwt = jwt.encode(payload={**payload, **self.payload}, key=settings.SECRET_KEY, algorithm='HS256', headers=self.headers).decode('utf8')
        de_code = jwt.decode(encoded_jwt, settings.SECRET_KEY, algorithms=['HS256'])
        # print(encoded_jwt)
        if settings.DEBUG:
            print(de_code)
        self.token = {'token': encoded_jwt}

    def get_token(self):
        return self.token
