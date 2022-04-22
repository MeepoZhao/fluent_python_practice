#!/usr/bin/python
# -*- coding:utf-8 -*-
# Create by MeepoZhao
# Create on 2022/4/22

"""
使用装饰器修改电商促销折扣示例
-装饰器功能，使用装饰器将各个促销的函数加入到一个队列中
"""

from ch06.s0608 import Order, Customer, LineItem
from ch06.promotions import *

promos = []


def promotion(promo_func):
    promos.append(promo_func)
    return promo_func


fidelity_promo = promotion(fidelity_promo)
bulk_item_promo = promotion(bulk_item_promo)
large_order_promo = promotion(large_order_promo)


def best_promo(order: Order):
    return max(promo(order) for promo in promos)


if __name__ == '__main__':
    joe = Customer('John', 0)
    ann = Customer('Ann', 1100)
    cart = [LineItem('banana', 4, 0.5),
            LineItem('apple', 10, 1.5),
            LineItem('watermellon', 5, 5.0)]

    cart2 = [LineItem(str(name), 15, 5) for name in range(25)]
    print(Order(ann, cart2, fidelity_promo))
    print(Order(ann, cart2, bulk_item_promo))
    print(Order(ann, cart2, large_order_promo))
    print(Order(ann, cart2, best_promo))
