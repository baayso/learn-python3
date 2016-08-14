#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ord()函数获取字符的整数表示
print('A:', ord('A'))

print()

# chr()函数把编码转换为对应的字符
print('66:', chr(66))
print('25991:', chr(25991))

print()

print(r'\u4e2d\u6587:', '\u4e2d\u6587')

print()

# 转义
print('\\\t\\')
# r''表示''内部的字符串默认不转义
print(r'\\\t\\')
# 多行内容
print('''line1
line2
line3''')

print()

# bytes类型的数据用带b前缀的单引号或双引号表示
# bytes的每个字符都只占用一个字节
print(b'ABC')

print()

# str通过encode()方法可以编码为指定的bytes
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))

print()

# 含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围
# print('中文'.encode('ascii'))  # 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)

# 要把bytes变为str，用decode()方法：
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print()

# len()函数计算的是str的字符数
print(len('ABC'))
print(len('中文'))

print()

# 换成bytes，len()函数就计算字节数
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

# 格式化方式和C语言一样，用%实现
#   %d    整数
#   %f   浮点数
#   %s   字符串
#   %x   十六进制整数
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))

# 格式化整数和浮点数可以指定是否 补0 和整数与小数的位数
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

# %s会把任何数据类型转换为字符串
print('Age: %s. Gender: %s' % (25, True))

# 用%%来表示一个%
print('growth rate: %d %%' % 7)
