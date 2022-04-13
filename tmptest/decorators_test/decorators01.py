#!/usr/bin/python
# -*- coding:utf-8 -*-
# Create by MeepoZhao
# Create on 2022/4/10

# 装饰器：实质是对函数进行封装，将实际调用的函数放入到包装中

def decorfun(func):
    def wrapper():
        print('铺地板')
        return func()

    return wrapper


@decorfun
def house():
    print('房子装修中')


house()  # 此处的用法相当于 house = decorfun(house)
