from django.conf import settings
from bs4 import BeautifulSoup

import os

import _thread

import json
import re
from datetime import datetime

import time
import datetime

import requests

from decimal import Decimal

from utils.Sms import SEND_SMS

from utils.Random import get_noncestr

from fund import models

from django.db.models import Q

# git请求
def getPull():
    baseURL = 'http://okami.net.cn:8000/git/'
    try:
        r = requests.post(f'{baseURL}get_sync', data={'id': settings.GIT_ID})
        if r.status_code == 200:
            print(json.dumps(r.json(), sort_keys=True, indent=2, ensure_ascii=False))
            if r.json()['is_update']:
                os.system('git reset --hard')
                data = {
                    'id': settings.GIT_ID,
                    'is_update': False,
                }
                res = requests.post(f'{baseURL}set_sync', data=data)
                if res.status_code == 201:
                    print(json.dumps(res.json(), sort_keys=True, indent=2, ensure_ascii=False))
                os.system('git pull')

            if r.json()['is_migrate']:
                os.system('python manage.py migrate')
                data = {
                    'id': settings.GIT_ID,
                    'is_migrate': False,
                }
                res = requests.post(f'{baseURL}set_sync', data=data)
                if res.status_code == 201:
                    print(json.dumps(res.json(), sort_keys=True, indent=2, ensure_ascii=False))
        else:
            print(r.status_code)

    except BaseException as e:
        print(e)
        print('error', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


# 为线程1定义一个函数
def main1(delay):
    while True:
        time.sleep(delay)
        getPull()


# 判断今天是否为周末
def is_week_lastday():
    now = (datetime.datetime.utcnow() + datetime.timedelta(hours=8))
    sunday = now.weekday()
    # 如果今天是周六、周日，则返回True
    if sunday == 5 or sunday == 6:
        return True
    else:
        return False


def loads_jsonp(jsonp):
    """
        解析jsonp数据格式为json
        :return:
        """
    try:
        return json.loads(re.match(".*?({.*}).*", jsonp, re.S).group(1))
    except:
        raise ValueError('实时估值失败...')


def strHandle(jsonp):
    try:
        str_json = re.search("Data_netWorthTrend.*?(\\[.*?\\]).+?", jsonp, re.S).group(1)
        return json.loads(str_json)
    except:
        raise ValueError('历史净值失败...')


def count(section, day):
    result = section[len(section) - day:]
    result.reverse()
    count = 0
    for item in result:
        count += Decimal(str(item['equityReturn']))
    return count


# 为线程3定义一个函数
def main3(delay, startTime, pages):
    print(f'每天 {startTime} 运行一次')

    class Paa:
        def __init__(self, pages):
            self.page = pages
            self.queryset = models.FundAll.objects.all().exclude(Q(type='货币型') | Q(status=False) | Q(name__contains='后端'))
            self.length = self.queryset.count()

        def getData(self):
            try:
                item = self.queryset[self.page:self.page + 1]
                code = item[0].code
                result = self.history(code)
                print(self.page + 1, self.length, item[0].name, result)
                r = requests.get(f'http://fund.eastmoney.com/pingzhongdata/{code}.js?v={get_noncestr(8)}')
                if r.status_code == 200:
                    section = strHandle(r.text)
                    data = {
                        "day": count(section, 1),
                        "week": result[1],
                        "one_month": result[2],
                        "three_month": result[3],
                        "six_month": result[4],
                    }
                    # print(data)
                    query = models.Future.objects.filter(code=item[0])
                    query.update(**data)
                    query.first().save()
            except BaseException as e:
                print(e)

        @staticmethod
        def history(code):
            arr = []
            res = requests.get(f'http://fundf10.eastmoney.com/FundArchivesDatas.aspx?type=jdzf&code={code}')
            if res.status_code == 200:
                bf = BeautifulSoup(res.text, features="html.parser")
                all_ul = bf.find_all('ul')
                for item in all_ul:
                    first = item.find_all('li', {'class': ['tor grn bold', 'tor red bold']})
                    if len(first) > 0:
                        arr.append(first[0].string.replace('%', ''))
            return arr if len(arr) >= 5 else [0, 0, 0, 0, 0]

        def start(self):
            while self.page < self.length:
                self.getData()
                self.page = self.page + 1



    while True:
        time.sleep(delay)
        now_localtime = time.strftime("%H:%M:%S", time.localtime())
        # print(now_localtime)
        if now_localtime == startTime:
            Paa(pages).start()



if not settings.DEBUG:
    _thread.start_new_thread(main1, (30, ))

_thread.start_new_thread(main3, (1, '22:00:00', 0))
