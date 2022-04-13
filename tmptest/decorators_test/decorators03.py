#!/usr/bin/python
# -*- coding:utf-8 -*-
# Create by MeepoZhao
# Create on 2022/4/12

# 不带参数的类装饰器
"""
基于类的装饰器实现，必须实现__call__和__init__两个内置函数。
__init__:接收被装饰函数
__call__：实现装饰逻辑
"""


class Logger:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('[INFO]: the function {func}() is running...'.format(func=self.func.__name__))
        return self.func(*args, **kwargs)


# 带参数的类装饰器
"""
__init__:不再接收被装饰函数，而是接收传入参数
__call__:接收被装饰函数，实现装饰逻辑
"""


class Logger2:
    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print('[{level}]: the function {func}() is running...'.format(level=self.level, func=func.__name__))
            return func(*args, **kwargs)

        return wrapper


@Logger
def say(something):
    print('say {}!'.format(something))


@Logger2(level='WARNING')
def say2(something):
    print('say {}!'.format(something))


if __name__ == '__main__':
    # say('hello')
    say2('hello')
