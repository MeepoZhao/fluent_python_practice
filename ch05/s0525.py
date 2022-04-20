#!/usr/bin/python
# -*- coding:utf-8 -*-
# Create by MeepoZhao
# Create on 2022/4/20

"""
methodcaller使用示例
"""

from operator import methodcaller

s = 'the time has come'
upcase = methodcaller('upper')  # 将upper函数绑定给upcase
print(upcase(s))

hiphenate = methodcaller('replace',' ','-')  # 将replace函数绑定给hiphenate，并限制了参数的值
print(hiphenate(s))