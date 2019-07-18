# -*- coding: utf-8 -*-
#!/usr/bin/python3
# @Time    : 2019/7/9 10:35 AM
# @Author  : zhaoyang
# @Site    : 
# @File    : task.py
# @Software: PyCharm
from celery import Celery
from Basic import celeryconfig as conf
from Basic.Opera_Kafka import Opera_Kafka
from Basic.Opera_Task import Asyncio_Task

# app = Celery('task',broker='amqp://guest@localhost//')
app=Celery('task')
app.config_from_object(conf)
oa=Asyncio_Task()
@app.task
def func():
    return oa.asyncio_task()

    # return ok.poll_persist_msg(topic_producer)

