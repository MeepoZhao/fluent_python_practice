#!/usr/bin/python
# -*- coding:utf-8 -*-
# Create by MeepoZhao
# Create on 2022/4/20

"""
使用reduce函数和一个匿名函数计算阶乘
"""

from functools import reduce


def fact(n):
    return reduce(lambda a, b: a * b, range(1, n + 1))


# 使用operator包中的函数计算乘积
from operator import mul


def fact2(n):
    return reduce(mul, range(1, n + 1))
