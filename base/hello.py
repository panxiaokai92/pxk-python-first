#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('1024 * 768 = ',1024*768)

#name = input('please enter your name:')
#print('hello',name)

#first python demo
print('I\'m ok, I\'m fine thanks ')
print('I\'m learning \n python')
print('\\\n\\')
print('\\\t\\')
print('\\\\t\\')
print(r'\\\\"hello world"\t\n')


print('''line1
line2
line3''')

##  r''表示''内部的字符串默认不转义
print(r'''hello,\n
world''')

print(None)

## 等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量
a = 123
print(a)
a = 'Test hello'
print(a)


a = 'ABC'
b = a 
a = 'XYZ'
print(b)

#常量
ABC = 3.1415926232323


print(10/3)
print(9/3)
print(10//3)	#地板除	
print(10%3)

print('Hi, %s, you have $%d.' % ('Michael', 1000000))

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

print('Age: %s. Gender: %s' % (25, True))
print('growth rate: %d %%' % 7)

print('Hello, {0}, 成绩提升了 {1:.2f}%'.format('小明', 17.125))