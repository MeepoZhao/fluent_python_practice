#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
生成器函数：

"""


def gen():
    i = 2
    while i < 10:
        tmp = yield i  # tmp用于接收send函数的值，当调用next函数时，tmp获取的是None值
        print('tmp:', tmp)
        i += 1
    return '没有更多的数据了'


g = gen()
print(g.send(None))  # 第一次send需要传入None值，返回的是yield右边的值
n1 = g.send('呵呵')
print('n1:', n1)
n2 = g.send('哈哈')
print('n2:', n2)
print(next(g))
