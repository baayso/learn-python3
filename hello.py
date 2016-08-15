#!/usr/bin/python
# -*- coding: utf-8 -*-

from bson.objectid import ObjectId
import fibo

fibo.fib(1000)
print(fibo.fib2(100))
print("fibo模块名:", fibo.__name__)

name = input('Please enter your name: ')

print(name != None)
print(name is not None)

if name is not None:
    print(name)
else:
    print('''not a
    nothing''')

print('''
not a
number''')

print()

oid = ObjectId()

print(oid.__str__())
print(oid.__repr__())

for n in range(10):
    print(ObjectId().__str__())

print()


# 默认参数最好指向不变对象，否则容易掉坑里
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


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(100))

d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(key)

for k, v in d.items():
    print(k, ':', v)
