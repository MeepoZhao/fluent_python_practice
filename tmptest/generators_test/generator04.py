#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
进程  >  线程  >  协程
协程作为生成器的主要使用场景之一，交替执行任务
"""


def task1(n):
    for i in range(n):
        print('看{}页书'.format(i))
        yield


def task2(n):
    for i in range(n):
        print('听了{}首歌'.format(i))
        yield


g1 = task1(5)
g2 = task2(5)

while True:
    try:
        next(g1)
        next(g2)
    except:
        break
