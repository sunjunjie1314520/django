import jwt

import datetime


headers = {
    'typ': 'jwt',
    'alg': 'HS256',
}

payload = {
    'id': 2,
    'username': 'adimn',
    'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=10*60)
}

encoded_jwt = jwt.encode(payload=payload, key='iv%x6xo7l7_u9bf_u!9#g#m*)*=ej@bek5)(@u3kh*72+unjv=', algorithm='HS256', headers=headers).decode('utf8')

de_code = jwt.decode(encoded_jwt, 'iv%x6xo7l7_u9bf_u!9#g#m*)*=ej@bek5)(@u3kh*72+unjv=', algorithms=['HS256'])
print(encoded_jwt)
print(de_code)
