from django.conf import settings

import os
import sys
import django

import _thread

import json
import re
from datetime import datetime

import time
import datetime

import requests

from utils.Sms import SEND_SMS

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(base_dir)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")

django.setup()

from fund import models


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

# 为线程2定义一个函数
def main2(delay, timeArea):
    while True:
        time.sleep(delay)
        if not is_week_lastday():
            now_localtime = time.strftime("%H:%M:%S", time.localtime())
            # print(now_localtime)

            queryset = models.Profit.objects.all()
            if now_localtime == timeArea:
                for item in queryset:
                    End(item)
        else:
            pass


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
        raise ValueError('Invalid Input')


def strHandle(jsonp):
    try:
        str_json = re.search("Data_netWorthTrend.*?(\\[.*?\\]).+?", jsonp, re.S).group(1)
        return json.loads(str_json)[-1]
    except:
        raise ValueError('strHandle Invalid Input')


# 基金实时信息
def Start(item):
    try:
        r = requests.get(f'http://fundgz.1234567.com.cn/js/{item.code}.js')
        if r.status_code == 200:
            result = loads_jsonp(r.text)
            print(result)
            a = SEND_SMS(item.phone)
            a.send(isDebug=False, content=f"【国寿安保基金】-------\n名称：{result['name']}\n估值：{result['gszzl']}%\n时间：{result['gztime']}")
        else:
            print(r.status_code)

    except BaseException as e:
        print(e)
        print('error', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


# 基金净值时间
def End(item):
    try:
        money = item.money
        r = requests.get(f'http://fund.eastmoney.com/pingzhongdata/{item.code}.js')
        if r.status_code == 200:
            result = strHandle(r.text)
            print(result)
            dateArray = datetime.datetime.fromtimestamp(result['x'] / 1000)
            timer = dateArray.strftime("%Y-%m-%d")
            ying = round(result['equityReturn'] / 100 * money, 2)
            item.sum = item.sum + ying
            item.money = item.money + ying
            item.save()
            a = SEND_SMS(item.phone)
            a.send(isDebug=False, content=f"【国寿安保基金】-------\n名称：{item.name}\n时间：{timer}\n总金额：{money}\n本日净值：{result['equityReturn']}%\n本日盈利：{ying}元\n累计收益：{item.sum}元")
        else:
            print(r.status_code)

    except BaseException as e:
        print(e)


if not settings.DEBUG:
    _thread.start_new_thread(main1, (30, ))
    _thread.start_new_thread(main2, (1, '22:00:00'))
