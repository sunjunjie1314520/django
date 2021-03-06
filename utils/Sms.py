
from django.conf import settings

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

class SEND_SMS:

    def __init__(self, phone):
        self.phone = phone
        self.code = RANDOM_CODE()
    
    def send(self, isDebug=True, content=''):
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

        debug = settings.DEBUG if isDebug else isDebug

        if not debug:
            url = 'http://bjksmtn.b2m.cn/simpleinter/sendSMS'

            appId = 'EUCP-EMY-SMS1-0RNX7'
            secretKey = '138B09C5C7BF9C18'
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            
            data = {
                'appId': appId,
                'timestamp': timestamp,
                'sign': MD5('{0}{1}{2}'.format(appId, secretKey, timestamp)),
                'mobiles': self.phone,
                'content': f'【国寿安保基金】您的验证码为：{self.code}，验证码5分钟有效' if content == '' else content,
            }

            # print(data)

            sendRes = requests.get(url, params=data)

            if sendRes.status_code == 200:
                if sendRes.json()['code'] == 'SUCCESS':
                    print('SUCCESS')
                else:
                    print('FAIL')
            else:
                print('request error')

    def get_data(self):
        debug = settings.DEBUG
        if not debug:
            return None
        return {'code': self.code}


if __name__ == "__main__":
    res = SEND_SMS('19871455054')
    res.send(isDebug=False)
