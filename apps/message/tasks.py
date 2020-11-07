
from celery import shared_task
from . import models
import _thread
import time

def query():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

# 为线程定义一个函数
def print_time(threadName, delay):
   while True:
        time.sleep(delay)
        query()

# _thread.start_new_thread(print_time, ("Thread-1", 3))

@shared_task()
def add(x, y):
    return x + y

@shared_task
def jian(x, y):
    return x - y