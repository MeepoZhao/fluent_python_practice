#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
使用yield创建生成器，并创建斐波那契函数
yield 相当于 return + 暂停
斐波那契数列：前两个元素的和等于当前元素
"""


def fibo(n):
    """
    :param n: 输入一个整数，表示斐波那契数列中的第几个元素
    :return: 返回前n个元素的值
    """
    # 初始化变量的值
    a, b = 0, 1
    index = 0
    while index < n:
        yield b
        a, b = b, a + b
        index += 1


g = fibo(5)

for x in range(5):
    print(next(g))
