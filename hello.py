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

oid = ObjectId()

print(oid.__str__())
print(oid.__repr__())

for n in range(10):
    print(ObjectId().__str__())


def add_end(L=[]):
    L.append('END')
    return L


print(add_end())
print(add_end())


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
