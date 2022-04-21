#!/usr/bin/python
# -*- coding:utf-8 -*-
# Create by MeepoZhao
# Create on 2022/4/21

from s0608 import Order


# 实现各个promotion的函数
def fidelity_promo(order: Order):
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order: Order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount


def large_order_promo(order: Order):
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    return 0
