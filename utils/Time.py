
from datetime import datetime, timedelta, date
import time

def get_timestamp():
    t = time.time()
    
    # print (t)                       #原始时间数据
    # print (int(t))                  #秒级时间戳
    # print (int(round(t * 1000)))    #毫秒级时间戳
    # print (int(round(t * 1000000))) #微秒级时间戳

    # 1499825149.257892    #原始时间数据
    # 1499825149           #秒级时间戳，10位
    # 1499825149257        #毫秒级时间戳，13位
    # 1499825149257892     #微秒级时间戳，16位
    return int(t)

def formatDate(date):
    """
    时间格式化  // 2020-10-18 20:16:30
    """
    return datetime.strptime(date, '%Y-%m-%d %H:%M:%S')


def NowTimeToUTC(seconds):
    """
    当前时间转UTC时间
    """
    ctime = datetime.now()
    utc = datetime.utcfromtimestamp(ctime.timestamp())
    c_time_delta = utc + timedelta(seconds=seconds)
    return c_time_delta

def SetTimeToUTC(tss1):
    """
    指定时间转UTC时间
    """
    timeArray = time.strptime(tss1, "%Y-%m-%d %H:%M:%S")
    # 转为时间戳
    timeStamp = int(time.mktime(timeArray))
    return datetime.utcfromtimestamp(timeStamp)

def get_ToDay_Type1(str_time=None):
    """
    获取今天的时间
    """
    curr_time = time.localtime()
    if str_time:
        curr_time = time.strptime(str_time, "%Y-%m-%d")
    start = time.strftime("%Y-%m-%d 00:00:00", curr_time)
    end = time.strftime("%Y-%m-%d 23:59:59", curr_time)
    return [start, end]


def get_ToDay_Type2(str_time=None):
    """
    获取今天的时间
    """
    de = time.strptime(str_time, "%Y-%m-%d")
    y = de.tm_year
    m = de.tm_mon
    d = de.tm_mday
    start = datetime(y,m,d)
    end = start + timedelta(days=1)
    print(start, end)
    return [start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d')]


def get_ToDay_Type3(str_time=None):
    """
    获取今天的时间
    """
    de = time.strptime(str_time, "%Y-%m-%d %H:%M:%S")
    y = de.tm_year
    m = de.tm_mon
    d = de.tm_mday
    h = de.tm_hour
    m1 = de.tm_min
    s = de.tm_sec
    start = datetime(y, m, d, h, m1, s)
    end = start + timedelta(minutes=15, seconds=0)
    return [start.strftime('%Y-%m-%d %H:%M:%S'), end.strftime('%Y-%m-%d %H:%M:%S')]


if __name__ == "__main__":
    a = get_ToDay_Type3('2020-11-02 22:44:00')
    print(a)
