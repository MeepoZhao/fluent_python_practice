#!/usr/bin/python
# -*- coding:utf-8 -*-
# Create by MeepoZhao
# Create on 2022/4/10


import time


# 装饰器用于实现日志打印
def logger(func):
    def wrapper(*args, **kwargs):
        print('开始准备执行：{} 函数了：'.format(func.__name__))
        func(*args, **kwargs)
        print('执行完毕！')

    return wrapper


@logger
def add(x: int, y: int) -> None:
    print('{} + {} = {}'.format(x, y, x + y))


# 定义一个时间计时器，用于统计函数的运行时长
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        cost_time = end - start
        print('花费的时间：{}秒'.format(cost_time))

    return wrapper


@timer
def want_sleep(sleep_time):
    time.sleep(sleep_time)


# 定义一个有参构造器，用于根据传递的参数执行不同的方案
def say_hello(country):
    def decorator_say(func):
        def wrapper(*args, **kwargs):
            if country == 'china':
                print('你好！')
            elif country == 'america':
                print('hello!')
            else:
                return

                # 实际执行函数的地方
            func(*args, **kwargs)

        return wrapper

    return decorator_say


@say_hello('china')
def xiao_ming():
    pass


@say_hello('america')
def jack():
    pass


if __name__ == '__main__':
    # add(200, 50)
    # want_sleep(20)
    xiao_ming()
    print('++++++++++++')
    jack()
