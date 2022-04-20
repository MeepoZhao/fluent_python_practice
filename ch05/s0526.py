#!/usr/bin/python
# -*- coding:utf-8 -*-
# Create by MeepoZhao
# Create on 2022/4/20

"""
functools.partial函数使用
基于一个函数创建一个新的可调用对象，把原函数的某些参数固定
"""
from operator import mul
from functools import partial

triple = partial(mul, 3)
print(triple(7))
lst = list(map(triple, range(5)))
print(lst)
