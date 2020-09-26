import os
import requests
from datetime import datetime
import json
from threading import Thread

time = datetime.now().strftime('%Y/%m/%d-%H:%M:%S')

os.system('git add ./')
print('开始提交')
os.system('git commit -m %s' % time)
os.system('git push')
try:
    data = {
        'id': 1,
        'is_update': 'true',
    }
    res = requests.post('http://www.okami.net.cn:8000/git/set_sync', data=data)
    if res.status_code==200:
        print(res.text)
        print('已完成提交到GIT => %s' % time)

except BaseException:
    print('network error')
