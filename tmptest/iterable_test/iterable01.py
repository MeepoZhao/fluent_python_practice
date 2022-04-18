#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
可迭代对象：
迭代器：
如何判断一个对象是否可迭代

迭代器定义：
1、从集合的第一个元素开始方案，直到所有的元素被访问结束
2、迭代器只能往前不能后退
3、可以被next()函数调用并不断返回下一个值的对象称为迭代器
4、可使用iter()函数将一个可迭代对象变为迭代器

Iterable:可迭代对象
    ABC for classes that provide the __iter__() method.
Iterator:迭代器
    ABC for classes that provide the __iter__() and __next__() methods.
"""

from collections.abc import Iterable
from collections.abc import Iterator

lst = [1, 2, 3]
f = isinstance(lst, Iterator)
print(f)
# print(next(lst))

ss = 'abc'
f2 = isinstance(ss, Iterable)
print(f2)

g = (x + 1 for x in range(5))
f3 = isinstance(g, Iterable)
print(f3)
