import requests
import base64
import json

class jPush:
    def __init__(self, AppKey, Secret):
        self.url = 'https://api.jpush.cn/v3/push'
        self.AppKey = AppKey
        self.Secret = Secret

    def base64(self, code: str):
        print('String => ', code)
        base_str = base64.b64encode(code.encode('utf-8'))
        return base_str.decode('utf-8')

    def send(self):
        base64_auth_string = self.base64(f'{self.AppKey}:{self.Secret}')
        print('Base64 => ', base64_auth_string)
        header = {
            'Content-Type': 'application/json',
            'Authorization': f'Basic {base64_auth_string}'
        }
        data = {
            # "cid": "1104a897920e6cd0b3a",
            "platform": "all",
            "audience": {
                "registration_id": ['1104a897920e6cd0b3a', '160a3797c8a36914fdc', '18071adc03adc86bf01']
            },
            "notification": {
                "android": {
                    "alert": "Hi, JPush!",
                    "title": "Send to Android",
                    "builder_id": 1,
                    "large_icon": "https://res.wx.qq.com/a/wx_fed/assets/res/OTE0YTAw.png",
                    "intent": {
                        "url": "intent:#Intent;component=com.jiguang.push/com.example.jpushdemo.SettingActivity;end",
                    },
                    "extras": {
                        "newsid": 321
                    }
                },
                "ios": {
                    "alert": "Hi, JPush!",
                    "sound": "default",
                    "badge": "+1",
                    "thread-id": "default",
                    "extras": {
                        "newsid": 321
                    }
                },
                "voip": {
                    "key": "value"
                },
                "quickapp": {
                    "alert": "Hi, JPush!",
                    "title": "Send to QuickApp",
                    "page": "/page1"
                }
            },
            "message": {
                "msg_content": "Hi,JPush",
                "content_type": "text",
                "title": "msg",
                "extras": {
                    "key": "value"
                }
            },
            "sms_message": {
               "temp_id": 1250,
               "temp_para": {
                       "code": "123456"
               },
                "delay_time": 3600,
                "active_filter": False
            },
            "options": {
                "time_to_live": 60,
                "apns_production": False,
                "apns_collapse_id": "jiguang_test_201706011100"
            },
            # "callback": {
            #     "url": "http://www.bilibili.com",
            #     "params": {
            #         "name": "joe",
            #         "age": 26
            #      },
            #      "type": 3
            # }
        }
        res = requests.post(self.url, headers=header, data=json.dumps(data))
        print(res.json())


if __name__ == '__main__':
    push = jPush(AppKey='f409bddab5054afa82669832', Secret='6836d291645fe2c792b6ecf3')
    push.send()
