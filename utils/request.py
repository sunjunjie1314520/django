
import requests
import os
import json

baseURL = 'http://okami.net.cn:8000/git/'

data = {
    'id': 3,
    'is_migrate': False,
}
res = requests.post(baseURL + 'set_sync', data=data)
if res.status_code == 201:
    print(json.dumps(res.json(), sort_keys=True, indent=2, ensure_ascii=False))
    os.system('python manage.py migrate')
