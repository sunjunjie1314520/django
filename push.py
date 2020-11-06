import os
import requests
from datetime import datetime
import json
import sys

try:
    migrate = sys.argv[1]
except BaseException:
    migrate = False

print(migrate)
print(type(migrate))


time = datetime.now().strftime('%Y/%m/%d-%H:%M:%S')

baseURL = 'http://okami.net.cn:8000/git/'

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
    res = requests.post(baseURL + 'set_sync', data=data)
    if res.status_code == 201:
        print(json.dumps(res.json(), sort_keys=True, indent=2, ensure_ascii=False))
        print('已完成提交到GIT => %s' % time)

except BaseException:
    print('network error')
