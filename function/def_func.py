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


# 位置参数（普通参数）


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


# 可变参数，参数前面加了一个*号
# 可变参数在函数调用时自动组装为一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc())
print(calc(1, 2))
print(calc(*[1, 2, 3]))

print()


# 关键字参数
# 关键字参数允许传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
person('Jack', 24, **extra)

print()


# 命名关键字参数
# 如果要限制关键字参数的名字，就可以用命名关键字参数
# 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)


person('Jack', 24, city='Beijing', job='Engineer')


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name, age, *args, city='Beijing', job):
    print(name, age, args, city, job)


person('Jack', 24, *[1, 2, 3], job='Engineer')

print()


# 参数组合
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

print()

# 对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
f1(*(1, 2, 3, 4), **{'d': 99, 'x': '#'})
f2(*(1, 2, 3), **{'d': 88, 'x': '#'})
