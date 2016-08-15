#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


# 空函数
def nop():
    pass


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


n = my_abs(-20)
print(n)

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

# TypeError: bad operand type:
# my_abs('123')

print()


# 默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5))
print(power(5, 2))

print()


# 默认参数不要指向不变对象
def add_end(L=[]):
    L.append('END')
    return L


# 将上面的函数修改一下
def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())
print(add_end())

print()

print(add_end2())
print(add_end2())

print()


# 可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc())
print(calc(1, 2))

print()
