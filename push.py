import os
import requests
from datetime import datetime
import json
import sys


migrate = True if sys.argv[2] == 'true' else False
git_id = int(sys.argv[1])
if migrate:
    print('本次需要同步数据库')

time = datetime.now().strftime('%Y/%m/%d-%H:%M:%S')

baseURL = 'http://okami.net.cn:8000/git/'

os.system('git add ./')
os.system('git commit -m %s' % time)
os.system('git push')

try:
    data = {
        'id': git_id,
        'is_update': True,
        'is_migrate': migrate,
    }
    res = requests.post(baseURL + 'set_sync', data=data)
    if res.status_code == 201:
        print(json.dumps(res.json(), sort_keys=True, indent=2, ensure_ascii=False))

except BaseException as e:
    print(e)
    print('network error')
