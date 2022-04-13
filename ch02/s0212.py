#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Filename :s0212.py
@Description :
@Datatime :2022/04/07 14:06:44
@Author :MeepoZhao
@Version :v1.0
'''

from collections import namedtuple


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector({},{})".format(self.x, self.y)
