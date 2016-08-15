#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式


# 生成[1x1, 2x2, 3x3, ..., 10x10]使用循环太繁琐
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

# 列表生成式则可以用一行语句代替循环生成上面的循环
print([x * x for x in range(1, 11)])

print()

# 还可以加上if判断
print([x * x for x in range(1, 11) if x % 2 == 0])

print()

# 还可以使用两层循环，可以生成全排列：
print([m + n for m in 'ABC' for n in 'XYZ'])

print()

# 列出当前目录下的所有文件和目录名
import os

print([d for d in os.listdir('.')])

print()

# 列表生成式也可以使用两个变量来生成list
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print([k + '=' + v for k, v in d.items()])

print()

# 把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])
print([s.lower() for s in L if isinstance(s, str)])
