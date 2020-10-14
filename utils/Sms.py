
import requests
import hashlib
import random
from datetime import datetime

def MD5(string):
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    return m.hexdigest()

def RANDOM_CODE():
    return random.randint(100000, 999999)

def SEND_SMS(phone, debug=False):
    # 我们的国内短信接口是http标准协议，接口说明和demo的地址：
    # http://www.b2m.cn/static/doc/sms/onlysms_or.html
    #  
    # 接口可以使用的url地址：
    # http://bjksmtn.b2m.cn
    # http://bjmtn.b2m.cn
    # http://shmtn.b2m.cn
    # 端口是80
    #  
    # http://gzmtn.b2m.cn
    # http://www.btom.cn
    # 端口是8080
    # 可任选，接口里有六种发送方法，用哪种都可以。
    
    random_code = RANDOM_CODE()

    if not debug:
        url = 'http://bjksmtn.b2m.cn/simpleinter/sendSMS'

        appId = 'EUCP-EMY-SMS1-0RNX7'
        secretKey = '138B09C5C7BF9C18'
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        
        data = {
            'appId': appId,
            'timestamp': timestamp,
            'sign': MD5('{0}{1}{2}'.format(appId, secretKey, timestamp)),
            'mobiles': phone,
            'content': '【国寿安保基金】您的验证码为：{code}，验证码5分钟有效'.format(code=random_code),
        }
        
        res = requests.get(url, params=data)
        if res.status_code == 200:
            if res.json()['code'] == 'SUCCESS':
                return {'phone': phone, 'code': random_code, 'success': True}
    return {'phone': phone, 'code': random_code, 'success': False}

if __name__ == "__main__":
    res = SEND_SMS('19871455054, 18827183521')
    print(res)