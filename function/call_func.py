#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = abs(100)
y = abs(-20)
print(x, y)

print()

# 以下函数可以接收任意多个参数
print('max(1, 2, 3) =', max(1, 2, 3))
print('min(1, 2, 3) =', min(1, 2, 3))
print('sum([1, 2, 3]) =', sum([1, 2, 3]))

print()

# 数据类型转换
print(int('123'))
print(int(12.34))
print(float('12.34'))
print(str(1.23))
print(str(100))
print(bool(1))
print(bool(0))
print(bool('he'))
print(bool(''))
print(bool(None))

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a = abs  # 变量a指向abs函数
print(a(-1))  # 所以也可以通过a调用abs函数
