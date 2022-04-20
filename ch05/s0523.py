#!/usr/bin/python
# -*- coding:utf-8 -*-
# Create by MeepoZhao
# Create on 2022/4/20

"""
演示使用itemgetter排序一个元素列表
itemgetter函数用于替代从序列中取出元素或读取对象属性的lambda表达式
"""

metro_data = [('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
              ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
              ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
              ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
              ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
              ]
from operator import itemgetter

# 按照metro_data各个元素中第二个字段的值进行排序
for city in sorted(metro_data, key=itemgetter(1)):
    print(city)

print('====================>')

cc_name = itemgetter(1, 0)  # 取序列中的(1,0)位置的值
for city in metro_data:
    print(cc_name(city))
