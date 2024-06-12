# -*- coding: utf-8 -*-

from threading import Thread
import time


def my_func():
    print("开始执行")
    # 模拟耗时操作
    time.sleep(2)
    print("执行完毕")
