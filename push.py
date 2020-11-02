import os
import requests
from datetime import datetime
import json
from threading import Thread

time = datetime.now().strftime('%Y/%m/%d-%H:%M:%S')

print('开始提交')
os.system('git add ./')
os.system('git commit -m %s' % time)
os.system('git push')
try:
    data = {
        'id': 3,
        'is_update': True,
        'is_migrate': True,
    }
    res = requests.post('http://okami.net.cn:8000/git/set_sync', data=data)
    if res.status_code == 200:
        print(res.text)
        print('已完成提交到GIT => %s' % time)

except BaseException:
    print('network error')
