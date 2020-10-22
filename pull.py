import requests
from time import sleep
from threading import Thread
from datetime import datetime
import os

baseURL = 'http://www.okami.net.cn:8000/git/'

def task():
    try:
        r = requests.post(baseURL + 'get_sync', data={'id': 3})
        if r.status_code == 200:
            print(r.json())
            if r.json()['is_update']:
                print('true-刷新')
                if r.json()['is_migrate']:
                    os.system('m2.bat')
                os.system('git reset --hard')
                os.system('git pull')
                data = {
                    'id': 3,
                    'is_update': 'false',
                }
                res = requests.post(baseURL + 'set_sync', data=data)
                if res.status_code == 200:
                    os.system('cls')
                    print(res.text)
            else:
                print('flase-不刷新')
        else:
            print(r.status_code)
    except BaseException:
        print('error', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

task()

while True:
    sleep(120)
    a = Thread(target=task)
    a.start()
