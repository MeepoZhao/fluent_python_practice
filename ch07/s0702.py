#!/usr/bin/python
# -*- coding:utf-8 -*-
# Create by MeepoZhao
# Create on 2022/4/22

"""
Python执行装饰器的时间

1、函数装饰器在导入模块时立即执行，而被装饰的函数只在明确调用时运行
2、函数装饰器在模块中会优先执行，即使没有调用该功能
"""

registry = []


# 实际使用过程中，装饰器的定义会放到一个单独的模块中
def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func


@register
def f1():
    print('running f1()')


@register
def f2():
    print('running f2()')


def f3():
    print('running f3()')


def main():
    print('runing main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()


if __name__ == '__main__':
    main()
