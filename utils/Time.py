
from datetime import datetime
import time

def get_timestamp():
    # 1499825149.257892    #原始时间数据
    # 1499825149           #秒级时间戳，10位
    # 1499825149257        #毫秒级时间戳，13位
    # 1499825149257892     #微秒级时间戳，16位
    t = time.time()
    # print (t)                       #原始时间数据
    # print (int(t))                  #秒级时间戳
    # print (int(round(t * 1000)))    #毫秒级时间戳
    # print (int(round(t * 1000000))) #微秒级时间戳
    return int(t)

def formatDate(date):
    print(date)
    return datetime.strptime(date, '%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":
    a = get_timestamp()
    print(a)