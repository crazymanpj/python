# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-01-17
# Author:  pangjian
# version: 1.0

from celery import task
import time


@task
def add(x, y):
    for i in range(30):
        print(i)
        time.sleep(1)

    return x + y
