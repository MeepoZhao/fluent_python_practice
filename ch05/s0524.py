#!/usr/bin/python
# -*- coding:utf-8 -*-
# Create by MeepoZhao
# Create on 2022/4/20

"""
演示attrgetter使用
"""

from collections import namedtuple

LatLong = namedtuple('LatLong', 'lat long')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')
metro_data = [('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
              ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
              ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
              ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
              ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833))
              ]
metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long))
               for name, cc, pop, (lat, long) in metro_data]

print(metro_areas[0])
print(metro_areas[0].coord.lat)

# 使用 attrgetter
from operator import attrgetter

# 获取两个属性，name和coord.lat
name_lat = attrgetter('name', 'coord.lat')

for city in sorted(metro_areas, key=attrgetter('coord.lat')):  # 按照coord.lat进行排序
    print(name_lat(city))  # 从属性中取出两个属性

"""
itemgetter:使用切片或者索引获取对应的元素
attrgetter:使用属性或者是key获取对应的元素
"""
