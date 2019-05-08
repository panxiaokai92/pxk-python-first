#函数 function


#调用函数
print(int('123'))
print(int(12.35))
print(str(1.23))
print(bool(1))
print(bool(''))
print(max(-1,0,4,6,234))

#定义函数,取绝对值
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
        
print(my_abs(-9))   

#取绝对值-添加对参数校验（只允许整数和浮点数）
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x     

#print(my_abs('A'))  

#函数返回多个值？ 假象。本质上返回的是tuple，语法上返回tuple可以省略括号，
#而多个变量可以同时接收一个tuple，按位置赋值给相应的值
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x,y)    



#例子：计算x2的函数
def power(x):
    return x * x

#位置参数--改造成n次方
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

#默认参数 -- 改造成2、n次方（不需要修改原先的x2的代码，即power(5) == power(5,2)）
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
    #注意点：默认参数必须指向不变的对象
    
#可变参数 -- 调用时，先组装list或者tuple
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum  
    
print(calc([1, 2, 3])) 
print(calc((1,3,5,7)))    

#可变参数 -- 改造 
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1, 2, 3)) 
print(calc(1,3,5,7))  

#可变参数 -- 改造（已经存在list或者tuple）
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

nums = [1, 2, 3]    
print(calc(nums[0], nums[1], nums[2]))
print(*nums)


#关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
    
print(person('Bob', 35, city='Beijing'))    
print(person('Adam', 45, gender='M', job='Engineer'))

#关键字参数 -- 改造（已经存在list或者tuple）
extra = {'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack', 24, city=extra['city'], job=extra['job']))
print(person('Jack', 24, **extra))

#命名关键字参数 -- 限制关键字参数的名字
def person(name, age, *, city, job):
    print(name, age, city, job)

print(person("pxk",1234,city="hangzhou",job="manager"))    

#参数组合
#Python中定义的参数，有必选参数、默认参数、可变参数、关键字参数和命名关键字参数5种，可以组合使用。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
    

print(f1(1, 2, 3, 'a', 'b'))    
print(f1(1, 2, 3, 'a', 'b', x=99))
print(f2(1, 2, d=99, ext=None))
    
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
print(f1(*args, **kw))

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
print(f2(*args, **kw))






