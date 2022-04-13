#!/usr/bin/python
# -*- coding:utf-8 -*-
# Create by MeepoZhao
# Create on 2022/4/13

"""
创建一个从单词到其出现情况的映射
即从索引中获取单词出现的频率信息，并把它们写进对应的列表中
"""

import sys
import re

# 一个正则表达式，用于查找单词
WORD_RE = re.compile(r'\w+')
# 使用一个字典记录各个单词出现的位置
index = {}
# 打开一个文件
with open(sys.argv[1], encoding='utf-8') as fp:
    # enumerate()第一个参数为可迭代对象，第二个参数是序号从何处开始，整体返回一个生成器
    for line_no, line in enumerate(fp, 1):
        # 遍历一行记录，对查找的单词
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # occurrences = index.get(word, [])
            # occurrences.append(location)
            # index[word] = occurrences
            # 使用一行代码用于替换上面的三行代码
            # setdefault()用于将字段中key对应的value设置为默认值，如果key在字典中存在，就不变更，最后返回key对应的值
            # index.setdefault(word, [])会获得word对应的列表，word不存在就返回一个空列表
            # 然后该列表会执行append操作，该操作是在原列表上执行的
            index.setdefault(word, []).append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])
