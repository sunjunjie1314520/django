
from rest_framework import status
from rest_framework.response import Response

from django.conf import settings


def success(code=0, msg=None, data=None):
    data = {
        'code': code,
        'msg': msg,
        'data': data,
    }
    return data

def error(code=1, msg=None):
    data = {
        'code': code,
        'msg': msg,
    }
    return data

def SerializerErrorResponse(serializer):
    errors = []
    json_data = serializer.errors
    for i, val in enumerate(json_data):
        if settings.DEBUG:
            errors.append('%s:%s' % (val, json_data[val][0]))
        else:
            errors.append('%s' % (json_data[val][0]))
    return Response(error(msg=errors[0]), status=status.HTTP_200_OK)

def SuccessResponse(**kwargs):
    return Response(success(**kwargs), status=status.HTTP_200_OK)

def ErrorResponse(**kwargs):
    return Response(error(**kwargs), status=status.HTTP_200_OK)

