import time

def timeStamp():
    """
    当前时间戳
    :return:
    """
    return str(time.time()).replace('.', '')

def currentDate():
    """
    年月日
    :return:
    """
    return time.strftime('%Y%m%d', time.localtime())


if __name__ == '__main__':
    # print(timeStamp())
    print(currentDate())
