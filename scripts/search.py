import os
import sys
import django
import requests
import re
import json

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")
django.setup()

from fund import models

def search(url):
    res = requests.get(url)
    if res.status_code == 200:
        result = re.search("\\[.*\\]", res.text, re.S).group()
        data = json.loads(result)
        for item in data:
            print(item)
            a = models.FundAll.objects.create(code=item[0], name=item[2], type=item[3])
            models.Future.objects.create(code=a)
        # print(f'一共有{len(data)}只基金')


if __name__ == '__main__':
    search('http://fund.eastmoney.com/js/fundcode_search.js')
