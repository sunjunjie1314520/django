
from rest_framework import status
from rest_framework.response import Response

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

def SerializerErrorResponse(serializer, debug=False):
    errors = []
    json_data = serializer.errors
    for i, val in enumerate(json_data):
        if debug:
            errors.append('%s:%s' % (val, json_data[val][0]))
        else:
            errors.append('%s' % (json_data[val][0]))
    return Response(error(msg=errors[0]), status=status.HTTP_200_OK)

def SuccessResponse(data=None, msg=None):
    return Response(success(data=data, msg=msg), status=status.HTTP_200_OK)

def ErrorResponse(code=None, msg=None):
    return Response(error(code=code, msg=msg), status=status.HTTP_200_OK)
        
class BasicView():

    def get(self, request, *argw, **kwargs):
        print(request.query_params.dict())
        return Response({'method': 'GET'}, status=status.HTTP_200_OK)

    def post(self, request, *argw, **kwargs):
        print(request.data.dict())
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return ErrorResponse(serializer)
        serializer.save()
        return Response(success(data=serializer.validated_data, msg='保存成功'), status=status.HTTP_201_CREATED)
