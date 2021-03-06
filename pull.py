import requests
from time import sleep
from threading import Thread
from datetime import datetime
import os
import json

def task():
    baseURL = 'http://okami.net.cn:8000/git/'
    try:
        r = requests.post(baseURL + 'get_sync', data={'id': 3})
        if r.status_code == 200:
            print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
            if r.json()['is_update']:

                os.system('git reset --hard')
                os.system('git pull')

                data = {
                    'id': 3,
                    'is_update': False,
                }
                res = requests.post(baseURL + 'set_sync', data=data)
                if res.status_code == 201:
                    print(json.dumps(res.json(), sort_keys=True, indent=2, ensure_ascii=False))

            if r.json()['is_migrate']:

                os.system('python manage.py migrate')

                data = {
                    'id': 3,
                    'is_migrate': False,
                }
                res = requests.post(baseURL + 'set_sync', data=data)
                if res.status_code == 201:
                    print(json.dumps(res.json(), sort_keys=True, indent=2, ensure_ascii=False))
        else:
            print(r.status_code)

    except BaseException as e:
        print(e)
        print('error', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


task()

while True:
    sleep(60)
    a = Thread(target=task)
    a.start()
