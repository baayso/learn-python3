#!/usr/bin/env python3
# -*- coding: utf-8 -*-

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

print()

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

print()

# range()函数可以生成一个整数序列
# list()函数可以转换为list
print(list(range(5)))

print()

# range(101)就可以生成0-100的整数序列
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

print()

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
