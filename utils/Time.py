
from datetime import datetime, timedelta
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

if __name__ == "__main__":
    a = timeToUTC('2020-10-19 01:15:20')
    print(a)
