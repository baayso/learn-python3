#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 取前3个元素
print('L[0:3] =', L[0:3])
# 如果第一个索引是0，可以省略
print('L[:3] =', L[:3])

print()

print('L[1:3] =', L[1:3])
# 倒数第一个元素的索引是-1
print('L[-2:] =', L[-2:])
print('L[-2:-1] =', L[-2:-1])

print()

R = list(range(100))
# 前10个数
print('R[:10] =', R[:10])
# 后10个数
print('R[-10:] =', R[-10:])
# 前11-20个数
print('R[10:20] =', R[10:20])
# 前10个数，每两个取一个
print('R[:10:2] =', R[:10:2])
# 所有数，每5个取一个
print('R[::5] =', R[::5])
# 原样复制一个list
print(L[:])

print()

# tuple也可以用切片操作，结果仍是tuple
print((0, 1, 2, 3, 4, 5)[:3])

print()

# 字符串也可以用切片操作，只是操作结果仍是字符串
# Python没有针对字符串的截取函数，只需要切片一个操作就可以完成
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])
