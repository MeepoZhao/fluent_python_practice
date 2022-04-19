#!/usr/bin/python
# -*- coding:utf-8 -*-
# Create by MeepoZhao
# Create on 2022/4/19

"""
实现一个BingoCage类，这个类的实例可以使用任何可迭代对象构建，而且会在内部存储一个随机顺序排列的列表
调用实例会取出一个元素
"""

import random


class BingoCage:

    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        return self.pick()


if __name__ == '__main__':
    bingo = BingoCage(range(3))  # 此处运行的是__init__函数
    aa = bingo.pick()  # 列表的最后一个元素被pop，aa获取其值
    bb = bingo()  # 执行__call__函数
    callable(bingo)  # 判断一个对象是否可调用
